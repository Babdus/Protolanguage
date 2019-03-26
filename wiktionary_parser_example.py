import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

def main(argv):
    start_time = time.time()
    main_lang = argv[0]
    word = argv[1]

    data = {}
    used_langs = set()

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

    words = []
    if word == '--words':
        with open('word_list') as fp:
            for line in fp:
                words.append(line.split()[0])
    else:
        words = [word]

    for word in words:
        url = f'https://{main_lang}.wiktionary.org/wiki/{word}'

        html = requests.get(url).content
        soup = BeautifulSoup(html, 'lxml')

        dictionary = {}

        ### FOR MAIN LANG
        heading_span = soup.find('span', id='English')
        if heading_span is None:
            return
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

        dictionary[word] = transcriptions
        print(f'\033[33;1mEnglish\033[0m: {word} {transcriptions}')

        ###

        translations_tables = soup.findAll('div', id=lambda x: x and x.startswith('Translations-'))
        if len(translations_tables) < 1:
            print('\033[31mNo translations found\033[0m')
            continue

        # print(f'\033[32mdata before:\033[0m: {data}')
        if main_lang in data:
            # print(f'\033[32mdata main_lang:\033[0m: {data[main_lang]}')
            # print(f'\033[32mtranscriptions[0]:\033[0m: {transcriptions[0]}')
            # print(f'\033[32mlist:\033[0m: {list}')
            data[main_lang].append(transcriptions[0])
            # print(f'\033[32mdata after:\033[0m: {data}')
        else:
            data[main_lang] = [transcriptions[0]]

        used_langs.add(main_lang)

        translations_table = translations_tables[0]

        for lang in langs:
            print(lang)
            translation_tag = translations_table.find('span', lang=lang)
            if translation_tag is None:
                if lang in data:
                    data[lang].append(None)
                else:
                    data[lang] = [None]
                continue
            a = translation_tag.find('a')
            if a is None:
                if lang in data:
                    data[lang].append(None)
                else:
                    data[lang] = [None]
                continue
            href = a.get('href')
            if href is None:
                if lang in data:
                    data[lang].append(None)
                else:
                    data[lang] = [None]
                continue
            translation = translation_tag.text

            url_2 = f'https://{main_lang}.wiktionary.org{href}'
            html_2 = requests.get(url_2).content
            soup_2 = BeautifulSoup(html_2, 'lxml')
            href_list = href.split('#')
            if len(href_list) < 2:
                if lang in data:
                    data[lang].append(None)
                else:
                    data[lang] = [None]
                continue
            anchor = href_list[1]
            heading_span = soup_2.find('span', id=anchor)
            if heading_span is None:
                if lang in data:
                    data[lang].append(None)
                else:
                    data[lang] = [None]
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

            if len(transcriptions) > 0:
                transcription = transcriptions[0]
            else:
                transcription = None
            if lang in data:
                data[lang].append(transcription)
            else:
                data[lang] = [transcription]
            used_langs.add(lang)

            # print(f'\033[32;1mdata:\033[0m: {data}')

    df = pd.DataFrame(data,columns=list(used_langs))
    df.to_csv('DATA_BASE_2')
    end_time = time.time()
    print(f'Took {end_time - start_time} seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
