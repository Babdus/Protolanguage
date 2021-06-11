import sys
from time import time
import pandas as pd
import numpy as np
from distance_dict_to_tree_dict import distance_to_tree

def generate(argv):
    d = pd.io.parsers.read_csv(argv[0],index_col=0).fillna(0)
    start = time()
    langs = list(d.columns)
    n = len(langs)
    delta = {}
    d = d.to_numpy()
    d = d + d.transpose()

    while n > 1:
        #1 Compute Q matrix
        Q = (d * (n-2)) - np.sum(d, axis=0).reshape(1, n) - np.sum(d, axis=1).reshape(n, 1)
        np.fill_diagonal(Q, 0)

        #2 Find pair with minimal value in Q
        i, j = np.unravel_index(Q.argmin(), Q.shape)

        #3 Create parent node for minimal found pair and assign edge lengths
        ij_name = langs[i]+'.'+langs[j]
        dist_i_ij = d[i, j]/2 + ( ( np.sum(d[i]) - np.sum(d[j]) )/(2*(n-2)) if n != 2 else 0 )

        delta[(langs[i], ij_name)] = dist_i_ij
        delta[(langs[j], ij_name)] = d[i, j] - dist_i_ij

        langs.append(ij_name)

        #4 Calculate distances to other nodes from new one
        dists_to_ij = (d[i] + d[j] - d[i, j])/2

        #5 Add row and column to d for new node
        d_new = np.zeros((n+1, n+1))
        d_new[:-1, :-1] = d
        d = d_new

        #6 Set new distances to the new node in d
        d[:-1, -1] = dists_to_ij
        d[-1, :-1] = dists_to_ij

        #6 Remove columns and rows for already parented nodes
        d = np.delete(d, (i, j), axis=0)
        d = np.delete(d, (i, j), axis=1)

        if i > j:
            del langs[i]
            del langs[j]
        else:
            del langs[j]
            del langs[i]

        n = len(langs)

    end = time()

    t_json = distance_to_tree(delta)
    with open(argv[1], 'w') as out:
        out.write(t_json)

    # print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    generate(sys.argv[1:])
