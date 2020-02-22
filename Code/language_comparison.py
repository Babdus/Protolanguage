import sys
from time import time
import pandas as pd
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
        return pd.read_csv(arg).code
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

def compare(argv):
    start = time()
    df = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')

    langs = ie_test_langs

    if len(argv) > 2:
        langs = get_languages(argv[2])

    with open(argv[1], 'w') as out:
        out.write(','+','.join(langs)+'\n')
        for i, col1 in enumerate(langs):
            out.write(col1)
            for j, col2 in enumerate(langs):
                if i <= j:
                    out.write(',')
                    continue
                print(col1, col2, end='\r')
                distances, output = calculate_distance(df, col1, col2, None)
                if len(distances) == 0:
                    out.write(',N/A')
                else:
                    out.write(f',{sum(distances)/len(distances)*100000//1/100000}')
            out.write('\n')

    end = time()
    print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    compare(sys.argv[1:])
