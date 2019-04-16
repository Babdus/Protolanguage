import sys
import time
import pandas as pd

def main(argv):
    df = pd.read_csv(argv[0], index_col=0)

    rows = df.index.tolist()
    vertices = {}

    for row in rows:
        vertices[row] = set()

    for col in df:
        s = set()
        for row in rows:
            cell = df[col][row]
            if len(cell) > 0:
                vertices[row].add(col)
                s.add(row)
        vertices[col] = s
    print(vertices)

if __name__ == "__main__":
    main(sys.argv[1:])
