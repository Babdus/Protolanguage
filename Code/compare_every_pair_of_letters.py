import sys
from time import time
from IPA.IPAData import letters
from IPA.IPAChar import IPAChar
from IPA.IPACharComparison import IPACharComparison

def main():
    # start = time()
    comparer = IPACharComparison()
    comparer.compare(IPAChar('p'), IPAChar('r'))
    print(str(comparer))
    print(comparer.get_distance())
    print(comparer.get_way())
    # for l1 in letters:
    #     for l2 in letters:
    #         comparer.compare(IPAChar(l1, printing=False), IPAChar(l2, printing=False))
    #         # print(str(comparer))
    # end = time()
    # print(end-start)

if __name__ == "__main__":
    main()
