import sys
import pandas as pd

def get_words(arg):
    if arg[-4:] == '.csv':
        return pd.read_csv(arg, keep_default_na=False).word
    else:
        return arg.split(' ')

def get_languages(arg):
    if arg[-4:] == '.csv':
        return pd.read_csv(arg, keep_default_na=False).code
    else:
        return arg.split(' ')

def convert(argv):

    words = list(get_words(argv[0]))
    langs = list(get_languages(argv[1]))
    catalogue = str(argv[2])
    output = str(argv[3])

    df = pd.io.parsers.read_csv(catalogue, index_col='Code')
    df = df[df.index.notnull()]
    df.drop(['Family', 'Group', 'Language', 'Code2'], axis=1, inplace=True)
    df['Missing'] = df.apply(lambda x: x.isnull().sum(), axis='columns')
    df.drop(df[df['Missing'] > 206].index, axis=0, inplace=True) #TODO change 206 to any number below to limit dictionaries with missing words
    df.drop(['Missing'], axis=1, inplace=True)
    df = df.fillna('')
    df = df[set(df.columns) & set(words)]
    df = df.transpose()
    df.index.names = ['word']
    df = df[set(df.columns) & set(langs)]
    df.to_csv(output)

if __name__ == "__main__":
    convert(sys.argv[1:])
