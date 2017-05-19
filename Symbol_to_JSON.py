import sys
import json

def main():
    with open('Features.txt') as f:
        feature_names = [feature.strip() for feature in f]
    symbol_features = {}
    with open('Symbol_Feature_Map.txt') as f:
        for line in f:
            line = line.split()
            features = dict(zip(feature_names, line[1:]))
            symbol_features[line[0]] = features
    symbols_json = json.dumps(symbol_features)
    print symbols_json

if __name__ == "__main__":
    main()
