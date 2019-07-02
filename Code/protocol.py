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
    stamp = datetime.fromtimestamp(time()).strftime('%Y%m%d%H%M%S')
    word_languge_dicts_path = data_dir_path + '/words_and_languages/' + name + '_dicts_' + stamp + '.csv'
    wiki_parser([words_csv, langs_csv, word_languge_dicts_path, 20])

    print('Calculating language distances')
    stamp = datetime.fromtimestamp(time()).strftime('%Y%m%d%H%M%S')
    language_distance_matrix_path = data_dir_path + '/words_and_languages/' + name + '_distances_' + stamp + '.csv'
    compare_langs([word_languge_dicts_path, language_distance_matrix_path, langs_csv])

    print('Generating language tree')
    stamp = datetime.fromtimestamp(time()).strftime('%Y%m%d%H%M%S')
    language_tree_path = data_dir_path + '/trees/' + name + '_tree_' + stamp + '.json'
    generate_tree([language_distance_matrix_path, language_tree_path])

    print('Reconstructing protolanguages')
    stamp = datetime.fromtimestamp(time()).strftime('%Y%m%d%H%M%S')
    protolanguage_tree_path = data_dir_path + '/trees/' + name + '_tree_with_languages_' + stamp + '.json'
    protolanguage_dir_path  = data_dir_path + '/trees/' + name + '_protolanguages_' + stamp
    reconstruct([language_tree_path, word_languge_dicts_path, protolanguage_tree_path, protolanguage_dir_path])

    end = time()

    print('total', ((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
