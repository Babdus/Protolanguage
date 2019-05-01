import sys
import pandas as pd
from collections import Counter
from IPA import IPAChar
from IPA import IPAString

def main(argv):
    df = pd.io.parsers.read_csv(argv[0],index_col=0)
    for i, row in df.iterrows():
        for cell in row:
            cell = cell.strip()
            if len(cell) > 0:
                print(cell)
                string = IPAString(cell)
                print(str(string))
                print('\n')

if __name__ == "__main__":
    main(sys.argv[1:])
