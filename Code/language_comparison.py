import sys
from time import time
import pandas as pd
import numpy as np
from multiprocessing import Pool
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom

test_langs = ['af', 'ar', 'as', 'az', 'ba', 'be', 'bg', 'bn', 'bo', 'br', 'ca',
              'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'fa', 'fi', 'fo', 'fr',
              'fy', 'ga', 'gd', 'gl', 'gv', 'he', 'hi', 'hu', 'hy', 'id', 'is',
              'it', 'ja', 'ka', 'km', 'ko', 'ku', 'lb', 'lo', 'lt', 'lv', 'mk',
              'mn', 'ms', 'mt', 'my', 'nl', 'nn', 'ny', 'oc', 'pl', 'ps', 'pt',
              'ro', 'ru', 'sa', 'se', 'sk', 'sl', 'sq', 'sv', 'te', 'tg', 'th',
              'tk', 'tl', 'tr', 'ug', 'uk', 'ur', 'vi', 'xh', 'yi', 'za', 'zu']

ie_test_langs = ['af', 'as', 'be', 'bg', 'bn', 'br', 'ca', 'cs',
                 'cy', 'da', 'de', 'el', 'en', 'es', 'fa', 'fo',
                 'fr', 'fy', 'ga', 'gd', 'gl', 'gv', 'hi', 'hy',
                 'is', 'it', 'ku', 'lb', 'lt', 'lv', 'mk', 'nl',
                 'nn', 'oc', 'pl', 'ps', 'pt', 'ro', 'ru', 'sa',
                 'sk', 'sl', 'sq', 'sv', 'tg', 'uk', 'ur', 'yi']


def get_languages(arg):
    if arg[-4:] == '.csv':
        return pd.read_csv(arg, keep_default_na=False).code
    else:
        return arg.split(' ')


def calculate_distance(df, lang_1, lang_2, output_file):
    lang_1_words = df[lang_1]
    lang_2_words = df[lang_2]

    output = []
    comp = Istcom()
    distances = []
    for i, word in enumerate(lang_1_words):
        if isinstance(word, str) and len(word) > 0 and isinstance(lang_2_words[i], str) and len(lang_2_words[i]) > 0:
            istr1 = Istr(word)
            istr2 = Istr(lang_2_words[i])
            comp.compare(istr1, istr2)
            distance = comp.distance / (len(istr1) + len(istr2)) * 5
            distances.append(distance)
            output.append((distance*1000//1/1000, word, lang_2_words[i]))
    return distances, output

def calculate_distance_raw(should_skip, lang_1, lang_2, wordtups, comp, n_langs):
    print('Calculating language distances',
            f'{lang_1: <4}', f'{lang_2: <4}',
            end='\r')
    if should_skip:
        return (lang_1, lang_2, None)
    distances = []
    for word_1, word_2 in wordtups:
        if isinstance(word_1, str) and len(word_1) > 0 and isinstance(word_2, str) and len(word_2) > 0:
            istr1 = Istr(word_1)
            istr2 = Istr(word_2)
            comp.compare(istr1, istr2)
            distance = comp.distance / (len(istr1) + len(istr2)) * 5
            distances.append(distance)
    return (lang_1, lang_2, np.mean(distances))

def compare_parallel(out, langs, df):
    table = df[sorted(langs)]
    table = table.loc[sorted(table.index)]
    matrix = np.array(table)
    comp = Istcom()
    pool = Pool(20)
    args = [ (i <= j, lang_1, lang_2, [ (word_1, word_2) for word_1, word_2 in matrix[:,(i, j)] ], comp, matrix.shape[1]) for i, lang_1 in enumerate(table.columns) for j, lang_2 in enumerate(table.columns) ]
    tuples = pool.starmap(calculate_distance_raw, args)
    tuples = np.array(sorted(tuples, key=lambda x: x[0]))
    tuples = tuples.reshape(matrix.shape[1], matrix.shape[1], -1)
    out.write(','+','.join(tuples[0,:,1]))
    out.write('\n')
    for block in tuples:
        out.write(block[0,0] + ',')
        out.write(','.join(['' if x is None else str(x) for x in block[:,2]]))
        out.write('\n')

def compare_loop(out, langs, df):
    n_langs = len(langs)
    counter = 0
    out.write(','+','.join(langs)+'\n')
    for i, col1 in enumerate(langs):
        out.write(col1)
        for j, col2 in enumerate(langs):
            if i <= j:
                out.write(',')
                continue
            counter += 1
            print('Calculating language distances',
                    f'{col1: <4}', f'{col2: <4}',
                    f'\033[32;1m{(100*counter)//(((n_langs**2)-n_langs)//2)}%\033[0m',
                    end='\r')
            distances, output = calculate_distance(df, col1, col2, None)
            if len(distances) == 0:
                out.write(',N/A')
            else:
                out.write(f',{sum(distances)/len(distances)*100000//1/100000}')
        out.write('\n')


def compare(argv):
    start = time()
    df = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')

    langs = list(set(ie_test_langs) & set(df.columns))

    if len(argv) > 2:
        langs = list(set(get_languages(argv[2])) & set(df.columns))

    with open(argv[1], 'w') as out:
        compare_parallel(out, langs, df)

    end = time()
    print('Calculating language distances', f'\033[32;1m100%\033[0m', ((end-start)*1000//1)/1000, 'seconds')


if __name__ == "__main__":
    compare(sys.argv[1:])
