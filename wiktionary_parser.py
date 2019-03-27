import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

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
                transcription = transcription_tag.text.strip('][/')
                if transcription[0] != '-':
                    transcriptions.append(transcription)

    print(f'\033[33;1m{anchor}\033[0m: {word} \033[34m{transcriptions}\033[0m')
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
    return translations_tables[0]


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
    html = requests.get(url).content
    return BeautifulSoup(html, 'lxml')


def construct_dictionary(words, langs, main_lang):
    data = {}
    used_langs = set()

    for word in words:
        soup = get_soup(f'https://{main_lang}.wiktionary.org/wiki/{word}')

        dictionary = {}
        transcriptions = get_transcriptions(word, soup, 'English')
        if len(transcriptions) == 0:
            print(f'\033[31mNo transcription found for {word}\033[0m')
            continue
        dictionary[main_lang] = transcriptions

        translations_tables = soup.findAll('div', id=lambda x: x and x.startswith('Translations-'))
        if len(translations_tables) < 1:
            print(f'\033[31mNo translations found for {word}\033[0m')
            continue

        append_to_data(data, main_lang, transcriptions)
        used_langs.add(main_lang)

        translations_table = get_relevant_translations_table(translations_tables)

        for lang in langs:
            transcriptions = find_translation_with_transcriptions(word, lang, main_lang, translations_table)
            append_to_data(data, lang, transcriptions)
            used_langs.add(lang)

    return pd.DataFrame(data, columns=list(used_langs))


def main(argv):
    start_time = time.time()
    main_lang = 'en'

    words = get_words(argv[0])
    langs = get_languages(argv[1])
    if words is None or langs is None:
        return
    dictionary = construct_dictionary(words, langs, main_lang)
    dictionary.to_csv(argv[2])

    end_time = time.time()
    print(f'Took {end_time - start_time} seconds')


if __name__ == "__main__":
    main(sys.argv[1:])
