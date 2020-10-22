import sys
from time import time
import pandas as pd
import numpy as np
from multiprocessing import Pool, current_process, cpu_count
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom
from IPA.IPACharComparison import save_cache, read_cache
from colors import *

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

def calculate_distance_raw(count, should_skip, lang_1, lang_2, wordtups, comp, n_langs):
    process_id = current_process()._identity[0]
    print(blue(f'{"Calculating language distances":<31}', bold=True),
            (process_id-1)*'\t\t',
            green(f'{count*100/n_langs**2:4.1f}%', bold=True),
            f'{lang_1: <3}', f'{lang_2: <3}', black('|', bold=True),
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
    pool = Pool(cpu_count())
    args = [ (i*matrix.shape[1]+j, i <= j, lang_1, lang_2, [ (word_1, word_2) for word_1, word_2 in matrix[:,(i, j)] ], comp, matrix.shape[1]) for i, lang_1 in enumerate(table.columns) for j, lang_2 in enumerate(table.columns) ]
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
            print(f'{col1: <4}', f'{col2: <4}',
                    green(f'{(100*counter)//(((n_langs**2)-n_langs)//2)}%', bold=True),
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

    read_cache(argv[3] + '/cache.pickle')

    with open(argv[1], 'w') as out:
        compare_parallel(out, langs, df)

    # save_cache(argv[3] + '/cache.pickle')

    end = time()
    # print(f'\033[32;1m100%\033[0m', ((end-start)*1000//1)/1000, 'seconds')


if __name__ == "__main__":
    compare(sys.argv[1:])
