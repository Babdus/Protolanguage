import sys
import pandas as pd

def main(argv):
    matrix_path = argv[0]
    df = pd.io.parsers.read_csv(matrix_path,index_col=0, keep_default_na=False)
    dictionary = {}
    for col in df.columns:
        for row in df.index:
            cell = str(df[col][row])
            if len(cell) > 0:
                dictionary[(col, row)] = float(cell)
    print(dictionary)
    if len(argv) > 1:
        with open(argv[1], 'w') as f:
            f.write(str(dictionary))

if __name__ == "__main__":
    main(sys.argv[1:])
