import sys
from data_collection.wiktionary_parser import parser as wiki_parser

def main(argv):
    words_csv = argv[0]
    langs_csv = argv[1]
    name      = argv[2]

    dir_path = '/home/babdus/Development/Python Projects/Protolanguage/'
    data_dir_path = dir_path + '/Data/'
    print('Parsing wiktionary')
    word_languge_matrix_path = data_dir_path + '/words_and_languages/' + name + '_matrix.csv'
    wiki_parser([words_csv, langs_csv, word_languge_matrix_path, 20])

    

if __name__ == "__main__":
    main(sys.argv[1:])
