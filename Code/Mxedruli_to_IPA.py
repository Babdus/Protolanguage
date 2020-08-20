import sys
import pandas as pd

d = {
    'ა': 'ä',
    'ბ': 'b',
    'გ': 'g',
    'დ': 'd',
    'ე': 'ɛ',
    'ვ': 'v',
    'ზ': 'z',
    'თ': 'tʰ',
    'ი': 'i',
    'კ': 'kʼ',
    'ლ': 'l',
    'მ': 'm',
    'ნ': 'n',
    'ო': 'ɔ',
    'პ': 'pʼ',
    'ჟ': 'ʒ',
    'რ': 'r',
    'ს': 's',
    'ტ': 'tʼ',
    'უ': 'u',
    'ფ': 'pʰ',
    'ქ': 'kʰ',
    'ღ': 'ʁ',
    'ყ': 'qʼ',
    'შ': 'ʃ',
    'ჩ': 'tʃ',
    'ც': 'ts',
    'ძ': 'dz',
    'წ': 'tsʼ',
    'ჭ': 'tʃʼ',
    'ხ': 'χ',
    'ჯ': 'dʒ',
    'ჰ': 'h',
    'ჲ': 'j',
    'ჴ': 'qʰ',
    'ჳ': 'w',
    'ჷ': 'ə',
    'ჸ': 'ʔ',
    'ჺ': 'æ'
}

def replace(s):
    print(s)
    res = ''
    if s == str(s):
        for ch in s:
            res += d[ch] if ch in d else ch
    return res

df = pd.read_csv(sys.argv[1])

df = df.applymap(lambda s: replace(s))

df.to_csv(sys.argv[1][:-4]+'_new.csv')
