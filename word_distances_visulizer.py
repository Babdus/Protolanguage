import sys
from collections import Counter

def main(argv):
    with open(argv[0]) as inp:
        array = [int(line.strip()) for line in inp.readlines()]
    occurences = Counter(array)

    for x in range(0, max(array)+1):
        bar = ''
        for l in range(occurences[x]):
            bar += '▓'
        x = " " + str(x) if x < 10 else str(x)
        print(f"\033[33;1m{x} \033[30m|" + bar + "\033[0m")

if __name__ == "__main__":
    main(sys.argv[1:])
