from IPA.IPAString import IPAString
from IPA.IPAChar import IPAChar
from IPA.IPAData import letters, modifiers, features, places, coronals, feature_names
from IPA.IPACharComparison import IPACharComparison
import numpy as np

class IPAStringComparison:
    def __init__(self):
        pass

    def compare(self, s1, s2, asymmetric=False, relat_dist_to_word1=0.5):
        self.str1 = s1
        self.str2 = s2
        seq1 = s1.chars
        seq2 = s2.chars
        oneago = None
        thisrow = [(ph.create_cost(), (('add: '+ph.symbol(), (-1, i)),)) for i, ph in enumerate(seq2)] + [(0, ())]
        for y in range(len(seq2)):
            thisrow[y] = (thisrow[y-1][0] + thisrow[y][0], thisrow[y-1][1] + thisrow[y][1])
        comparer = IPACharComparison()
        for x in range(len(seq1)):
            twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [(thisrow[-1][0] + seq1[x].delete_cost(), thisrow[-1][1] + (('del: '+seq1[x].symbol(), (x, -1)),))]
            for y in range(len(seq2)):
                delcost = oneago[y][0] + seq1[x].delete_cost()
                addcost = thisrow[y-1][0] + seq2[y].create_cost()
                comparer.compare(seq1[x], seq2[y], asymmetric=asymmetric, relat_dist_to_ch1=relat_dist_to_word1)
                subcost = oneago[y-1][0] + comparer.distance
                thisrow[y] = min(delcost, addcost, subcost)

                argmin = np.argmin((delcost, addcost, subcost))
                if argmin == 0:
                    thisrow[y] = (delcost, oneago[y][1] + (('del: '+seq1[x].symbol(), (x, y)),))
                if argmin == 1:
                    thisrow[y] = (addcost, thisrow[y-1][1] + (('add: '+seq2[y].symbol(), (x, y)),))
                if argmin == 2:
                    step = (('sub: '+seq1[x].symbol()+' '+seq2[y].symbol(), (x, y, comparer.parent)),) if comparer.distance > 0 else ()
                    thisrow[y] = (subcost, oneago[y-1][1] + step)

                # if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
                #     and seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
                #     if twoago[y - 2][0] + 5 < thisrow[y][0]:
                #         print(thisrow[y][1][:-2])
                #         print(thisrow[y][1])
                #         thisrow[y] = (twoago[y - 2][0] + 5, thisrow[y][1][:-2] + ('tra: '+seq2[y].symbol()+' '+seq1[x].symbol(),))
        self.distance, self.steps = thisrow[len(seq2)-1]

        if asymmetric:
            word_as_dict_of_indexes = {i: [ch] for i, ch in enumerate(seq1)}
            for step in self.steps:
                action = step[0]
                indexes = step[1][:2]
                if len(step[1]) > 2:
                    parent_sound = step[1][2]
                choice = np.random.choice([True, False], 1, p=[relat_dist_to_word1, 1-relat_dist_to_word1])[0]
                if choice and action[:3] == 'add':
                    if indexes[0] in word_as_dict_of_indexes:
                        word_as_dict_of_indexes[indexes[0]].append(seq2[indexes[1]])
                    else:
                        word_as_dict_of_indexes[indexes[0]] = [seq2[indexes[1]]]
                elif choice and action[:3] == 'del':
                    del word_as_dict_of_indexes[indexes[0]]
                elif action[:3] == 'sub':
                    word_as_dict_of_indexes[indexes[0]][0] = parent_sound
            self.parent = IPAString([item for index in sorted(list(word_as_dict_of_indexes)) for item in word_as_dict_of_indexes[index]], create_from_char_array=True)

        return thisrow[len(seq2)-1]

    def distance(self):
        return self.distance

    def steps(self):
        return self.steps
