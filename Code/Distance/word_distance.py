import sys
from ..IPA import IPAString

def main(argv):
    ipastr = IPAString('bear')
    print(str(ipastr))

if __name__ == "__main__":
    main(sys.argv)
