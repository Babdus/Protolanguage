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
from generate_tree import generate as generate_tree
from generate_protolanguages import generate as reconstruct

def main(argv):
    words_csv = argv[0]
    langs_csv = argv[1]
    name      = argv[2]
    from_web  = argv[3]
    if len(argv) > 4:
        from_step = int(argv[4])
    else:
        from_step = 0

    dir_path      = '/home/babdus/Development/Python Projects/Protolanguage/'
    data_dir_path = dir_path + '/Data/'

    start = time()

    if bool(int(from_web)):
        if from_step < 1:
            print('Parsing wiktionary')
        word_languge_dicts_path = data_dir_path + '/words_and_languages/' + name + '_dicts.csv'
        if from_step < 1:
            wiki_parser([words_csv, langs_csv, word_languge_dicts_path, 20])

    else:
        if from_step < 1:
            print('Converting catalogue')
        word_languge_dicts_path = data_dir_path + '/words_and_languages/' + name + '_dicts.csv'
        catalogue_path = data_dir_path + '/words_and_languages/Catalogue.csv'
        if from_step < 1:
            convert_catalogue([words_csv, langs_csv, catalogue_path, word_languge_dicts_path])

    if from_step < 2:
        print('Calculating language distances', end='\r')
    language_distance_matrix_path = data_dir_path + '/words_and_languages/' + name + '_distances.csv'
    if from_step < 2:
        compare_langs([word_languge_dicts_path, language_distance_matrix_path, langs_csv])

    if from_step < 3:
        print('Generating language tree')
    if not os.path.exists(data_dir_path + '/trees/' + name):
        os.makedirs(data_dir_path + '/trees/' + name)
    language_tree_path = data_dir_path + '/trees/' + name + '/tree.json'
    if from_step < 3:
        generate_tree([language_distance_matrix_path, language_tree_path])

    if from_step < 4:
        print('Reconstructing protolanguages')
    protolanguage_tree_path = data_dir_path + '/trees/' + name + '/tree_with_languages.json'
    protolanguage_dir_path  = data_dir_path + '/trees/' + name + '/protolanguages'
    if from_step < 4:
        reconstruct([language_tree_path, word_languge_dicts_path, protolanguage_tree_path, protolanguage_dir_path])

    end = time()

    print('total', ((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
