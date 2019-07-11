# argv[0]: word list csv
# argv[1]: lang list csv
# argv[2]: name

import sys
from time import time
from datetime import datetime
from data_collection.wiktionary_parser import parser as wiki_parser
from language_comparison import compare as compare_langs
from generate_tree import generate as generate_tree
from generate_protolanguages import generate as reconstruct

def main(argv):
    words_csv = argv[0]
    langs_csv = argv[1]
    name      = argv[2]

    dir_path      = '/home/babdus/Development/Python Projects/Protolanguage/'
    data_dir_path = dir_path + '/Data/'

    start = time()

    print('Parsing wiktionary')
    word_languge_dicts_path = data_dir_path + '/words_and_languages/' + name + '_dicts.csv'
    wiki_parser([words_csv, langs_csv, word_languge_dicts_path, 20])

    print('Calculating language distances')
    language_distance_matrix_path = data_dir_path + '/words_and_languages/' + name + '_distances.csv'
    compare_langs([word_languge_dicts_path, language_distance_matrix_path, langs_csv])

    print('Generating language tree')
    language_tree_path = data_dir_path + '/trees/' + name + '/tree.json'
    generate_tree([language_distance_matrix_path, language_tree_path])

    print('Reconstructing protolanguages')
    protolanguage_tree_path = data_dir_path + '/trees/' + name + '/tree_with_languages.json'
    protolanguage_dir_path  = data_dir_path + '/trees/' + name + '/protolanguages'
    reconstruct([language_tree_path, word_languge_dicts_path, protolanguage_tree_path, protolanguage_dir_path])

    end = time()

    print('total', ((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
