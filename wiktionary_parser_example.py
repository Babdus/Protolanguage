import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

def main(argv):
    start_time = time.time()
    main_lang = argv[0]
    word = argv[1]
    url = f'https://{main_lang}.wiktionary.org/wiki/{word}'

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    translations_tables = soup.findAll('div', id=lambda x: x and x.startswith('Translations-'))
    if len(translations_tables) < 1:
        print('\033[31mNo translations found\033[0m')
        return

    translations_table = translations_tables[0]
    dictionary = {}

    if len(argv) > 2:
        if argv[2] == '--full':
            df = pd.read_csv('languages_full_list.csv')
            langs = df.code
        else:
            langs = argv[2:]
    else:
        langs = []
        with open('language_list') as fp:
            for line in fp:
                langs.append(line.split()[0])

    for lang in langs:

        translation_tag = translations_table.find('span', lang=lang)
        if translation_tag is None:
            continue
        href = translation_tag.find('a').get('href')
        if href is None:
            continue
        translation = translation_tag.text

        url_2 = f'https://{main_lang}.wiktionary.org{href}'
        html_2 = requests.get(url_2).content
        soup_2 = BeautifulSoup(html_2, 'lxml')
        href_list = href.split('#')
        if len(href_list) < 2:
            continue
        anchor = href_list[1]
        heading_span = soup_2.find('span', id=anchor)
        if heading_span is None:
            continue
        heading = heading_span.parent

        transcriptions = []

        for next_heading in heading.next_siblings:
            if next_heading.name == 'h2':
                break
            if type(next_heading).__name__ == 'Tag':
                transcription_tags = next_heading.findAll('span', {"class": "IPA"})
                for transcription_tag in transcription_tags:
                    transcription = transcription_tag.text
                    transcription = transcription.strip('][/')
                    if transcription[0] != '-':
                        transcriptions.append(transcription)

        dictionary[translation] = transcriptions
        print(f'\033[33;1m{anchor}\033[0m: {translation} {transcriptions}')


if __name__ == "__main__":
    main(sys.argv[1:])
