# argv[0]: tree.json (without languages)
# argv[1]: words × languages.csv
# argv[2]: output tree.json (with languages)
# argv[3]: output directory for each protolanguage

import sys
import os
from time import time
import random
import json
import pandas as pd
import hashlib
from multiprocessing import Pool, cpu_count
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom
from colors import *

def convert_istr_to_printable(tree, languages_dict):
    if 'children' in tree:
        convert_istr_to_printable(tree['children'][0], languages_dict)
        convert_istr_to_printable(tree['children'][1], languages_dict)
    for word in tree['lang']:
        tree['lang'][word] = tree['lang'][word].to_ipa()
        languages_dict[tree['name']] = tree['lang']

def load_modern_language(lang, df):
    dictionary = df[lang].to_dict()
    for word in dictionary:
        dictionary[word] = Istr(dictionary[word])
    return dictionary

def reconstruct_word(word, lang1_word, lang2_word, dist1, dist2, comp):
    if len(lang2_word) < 1:
        return word, lang1_word
    elif len(lang1_word) < 1:
        return word, lang2_word
    else:
        comp.compare(lang1_word, lang2_word, asymmetric=True, relat_dist_to_word1=(dist1/(dist1+dist2)))
        return word, comp.parent

def reconstruct_language(child1, child2):
    # lang = {}
    comp = Istcom()
    lang1 = child1['lang']
    lang2 = child2['lang']
    dist1 = child1['distance']
    dist2 = child2['distance']

    print(blue('Reconstructing protolanguages', bold=True), random_color(f"{child1['name'][:16]:<3}"), random_color(f"{child2['name'][:16]:<3}"), ' '*32, end='\r')

    pool = Pool(cpu_count()-1)
    args = [(word, lang1[word], lang2[word], dist1, dist2, comp) for word in lang1]
    tuples = pool.starmap(reconstruct_word, args)

    lang = {key: value for key, value in tuples}

    # for word in lang1:
    #     if len(lang2[word]) < 1:
    #         lang[word] = lang1[word]
    #     elif len(lang1[word]) < 1:
    #         lang[word] = lang2[word]
    #     else:
    #         comp.compare(lang1[word], lang2[word], asymmetric=True, relat_dist_to_word1=(dist1/(dist1+dist2)))
    #         lang[word] = comp.parent
    #         # print(comp.parent.to_ipa())
    return lang

def reconstruct_languages(tree, df):
    child1 = tree['children'][0]
    child2 = tree['children'][1]

    if 'children' in child1:
        reconstruct_languages(child1, df)
    else:
        # child1['full_name'] = child1['name']
        # child1['name']      = tree['name'].split('.')[0]
        child1['lang']      = load_modern_language(child1['name'], df)
    if 'children' in child2:
        reconstruct_languages(child2, df)
    else:
        # child2['full_name'] = child2['name']
        # child2['name']      = tree['name'].split('.')[1]
        child2['lang']      = load_modern_language(child2['name'], df)

    tree['lang'] = reconstruct_language(child1, child2)

def generate(argv):
    df = pd.io.parsers.read_csv(argv[1],index_col=0).fillna('')
    start = time()

    with open(argv[0]) as f:
        forest = json.load(f)

    tree = forest[0]
    reconstruct_languages(tree, df)

    languages_dict = {}
    convert_istr_to_printable(tree, languages_dict)
    end = time()

    # for word in tree['lang']:
    #     print(word)
    #     print(tree['lang'][word])
    #     print('\n')

    t_json = json.dumps([tree], indent=2)
    with open(argv[2], 'w') as out:
        out.write(t_json)

    for lang in languages_dict:
        l_json = json.dumps(languages_dict[lang])
        if not os.path.exists(argv[3]):
            os.makedirs(argv[3])
        lang_path = hashlib.md5(lang.encode()).hexdigest()
        with open(argv[3] + '/' + lang_path + '.json', 'w') as out:
            out.write(l_json)

    # print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    generate(sys.argv[1:])
