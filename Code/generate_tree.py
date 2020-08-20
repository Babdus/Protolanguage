import sys
from time import time
import pandas as pd
import numpy as np
from distance_dict_to_tree_dict import distance_to_tree

def generate(argv):
    d = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')
    start = time()

    for l1 in d.columns:
        for l2 in d.columns:
            if l1 == l2:
                d[l1][l2] = 0
            elif d[l1][l2] == '':
                d[l1][l2] = d[l2][l1]

    Q = pd.DataFrame(columns=d.columns, index=d.columns)
    delta = {}

    n = d.shape[0]
    while n > 1:
        #1 Compute Q matrix
        for a in d.columns:
            for b in d.columns:
                if a != b:
                    Q[a][b] = (n-2)*d[a][b] - sum(d[a][k] for k in d.columns) - sum(d[b][k] for k in d.columns)
                # else:
                #     Q[a][b] = 0

        # Q.astype(np.float16)

        #2 Find pair with minimal value in Q
        # try:
        a, b = Q.stack().astype(np.float16).idxmin()
        # except TypeError:
        #     print(Q)
        #     exit()

        #3 Create parent node for minimal found pair and assign edge lengths
        ab = a+'.'+b
        if n == 2:
            delta[(a, ab)] = 0.5*d[a][b]
        else:
            delta[(a, ab)] = 0.5*d[a][b] + 1/(2*(n-2)) * (sum(d[a][k] for k in d.columns) - sum(d[b][k] for k in d.columns))
        delta[(b, ab)] = d[a][b] - delta[(a, ab)]

        #4 Add row and column to d for new node
        d[ab] = [0]*n

        matrix = d.values.tolist()
        matrix.append([0]*(n+1))
        d = pd.DataFrame(matrix, columns=d.columns, index=d.columns)

        #5 Define distances to other nodes from new one
        for k in d.columns:
            if k != ab:
                d[k][ab] = d[ab][k] = 0.5 * (d[a][k] + d[b][k] - d[a][b])

        #6 Remove columns and rows for already parented nodes
        d = d.drop([a, b])
        d = d.drop([a, b], 1)

        Q = pd.DataFrame(columns=d.columns, index=d.columns)

        n = d.shape[0]

    end = time()

    t_json = distance_to_tree(delta)
    with open(argv[1], 'w') as out:
        out.write(t_json)

    print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    generate(sys.argv[1:])
