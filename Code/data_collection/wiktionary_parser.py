import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy
import threading
from pdb import set_trace as bp
from multiprocessing import Pool

global_lock = threading.Lock()

def get_words(arg):
    if arg[-4:] == '.csv':
        return pd.read_csv(arg).word
    else:
        return arg.split(' ')

def get_languages(arg):
    if arg[-4:] == '.csv':
        return pd.read_csv(arg).code
    else:
        return arg.split(' ')

def get_transcriptions(word, soup, anchor):
    heading_span = soup.find('span', id=anchor)
    if heading_span is None:
        return []
    heading = heading_span.parent

    transcriptions = []
    for next_heading in heading.next_siblings:
        if next_heading.name == 'h2':
            break
        if type(next_heading).__name__ == 'Tag':
            transcription_tags = next_heading.findAll('span', {"class": "IPA"})
            for transcription_tag in transcription_tags:
                transcription = transcription_tag.text.strip('][/').split(',')[0]
                if len(transcription) > 0 and transcription[0] != '-':
                    transcriptions.append(transcription)

    print(f'\033[33;1m{anchor}\033[0m: {word} \033[34m{transcriptions}\033[0m', end='\r')
    return transcriptions

def get_relevant_transcription(transcriptions):
    if transcriptions and len(transcriptions) > 0:
        return transcriptions[0]
    return None

def append_to_data(data, lang, transcriptions):
    transcription = get_relevant_transcription(transcriptions)
    if lang in data:
        data[lang].append(transcription)
    else:
        data[lang] = [transcription]

def get_relevant_translations_table(translations_tables):
    argmax = numpy.argmax([len(table.findChildren()) for table in translations_tables])
    return translations_tables[argmax]

def find_translation_with_transcriptions(word, lang, main_lang, translations_table):
    translation_tag = translations_table.find('span', lang=lang)
    if translation_tag is None:
        return None

    a = translation_tag.find('a')
    if a is None:
        return None

    href = a.get('href')
    if href is None:
        return None

    href_list = href.split('#')
    if len(href_list) < 2:
        return None

    translation = translation_tag.text
    soup = get_soup(f'https://{main_lang}.wiktionary.org{href}')
    anchor = href_list[1]
    return get_transcriptions(translation, soup, anchor)

def get_soup(url):
    try:
        html = requests.get(url).content
    except requests.exceptions.ConnectionError as e:
        print(f'\033[31m{e}\033[0m')
        time.sleep(5)
        html = requests.get(url).content
    if html is None:
        return None
    return BeautifulSoup(html, 'lxml')

def get_translation_tables(soup, word, main_lang):
    embedded_translations = soup.findAll('div', id=lambda x: x and x.startswith('Translations-'))
    soup_2 = get_soup(f'https://{main_lang}.wiktionary.org/wiki/{word}/translations')
    remote_translations = soup_2.findAll('div', id=lambda x: x and x.startswith('Translations-'))
    return embedded_translations + remote_translations

def construct_row(word, langs, main_lang):
    soup = get_soup(f'https://{main_lang}.wiktionary.org/wiki/{word}')

    dictionary = {}
    transcriptions = get_transcriptions(word, soup, 'English')
    if len(transcriptions) == 0:
        print(f'\033[31mNo transcription found for {word}\033[0m')
        return

    translations_tables = get_translation_tables(soup, word, main_lang)
    if len(translations_tables) < 1:
        print(f'\033[31mNo translations found for {word}\033[0m')
        return

    dictionary[main_lang] = get_relevant_transcription(transcriptions)

    translations_table = get_relevant_translations_table(translations_tables)

    for lang in langs:
        transcriptions = find_translation_with_transcriptions(word, lang, main_lang, translations_table)
        dictionary[lang] = get_relevant_transcription(transcriptions)

    with open(f'Data/words_and_languages/temp/{word}.csv', 'w') as out:
        langs.sort()
        out.write(','.join(['word'] + langs) + '\n')
        out.write(','.join([word] + [dictionary[lang] if dictionary[lang] is not None else '' for lang in langs]) + '\n')
    return { 'word': word, 'dictionary': dictionary }

def construct_dictionary(words, langs, main_lang, processes):
    pool = Pool(processes)
    args = [(word, langs, main_lang) for word in words]
    dictionaries = pool.starmap(construct_row, args)

    return dictionaries

def write_in_file(dictionaries, output_path):
    lang_set = set()
    for row in dictionaries:
        lang_set = lang_set.union(set(row['dictionary'].keys()))

    lang_list = list(lang_set)
    lang_list.sort()
    with open(output_path, 'w') as out:
        out.write(','.join(['word'] + lang_list) + '\n')
        for row in dictionaries:
            out.write(','.join([row['word']] + [row['dictionary'][lang] if row['dictionary'][lang] is not None else '' for lang in lang_list]) + '\n')

def parser(argv):
    start_time = time.time()
    main_lang = 'en'

    words = get_words(argv[0])
    langs = get_languages(argv[1])
    langs = [str(lang) for lang in langs]
    if words is None or langs is None:
        return
    dictionaries = construct_dictionary(words, langs, main_lang, int(argv[3]))
    write_in_file(dictionaries, argv[2])

    end_time = time.time()
    print(f'Took {end_time - start_time} seconds')

if __name__ == "__main__":
    parser(sys.argv[1:])
