import sys
from time import time
import pandas as pd
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom

def calculate_distance(df, lang_1, lang_2, output_file):
    lang_1_words = df[lang_1]
    lang_2_words = df[lang_2]

    distances = []
    output = []
    comp = Istcom()
    for i, word in enumerate(lang_1_words):
        if isinstance(word, str) and len(word) > 0 and isinstance(lang_2_words[i], str) and len(lang_2_words[i]) > 0:
            istr1 = Istr(word)
            istr2 = Istr(lang_2_words[i])
            comp.compare(istr1, istr2)
            distance = comp.distance / (len(istr1) + len(istr2)) * 5
            distances.append(distance)
            output.append((distance, word, lang_2_words[i]))
    output.sort()
    if output_file is not None:
        with open(output_file, 'w') as out:
            for o in output:
                out.write(f'{o[1]} {o[2]}: {o[0]}\n')
    return distances, output

def main(argv):
    start = time()
    df = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')

    # for col1 in df.columns:
    dists = []
    for col2 in df.columns:
        distances, output = calculate_distance(df, 'ka', col2, None)
        if len(distances) > 50:
            dists.append((sum(distances)/len(distances), 'ka', col2))

    dists.sort()
    for dist in dists:
        print(dist[1], dist[2], dist[0])

    end = time()
    print(((end-start)*1000//1)/1000, 'seconds')

if __name__ == "__main__":
    main(sys.argv[1:])
