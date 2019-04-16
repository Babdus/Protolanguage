import time
import requests
from multiprocessing import Pool

def construct_row(word):
    print(word)
    try:
        html = requests.get(f'https://en.wiktionary.org/wiki/{word}').content
    except requests.exceptions.ConnectionError as e:
        print(f'{i}: \033[31m{e}\033[0m')
        time.sleep(5)
    return word

for i in range(100):
    print(i)
    with open('Data/words_and_languages/swadesh_list.csv') as f:
        words = [line.strip() for line in f]
        print(words)
        pool = Pool(20)
        dictionaries = pool.map(construct_row, words)
