from IPA.IPAString import IPAString
from IPA.IPAChar import IPAChar
from IPA.IPAData import letters, modifiers, features, places, coronals, feature_names
from IPA.IPACharComparison import IPACharComparison
import numpy as np

class IPAStringComparison:
    def __init__(self):
        pass

    def compare(self, s1, s2):
        self.str1 = s1
        self.str2 = s2
        seq1 = s1.chars
        seq2 = s2.chars
        oneago = None
        thisrow = [(ph.create_cost(), ('add: '+ph.symbol(),)) for ph in seq2] + [(0, ())]
        for y in range(len(seq2)):
            thisrow[y] = (thisrow[y-1][0] + thisrow[y][0], thisrow[y-1][1] + thisrow[y][1])
        comparer = IPACharComparison()
        for x in range(len(seq1)):
            twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [(thisrow[-1][0] + seq1[x].delete_cost(), thisrow[-1][1] + ('del: '+seq1[x].symbol(),))]
            for y in range(len(seq2)):
                delcost = oneago[y][0] + seq1[x].delete_cost()
                addcost = thisrow[y-1][0] + seq2[y].create_cost()
                comparer.compare(seq1[x], seq2[y])
                subcost = oneago[y-1][0] + comparer.distance
                thisrow[y] = min(delcost, addcost, subcost)

                argmin = np.argmin((delcost, addcost, subcost))
                if argmin == 0:
                    thisrow[y] = (delcost, oneago[y][1] + ('del: '+seq1[x].symbol(),))
                if argmin == 1:
                    thisrow[y] = (addcost, thisrow[y-1][1] + ('add: '+seq2[y].symbol(),))
                if argmin == 2:
                    step = ('sub: '+seq1[x].symbol()+' '+seq2[y].symbol(),) if comparer.distance > 0 else ()
                    thisrow[y] = (subcost, oneago[y-1][1] + step)

                # if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
                #     and seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
                #     if twoago[y - 2][0] + 5 < thisrow[y][0]:
                #         print(thisrow[y][1][:-2])
                #         print(thisrow[y][1])
                #         thisrow[y] = (twoago[y - 2][0] + 5, thisrow[y][1][:-2] + ('tra: '+seq2[y].symbol()+' '+seq1[x].symbol(),))
        self.distance, self.steps = thisrow[len(seq2)-1]
        return thisrow[len(seq2)-1]

    def distance(self):
        return self.distance

    def steps(self):
        return self.steps
