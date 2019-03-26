import urllib.request
import sys
from lxml import html
import re
import time
from bs4 import BeautifulSoup
import requests

def main(argv):
    start_time = time.time()
    main_lang = argv[0]
    word = argv[1]
    translation_lang = argv[2]
    url = f'https://{main_lang}.wiktionary.org/wiki/{word}'

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    translations_table = soup.findAll('div', id=lambda x: x and x.startswith('Translations-'))[0]

    dictionary = {}

    langs = argv[2:]

    for lang in langs:

        translation_tag = translations_table.find('span', lang=lang)
        href = translation_tag.find('a').get('href')
        translation = translation_tag.text

        url_2 = f'https://{main_lang}.wiktionary.org{href}'
        html_2 = requests.get(url_2).content
        soup_2 = BeautifulSoup(html_2, 'lxml')
        anchor = href.split('#')[1]
        heading = soup_2.find('span', id=anchor).parent

        transcriptions = []

        for next_heading in heading.next_siblings:
            if next_heading.name == 'h2':
                break
            if type(next_heading).__name__ == 'NavigableString':
                continue
            transcription_tags = next_heading.findAll('span', {"class": "IPA"})
            for transcription_tag in transcription_tags:
                transcription = transcription_tag.text
                transcription = transcription.strip('][/')
                if transcription[0] != '-':
                    transcriptions.append(transcription)

        dictionary[translation] = transcriptions
        print(translation, transcriptions)

    print(dictionary)


if __name__ == "__main__":
    main(sys.argv[1:])
