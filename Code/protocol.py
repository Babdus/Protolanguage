# argv[0]: word list csv
# argv[1]: lang list csv
# argv[2]: name
# argv[3]: from web?
# argv[4]: from step #

import sys
import os
from time import time
from datetime import datetime
from data_collection.wiktionary_parser import parser as wiki_parser
from data_collection.convert_catalogue_to_dicts import convert as convert_catalogue
from language_comparison import compare as compare_langs
from generate_tree_np import generate as generate_tree
from generate_protolanguages import generate as reconstruct
from colors import *


def step(n, text, function, args_list, then, from_step):
    if from_step <= n:
        print(blue(text, bold=True), end='\r')
        function(args_list)
        now = time()
        print(blue(text, bold=True), yellow('DONE', bold=True), black(f'{now-then:.3f} seconds', bold=True), ' '*64)
        return now
    return then


def main(argv):
    words_csv = argv[0]
    langs_csv = argv[1]
    name      = argv[2]
    from_web  = argv[3]
    from_step = int(argv[4]) if len(argv) > 4 else 0

    dir_path      = ''#'/home/babdus/Development/Python Projects/Protolanguage/'
    data_dir_path = dir_path + 'Data/'

    start = time()

    # step 0
    if bool(int(from_web)):
        word_languge_dicts_path = data_dir_path + '/words_and_languages/' + name + '_dicts.csv'
        then = step(0, 'Parsing wiktionary', wiki_parser, [words_csv, langs_csv, word_languge_dicts_path, 20], start, from_step)
    else:
        word_languge_dicts_path = data_dir_path + '/words_and_languages/' + name + '_dicts.csv'
        catalogue_path = data_dir_path + '/words_and_languages/Catalogue.csv'
        then = step(0, 'Converting catalogue', convert_catalogue, [words_csv, langs_csv, catalogue_path, word_languge_dicts_path], start, from_step)

    # step 1
    language_distance_matrix_path = data_dir_path + '/words_and_languages/' + name + '_distances.csv'
    then = step(1, 'Calculating language distances', compare_langs, [word_languge_dicts_path, language_distance_matrix_path, langs_csv, data_dir_path], then, from_step)

    # step 2
    if not os.path.exists(data_dir_path + '/trees/' + name):
        os.makedirs(data_dir_path + '/trees/' + name)
    language_tree_path = data_dir_path + '/trees/' + name + '/tree.json'
    then = step(2, 'Generating language tree', generate_tree, [language_distance_matrix_path, language_tree_path], then, from_step)

    # step 3
    protolanguage_tree_path = data_dir_path + '/trees/' + name + '/tree_with_languages.json'
    protolanguage_dir_path  = data_dir_path + '/trees/' + name + '/protolanguages'
    then = step(3, 'Reconstructing protolanguages', reconstruct, [language_tree_path, word_languge_dicts_path, protolanguage_tree_path, protolanguage_dir_path], then, from_step)

    end = time()
    print(red(f'total {end-start:.3f} seconds', bold=True))

if __name__ == "__main__":
    main(sys.argv[1:])
