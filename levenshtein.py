import sys
import numpy as np
import pandas as pd
import math

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    # print (matrix)
    return (matrix[size_x - 1, size_y - 1])

def main(argv):
    english_words = pd.read_csv(argv[0]).en
    german_words = pd.read_csv(argv[0]).de

    with open(argv[1], 'w') as out:
        for i, word in enumerate(english_words):
            print(word, german_words[i])
            if isinstance(german_words[i], str) and len(german_words[i]) > 0:
                distance = levenshtein(word, german_words[i])
                print(word, german_words[i], distance)
                out.write(str(int(distance)) + ' ' + word + '\n')


if __name__ == "__main__":
    main(sys.argv[1:])
