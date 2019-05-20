import sys
import pandas as pd
from IPA.IPAString import IPAString as Istr
from IPA.IPAStringComparison import IPAStringComparison as Istcom

def calculate_distance(input_file, lang_1, lang_2, output_file):
    df = pd.io.parsers.read_csv(input_file,index_col=0).fillna('')
    lang_1_words = getattr(df, lang_1)
    lang_2_words = getattr(df, lang_2)

    distances = []
    output = []
    for i, word in enumerate(lang_1_words):
        if isinstance(word, str) and len(word) > 0 and isinstance(lang_2_words[i], str) and len(lang_2_words[i]) > 0:
            istr1 = Istr(word)
            istr2 = Istr(lang_2_words[i])
            comp = Istcom()
            comp.compare(istr1, istr2)
            distance = comp.distance / (len(istr1) + len(istr2)) * 5
            distances.append(distance)
            output.append((distance, word, lang_2_words[i]))
    output.sort()
    with open(output_file, 'w') as out:
        for o in output:
            out.write(f'{o[1]} {o[2]}: {o[0]}\n')
    return distances

def main(argv):
    calculate_distance(argv[0], argv[1], argv[2], argv[3])

if __name__ == "__main__":
    main(sys.argv[1:])
