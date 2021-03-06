import sys
import pandas as pd
from collections import Counter
from language_comparison import calculate_distance

def main(argv):
    df = pd.io.parsers.read_csv(argv[0],index_col=0).fillna('')
    distances, output = calculate_distance(df, argv[1], argv[2], f'{argv[1]}-{argv[2]}.out')

    with open(f'../Test/{argv[1]}-{argv[2]}.out', 'w') as out:
        for o in output:
            out.write(f'{o[1]} - {o[2]}: {o[0]}\n')

    array = [int(elem) for elem in distances]
    # with open(argv[0]) as inp:
    #     array = [int(line.split()[0].strip()) for line in inp.readlines()]
    occurences = Counter(array)
    max_value = occurences.most_common()[0][1]
    print(sum(array)/len(array))

    axis = ''
    axis_val = ''
    for x in range(max_value):
        if x%5 == 0:
            axis += '┴'
            if x > 100:
                axis_val = axis_val[:-2] + str(x)
            elif x >= 10:
                axis_val = axis_val[:-1] + str(x)
            else:
                axis_val += str(x)
        else:
            axis += '─'
            axis_val += ' '

    print('\n\033[33;1mDistances\033[0m\033[35m│ Occurences ⤳')
    print('       \033[33;1m↯\033[0m\033[35m │' + axis_val)
    print('         ├' + axis)

    for x in range(0, max(array)+1):
        bar = ''
        for l in range(occurences[x]):
            bar += '▒'
        x = " " + str(x) if x < 10 else str(x)
        print(f"      \033[33;1m{x}\033[0m\033[35m╶┤\033[30;1m" + bar + "\033[0m")

if __name__ == "__main__":
    main(sys.argv[1:])
