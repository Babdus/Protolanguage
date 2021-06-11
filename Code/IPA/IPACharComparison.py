from IPA.IPAChar import IPAChar
from IPA.IPAData import *
from munkres import Munkres, DISALLOWED
from IPA.dijkstra import *
import pickle

cache = {}

def read_cache(path):
    global cache
    with open(path, 'rb') as f:
        cache = pickle.load(f)

def save_cache(path):
    with open(path, 'wb') as f:
        pickle.dump(cache, f)

def in_the_same_cluster(f1, f2):
    s1 = places | secondary_places
    s2 = manners | secondary_manners
    s3 = airflows
    return (f1 in s1 and f2 in s1) or (f1 in s2 and f2 in s2) or (f1 in s3 and f2 in s3) or (f1 in {'GL', 'GZ'} and f2 in {'EJ', 'IT'}) or (f1 in {'EJ', 'IT'} and f2 in {'GL', 'GZ'})

class IPACharComparison:
    def __init__(self):
        pass

    def compare(self, ch1, ch2, asymmetric=False, relat_dist_to_ch1=0.5):
        global cache
        self.char1 = ch1
        self.char2 = ch2

        self.parent = ch1 if asymmetric else None

        if not asymmetric:
            if (ch1.symbol(), ch2.symbol()) in cache:
                self.distance = cache[(ch1.symbol(), ch2.symbol())]
                return

        self.distance = 0
        self.way = {}
        set1 = self.char1.features - self.char2.features
        set2 = self.char2.features - self.char1.features

        if len(set1) + len(set2) == 0:
            return

        if asymmetric:
            self.find_parent(set1 | set2, tuple(sorted(list(set1))), tuple(sorted(list(set2))), relat_dist_to_ch1)
            return

        column_names = [f1 for f1 in set1] + ['X' for x in set2]
        row_names = [f2 for f2 in set2] + ['X' for x in set1]
        matrix = []
        for f2 in set2:
            row = [feature_distance_map[(f1, f2)] if in_the_same_cluster(f1, f2) else DISALLOWED for f1 in set1]
            row += [feature_distance_map[('X', f2)] for x in set2]
            matrix.append(row)
        for y in range(len(set1)):
            row = [feature_distance_map[(f1, 'X')] for f1 in set1]
            row += [0 for x in set2]
            matrix.append(row)

        munkres = Munkres()
        indexes = munkres.compute(matrix)
        indexes = [step for step in indexes if step[1] < len(set1) or step[0] < len(set2)]
        self.distance = sum(matrix[step[0]][step[1]] for step in indexes)
        self.way = {column_names[step[1]]: row_names[step[0]] for step in indexes}

        if not asymmetric:
            cache[(ch1.symbol(), ch2.symbol())] = self.distance
            cache[(ch2.symbol(), ch1.symbol())] = self.distance
            print(len(cache), end='\r')

    @staticmethod
    def is_valid_sound(features):
        # TODO check here real validity of generated protosounds
        valid = (len(features & places) == 1 or (len(features & {'AL', 'PA'}) == 2 and len(features & places) == 2)) and len(features & manners) == 1
        return valid

    @staticmethod
    def adjust_features(features):
        if 'SF' in features and len(coronals & features) == 0:
            features.remove('SF')
            features.add('NF')
        if 'SS' in features and len(coronals & features) == 0:
            features.remove('SS')
            features.add('NS')
        if 'LA' in features and (len(linguals & features) == 0 or len(vowels & features) > 0):
            features.remove('LA')
        if 'LA' in features and 'PL' in features:
            features.remove('PL')
            features.add('NF')
        if len(features & vowels) > 0 and len(features & vowelable_places) == 0:
            features = features - vowels
            features.add('SV')
        if len(features & vowels) > 0 and len(features & (places - vowelable_places)) > 0:
            features = features - (places - vowelable_places)
        if 'VI' in features and len(features & vibrantable_places) == 0:
            features.remove('VI')
            features.add('NS')
        if 'TA' in features and len(features & vibrantable_places) == 0:
            features.remove('TA')
            features.add('PL')
        if len({'PO', 'PL'} & features) > 1:
            features.remove('PO')
            features.add('AL')
        if len({'PO', 'NA'} & features) > 1:
            features.remove('PO')
            features.add('AL')
        if len({'PO', 'VI'} & features) > 1:
            features.remove('PO')
            features.add('AL')
        if len({'PO', 'TA'} & features) > 1:
            features.remove('PO')
            features.add('AL')
        if len({'DE', 'PL'} & features) > 1:
            features.remove('DE')
            features.add('AL')
        if len({'PA', 'PZ'} & features) > 1:
            features.remove('PZ')
        if len({'VE', 'VZ'} & features) > 1:
            features.remove('VZ')
        if len({'LB', 'LZ'} & features) > 1:
            features.remove('LZ')
        if len({'RE', 'RZ'} & features) > 1:
            features.remove('RZ')
        if len({'PH', 'HZ'} & features) > 1:
            features.remove('HZ')
        if len({'GL', 'GZ'} & features) > 1:
            features.remove('GZ')
        if len({'PZ', 'VE'} & features) > 1:
            features.remove('PZ')
            features.remove('VE')
            features.add('NE')
        if len({'PZ', 'VZ'} & features) > 1:
            features.remove('PZ')
            features.remove('VZ')
        if len({'AL', 'PA', 'SV'} & features) > 2:
            features.remove('AL')
        if len({'AL', 'PA', 'TA'} & features) > 2 or len({'AL', 'PA', 'VI'} & features) > 2:
            features.remove('PA')
            features.add('PZ')
        if len({'VZ', 'PA'} & features) > 1 and len(features & places) == 1:
            features.remove('PA')
            features.remove('VZ')
            features.add('NE')
        if len({'NA', 'GL'} & features) > 1:
            features.remove('NA')
            features.add('NZ')
            features.add('NS')
        if len({'NA', 'PH'} & features) > 1:
            features.remove('PH')
            features.add('UV')
        return features

    def find_parent(self, feature_set, vertex1, vertex2, relat_dist_to_ch1):
        if vertex1 == ():
            vertex1 = 'X'
        if vertex2 == ():
            vertex2 = 'X'
        dists_to_char1, next_nodes_to_char1 = dijkstra(vertex1, feature_set, asymmetric_feature_distance_map)
        dists_to_char2, next_nodes_to_char2 = dijkstra(vertex2, feature_set, asymmetric_feature_distance_map)

        same_features = self.char1.features & self.char2.features
        relat_dists_to_char1 = {}
        for node in dists_to_char1:
            if IPACharComparison.is_valid_sound(set(node) | same_features):
                total = dists_to_char1[node] + dists_to_char2[node]
                relat_dists_to_char1[node] = (dists_to_char1[node] / total, total)

        minimal_distance = relat_dists_to_char1[min(relat_dists_to_char1, key=lambda x: relat_dists_to_char1[x][1])][1]
        sorted_distances = sorted(relat_dists_to_char1.items(), key=lambda item: item[1][1]/minimal_distance/2 + abs(item[1][0]-relat_dist_to_ch1))
        self.sorted_distances = sorted_distances
        parent_features = IPACharComparison.adjust_features(set(sorted_distances[0][0]) | same_features)

        try:
            self.parent = IPAChar(parent_features, create_from_set=True, printing=False)
        except ValueError as e:
            print(e)
            print('Context:', self.char1, self.char2)

        self.distance = sorted_distances[0][1][1]

    def get_distance(self):
        return self.distance

    def get_parent(self):
        return self.parent

    def get_way(self):
        return self.way

    def __str__(self):
        return f'Distance: {self.distance}\nWay: ' + "".join([f'{step}->{self.way[step]}\n' for step in self.way])
