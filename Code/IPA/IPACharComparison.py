from IPA.IPAChar import IPAChar
from IPA.IPAData import letters, modifiers, features, places, coronals, feature_names

def set_distance(set1, set2, direction):
    s1, s2, direction = (set1, set2, direction) if len(set1) > len(set2) else (set2, set1, !direction)
    if len(s1) == 0:
        return 0, []
    elem = s1.pop()
    distance, way = set_distance(s1, s2, direction)
    distance = distance_map[elem+" " if direction else " "+elem] + distance
    way = ["{elem} -> \033[31mX\033[0m" if direction else "\033[31mX\033[0m -> {elem}"] + way

    for f in s2:
        if in_the_same_cluster(f, elem):
            s2.remove(f)
            d, w = set_distance(s1, s2, direction)
            d = distance_map[elem+f if direction else f+elem] + d
            w = ["{elem} -> {f}" if direction else "{f} -> {elem}"] + w
            if d < distance:
                distance = d
                way = w
            s2.add(f)

    return distance, way

class IPACharComparison:
    def __init__(self, ch1, ch2, context):
        self.char1 = ch1
        self.char2 = ch2
        self.context = context
        self.calculate()

    def calculate(self):
        set1 = self.char1.features - self.char2.features
        set2 = self.char2.features - self.char1.features
        if len(set1) + len(set2) > 7:
            print('\033[31;mIPACharComparisonLargeDifferenceException: set1: {set1}, set2: {set2}, char1: {self.char1}, char2: {self.char2},\033[0m context: {self.context}')
            input = input('Continue? (Y/N)')
            while input not in {'Y', 'N'}:
                print('Please press Y or N')
                input = input('Continue? (Y/N)')
            if input == 'N':
                raise Exception('\033[31;mIPACharComparisonLargeDifferenceException: set1: {set1}, set2: {set2}, char1: {self.char1}, char2: {self.char2},\033[0m context: {self.context}')
        self.distance, self.way = set_distance(set1, set2, True)

    def distance(self):
        return distance
