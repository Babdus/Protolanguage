import sys
import pandas as pd
from collections import Counter
from IPA import IPAChar
from IPA import IPAString

def main(argv):
    df = pd.io.parsers.read_csv(argv[0],index_col=0)
    count = 0
    for i, row in df.iterrows():
        for j, cell in enumerate(row):
            cell = cell.strip()
            if len(cell) > 0:
                print(count)
                print(f'\033[34;1m{cell}\033[0m (\033[33;1m{df.columns[j].strip()}\033[0m)')
                string = IPAString(cell)
                print(str(string))
                print('\n')
            count += 1

if __name__ == "__main__":
    main(sys.argv[1:])
