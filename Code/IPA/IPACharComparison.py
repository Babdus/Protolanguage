from IPA.IPAChar import IPAChar
from IPA.IPAData import feature_distance_map, places, secondary_places, manners, secondary_manners, airflows
from munkres import Munkres, DISALLOWED

def in_the_same_cluster(f1, f2):
    s1 = places | secondary_places
    s2 = manners | secondary_manners
    s3 = airflows
    return (f1 in s1 and f2 in s1) or (f1 in s2 and f2 in s2) or (f1 in s2 and f2 in s2) or (f1 in {'GL', 'GZ'} and f2 in {'EJ', 'IT'}) or (f1 in {'EJ', 'IT'} and f2 in {'GL', 'GZ'})

class IPACharComparison:
    def __init__(self):
        pass

    def compare(self, ch1, ch2):
        self.char1 = ch1
        self.char2 = ch2
        self.distance = 0
        self.way = {}
        set1 = self.char1.features - self.char2.features
        set2 = self.char2.features - self.char1.features
        if len(set1) + len(set2) == 0:
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

    def get_distance(self):
        return self.distance

    def get_way(self):
        return self.way

    def __str__(self):
        return f'Distance: {self.distance}\nWay: ' + "".join([f'{step}->{self.way[step]}\n' for step in self.way])
