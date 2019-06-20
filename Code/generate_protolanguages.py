# argv[0]: tree.json (without languages)
# argv[1]: words × languages.csv
# argv[2]: output tree.json (with languages)

import sys
from time import time
import random
import json
import pandas as pd
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom

def convert_istr_to_printable(tree):
    if 'children' in tree:
        convert_istr_to_printable(tree['children'][0])
        convert_istr_to_printable(tree['children'][1])
    for word in tree['lang']:
        tree['lang'][word] = str(tree['lang'][word])

def load_modern_language(lang, df):
    dictionary = df[lang].to_dict()
    for word in dictionary:
        dictionary[word] = Istr(dictionary[word])
    return dictionary

def reconstruct_language(child1, child2):
    lang = {}
    comp = Istcom()
    lang1 = child1['lang']
    lang2 = child2['lang']
    dist1 = child1['distance']
    dist2 = child2['distance']

    color_code = random.choice([30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97])
    print(f'\033[{str(color_code)}m')
    print(child1['name'], child2['name'])
    print('\033[0m')

    for word in lang1:
        if len(lang2[word]) < 1:
            lang[word] = lang1[word]
        elif len(lang1[word]) < 1:
            lang[word] = lang2[word]
        else:
            comp.compare(lang1[word], lang2[word], asymmetric=True, relat_dist_to_word1=(dist1/(dist1+dist2)))
            lang[word] = comp.parent
    return lang

def reconstruct_languages(tree, df):
    child1 = tree['children'][0]
    child2 = tree['children'][1]

    if 'children' in child1:
        reconstruct_languages(child1, df)
    else:
        child1['lang'] = load_modern_language(tree['name'][:2], df)
    if 'children' in child2:
        reconstruct_languages(child2, df)
    else:
        child2['lang'] = load_modern_language(tree['name'][-2:], df)

    tree['lang'] = reconstruct_language(child1, child2)

def main(argv):
    df = pd.io.parsers.read_csv(argv[1],index_col=0).fillna('')
    start = time()

    with open(argv[0]) as f:
        forest = json.load(f)

    tree = forest[0]
    reconstruct_languages(tree, df)

    convert_istr_to_printable(tree)
    end = time()

    for word in tree['lang']:
        print(word)
        print(tree['lang'][word])
        print('\n')

    t_json = json.dumps([tree], indent=2)
    with open(argv[2], 'w') as out:
        out.write(t_json)

    print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
