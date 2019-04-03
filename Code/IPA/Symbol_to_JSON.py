import sys
import json

def main():
    with open('Features.txt') as infile:
        feature_names = [feature.strip() for feature in infile]
    symbol_features = {}
    with open('Symbol_Feature_Map.txt') as infile:
        for line in infile:
            line = line.split()
            if line[0] == 'end':
                break
            bool_features = [bool(int(digit)) for digit in line[1:]]
            features = dict(zip(feature_names, bool_features))
            symbol_features[line[0]] = features
    with open('Symbols.json', 'w') as outfile:
        json.dump(symbol_features, outfile)
    for symbol in symbol_features:
        print(symbol)
        for feature in symbol_features[symbol]:
            print('\t', feature, '-', int(symbol_features[symbol][feature]))

if __name__ == "__main__":
    main()
