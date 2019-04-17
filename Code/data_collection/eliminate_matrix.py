import sys
import time
import pandas as pd

def construct_graph(df):
    rows = df.index.tolist()

    print(df)
    lang_vertices = {}
    word_vertices = {}

    for row in rows:
        word_vertices[row] = set()

    count = 0
    for col in df:
        s = set()
        for row in rows:
            cell = df[col][row]
            cell = cell.strip()
            if len(cell) > 0:
                count += 1
                word_vertices[row].add(col)
                s.add(row)
        lang_vertices[col] = s
    # print(lang_vertices, word_vertices)
    print(count)
    return lang_vertices, word_vertices

def find_minimal_vertices(vs):
    min = 1000000
    argmins = []
    for key in vs:
        n = len(vs[key])
        if n < min:
            min = n
            argmins = [key]
        elif n == min:
            argmins.append(key)
    return argmins, min

def find_minimal_vertex(lang_vs, word_vs):
    argmin_ls, min_l = find_minimal_vertices(lang_vs)
    argmin_ws, min_w = find_minimal_vertices(word_vs)
    if min_l == len(word_vs) and min_w == len(lang_vs):
        return None, ''
    if min_l < min_w:
        vs, xvs, argmin_vs, min_v, side = lang_vs, word_vs, argmin_ls, min_l, 'lang'
    else:
        vs, xvs, argmin_vs, min_v, side = word_vs, lang_vs, argmin_ws, min_w, 'word'
    min = 1000000
    argmin = None
    for argmin_v in argmin_vs:
        # print('argmin_v:', argmin_v)
        s = sum(len(xvs[v]) for v in vs[argmin_v])
        min, argmin, = (s, argmin_v) if s < min else (min, argmin)
    return argmin, side

def remove_vertex(v, vs, xvs):
    s = vs.pop(v)
    for a in s:
        xvs[a].remove(v)

def main(argv):
    df = pd.read_csv(argv[0], index_col=0).fillna('')
    lang_vertices, word_vertices = construct_graph(df)

    start = time.time()
    i = 0
    while True:
        print("iter:", i)
        minimal_vertex, side = find_minimal_vertex(lang_vertices, word_vertices)
        if minimal_vertex is None:
            break
        vs, xvs = (lang_vertices, word_vertices) if side == 'lang' else (word_vertices, lang_vertices)
        # print(minimal_vertex)
        remove_vertex(minimal_vertex, vs, xvs)
        # print(lang_vertices, word_vertices)
        i += 1
    end = time.time()

    # print(lang_vertices, word_vertices)
    df_f = df.loc[list(word_vertices.keys()), list(lang_vertices.keys())]
    print(df_f)
    print('Took', "%.3f" % (end-start), 'seconds')
    df_f.to_csv(argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
