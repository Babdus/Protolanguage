import sys
import pandas as pd
from distance_dict_to_tree_dict import distance_to_tree

def main(argv):
    d = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')
    print(d)

    for l1 in d.columns:
        for l2 in d.columns:
            if l1 == l2:
                d[l1][l2] = 0
            elif d[l1][l2] == '':
                d[l1][l2] = d[l2][l1]

    print(d)

    Q = pd.DataFrame(columns=d.columns, index=d.columns)
    print(Q)

    delta = {}

    n = d.shape[0]
    while n > 1:

        print('\033[34;1md\033[0m')
        print(d)

        #1 Compute Q matrix
        for a in d.columns:
            for b in d.columns:
                if a != b:
                    Q[a][b] = (n-2)*d[a][b] - sum(d[a][k] for k in d.columns) - sum(d[b][k] for k in d.columns)

        print('\033[33;1mQ\033[0m')
        print(Q)

        #2 Find pair with minimal value in Q
        a, b = Q.stack().idxmin()

        #3 Create parent node for minimal found pair and assign edge lengths
        ab = a+b
        if n == 2:
            delta[(a, ab)] = 0.5*d[a][b]
        else:
            delta[(a, ab)] = 0.5*d[a][b] + 1/(2*(n-2)) * (sum(d[a][k] for k in d.columns) - sum(d[b][k] for k in d.columns))
        delta[(b, ab)] = d[a][b] - delta[(a, ab)]

        print('\033[32;1mDelta\033[0m')
        print(delta)

        #4 Add row and column to d for new node
        d[ab] = [0]*n

        matrix = d.values.tolist()
        matrix.append([0]*(n+1))
        d = pd.DataFrame(matrix, columns=d.columns, index=d.columns)

        print('\033[34;1md\033[0m')
        print(d)

        #5 Define distances to other nodes from new one
        for k in d.columns:
            if k != ab:
                d[k][ab] = d[ab][k] = 0.5 * (d[a][k] + d[b][k] - d[a][b])

        print('\033[34;1md\033[0m')
        print(d)

        #6 Remove columns and rows for already parented nodes
        d = d.drop([a, b])
        d = d.drop([a, b], 1)

        Q = pd.DataFrame(columns=d.columns, index=d.columns)

        print('\033[33;1mQ\033[0m')
        print(Q)

        print('\033[34;1md\033[0m')
        print(d)

        n = d.shape[0]

        print('\033[35mn\033[0m: ', n)

    print(delta)

    distance_to_tree(delta)

if __name__ == "__main__":
    main(sys.argv[1:])