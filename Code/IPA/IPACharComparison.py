from IPA.IPAChar import IPAChar
from IPA.IPAData import letters, modifiers, features, places, coronals, feature_names

class IPACharComparison:
    def __init__(self, ch1, ch2):
        self.char1 = ch1
        self.char2 = ch2
        self.calculate()

    def calculate(self):
        c1 = self.char1.counter
        c2 = self.char2.counter
        self.distance = sum((c2 - c1 - (c2 & c1)).values()) + sum((c1 - c2 - (c1 & c2)).values()) + sum((c1 & c2).values())

    def distance(self):
        return distance
