import sys
from time import time
import pandas as pd
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom

def calculate_distance(df, lang_1, lang_2, output_file):
    lang_1_words = df[lang_1]
    lang_2_words = df[lang_2]

    output = []
    comp = Istcom()
    distances = []
    for i, word in enumerate(lang_1_words):
        if isinstance(word, str) and len(word) > 0 and isinstance(lang_2_words[i], str) and len(lang_2_words[i]) > 0:
            istr1 = Istr(word)
            istr2 = Istr(lang_2_words[i])
            comp.compare(istr1, istr2)
            distance = comp.distance / (len(istr1) + len(istr2)) * 5
            distances.append(distance)
            output.append((distance*1000//1/1000, word, lang_2_words[i]))
    return distances, output

def main(argv):
    start = time()
    df = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')

    # for col1 in df.columns:
    matrix = []
    for i, col1 in enumerate(df.columns):
        row = []
        for j, col2 in enumerate(df.columns):
            if i <= j:
                row.append('')
                continue
            print(col1, col2)
            distances, output = calculate_distance(df, col1, col2, None)
            if len(distances) > 20:
                # out = list(map(lambda x: f'{x[0]}: {x[1]} {x[2]}', output))
                row.append(f'{sum(distances)/len(distances)*100000//1/100000}')
            else:
                row.append('-')
        matrix.append(row)

    df2 = pd.DataFrame(matrix, index=df.columns, columns=df.columns)
    df2.to_csv(argv[1])

    end = time()
    print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
