import sys
import json
import pandas as pd

d_dict = {('a', 'ac'): 7, ('c', 'ac'): 9, ('b', 'bd'): 8, ('d', 'bd'): 6,
          ('e', 'ace'): 3, ('ac', 'ace'): 6, ('ace', 'acebd'): 2, ('bd', 'acebd'): 4}

def get_language_codes():
    df = pd.read_csv('/home/babdus/Development/Python Projects/Protolanguage/Data/words_and_languages/language_list.csv', skipinitialspace=True)
    d = {row[1].code: row[1].language for row in df.iterrows()}
    return d

def create_tree(tree, root, ch_dict, language_codes):
    if root in ch_dict:
        for child, distance in ch_dict[root]:
            node = {'name': child, 'distance': distance, 'parent': root}
            if child in language_codes:
                node['full_name'] = language_codes[child]
            if 'children' in tree:
                tree['children'].append(node)
            else:
                tree['children'] = [node]
            create_tree(node, child, ch_dict, language_codes)

def distance_to_tree(d_dict):
    language_codes = get_language_codes()
    ch_dict = {}
    for d in d_dict:
        if d[1] in ch_dict:
            ch_dict[d[1]].append((d[0], d_dict[d]))
        else:
            ch_dict[d[1]] = [(d[0], d_dict[d])]

    root = ''
    for node in ch_dict:
        if len(node) > len(root):
            root = node

    t_dict = {}
    t_dict['name'] = root
    t_dict['parent'] = 'null'
    t_dict['children'] = []

    create_tree(t_dict, root, ch_dict, language_codes)

    t_json = json.dumps([t_dict], indent=2)
    # print(t_json)
    return t_json

def main(argv):
    distance_to_tree(d_dict)

if __name__ == "__main__":
    main(sys.argv[1:])
