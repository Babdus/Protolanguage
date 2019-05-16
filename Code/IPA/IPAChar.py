from collections import Counter
from IPA.IPAData import replace_with, letters, ignore_set, modifiers, features, places, coronals, feature_names

class IPAChar:
    def __init__(self, symbols):
        self.modifiers = []
        self.symbols = ''
        self.features = None
        for i, symbol in enumerate(symbols):
            if symbol in replace_with:
                symbol = replace_with[symbol]
            if symbol in letters:
                if len(self.symbols) > 0:
                    ch = IPAChar(symbol)
                    if ch.is_spirant() and self.is_plosive() and !self.has_modifiers() and self.has_same_place(ch):
                        self.make_affricate(ch)
                else
                    self.symbols += symbol
                    self.features = letters[symbol]
            elif symbol in modifiers and len(self.features) > 0:
                method = modifiers[symbol]
                args = method['args']
                action = method['action']
                getattr(self, action)(symbol, *args)
                self.symbols += symbol
                self.modifiers.append(symbol)
            elif symbol in ignore_set:
                continue
            else:
                raise ValueError(f"\033[31m {symbol} \033[0m, context: {symbols}")

    def add(self, symbol, *args):
        for arg in args:
            for key, value in features.items():
                if arg in value:
                    whole = True
                    for feature in value:
                        if feature in self.counter:
                            self.counter[feature] /= 2
                            whole = False
                    self.counter[arg] += 12 if whole else 6
        self.symbols += symbol

    def make(self, symbol, *args):
        cluster = args[0]
        for feature in features[cluster]:
            del self.counter[feature]
        feature = args[1]
        self.counter[feature] = 12
        self.symbols += symbol

    def half_labialize(self, symbol):
        for place in places:
            if place in self.counter:
                self.counter[place] *= 3/4
        self.counter['LB'] += 3
        self.symbols += symbol

    def devoice(self, symbol):
        if self.counter['VO'] > 0:
            del self.counter['VO']
            self.symbols += symbol

    def intensify(self, symbol):
        self.counter['EJ'] += 6
        self.symbols += symbol

    def dentalize(self, symbol):
        if self.counter['LB'] > 0:
            self.counter['LD'] += self.counter['LB']
            del self.counter['LB']
            self.symbols += symbol
        if self.counter['AL'] > 0:
            self.counter['DE'] += self.counter['AL']
            del self.counter['AL']
            self.symbols += symbol
        if self.counter['PO'] > 0:
            self.counter['DE'] += self.counter['PO']
            del self.counter['PO']
            self.symbols += symbol
        if self.counter['PO'] > 0:
            self.counter['DE'] += self.counter['PO']
            del self.counter['PO']
            self.symbols += symbol

    def advance(self, symbol):
        if self.counter['LD'] > 0:
            self.counter['LB'] += self.counter['LD']
            del self.counter['LD']
            self.symbols += symbol
        if self.counter['DE'] > 0:
            self.counter['LL'] += self.counter['DE']/2
            self.counter['DE'] /= 2
            self.symbols += symbol
        if self.counter['AL'] > 0:
            self.counter['DE'] += self.counter['AL']
            del self.counter['AL']
            self.symbols += symbol
        if self.counter['PO'] > 0:
            self.counter['AL'] += self.counter['PO']
            del self.counter['PO']
            self.symbols += symbol
        if self.counter['RE'] > 0:
            self.counter['PO'] += self.counter['RE']
            del self.counter['RE']
            self.symbols += symbol
        if self.counter['PA'] > 0:
            self.counter['AL'] += self.counter['PA']/2
            self.counter['PA'] /= 2
            self.symbols += symbol
        if self.counter['VE'] > 0:
            fraction = 1/2
            if self.counter['CL'] + self.counter['OP'] == 12:
                fraction = 1/4
            self.counter['PA'] += self.counter['VE']*fraction
            self.counter['VE'] -= self.counter['VE']*fraction
            self.symbols += symbol
        if self.counter['UV'] > 0:
            self.counter['VE'] += self.counter['UV']/2
            self.counter['UV'] /= 2
            self.symbols += symbol
        if self.counter['PH'] > 0:
            self.counter['UV'] += self.counter['PH']
            del self.counter['PH']
            self.symbols += symbol
        if self.counter['GL'] > 0:
            self.counter['PH'] += self.counter['GL']
            del self.counter['GL']
            self.symbols += symbol

    def lower(self, symbol):
        if self.counter['CL'] + self.counter['OP'] == 12:
            self.counter['CL'] -= 2
            self.counter['OP'] += 2
            if self.counter['OP'] > 12:
                self.counter['OP'] = 12
            if self.counter['CL'] < 0:
                self.counter['CL'] = 0
            self.symbols += symbol
        if self.counter['SP'] + self.counter['CL'] == 12:
            self.counter['SP'] -= 3
            self.counter['CL'] += 3
            if self.counter['CL'] > 12:
                self.counter['CL'] = 12
            if self.counter['SP'] < 0:
                self.counter['SP'] = 0
            self.symbols += symbol
        if self.counter['SP'] + self.counter['VI'] == 12:
            self.counter['SP'] -= 6
            self.counter['VI'] += 6
            if self.counter['VI'] > 12:
                self.counter['VI'] = 12
            if self.counter['SP'] < 0:
                self.counter['SP'] = 0
            self.symbols += symbol
        if self.counter['SP'] + self.counter['TA'] == 12:
            self.counter['SP'] -= 6
            self.counter['TA'] += 6
            if self.counter['TA'] > 12:
                self.counter['TA'] = 12
            if self.counter['SP'] < 0:
                self.counter['SP'] = 0
            self.symbols += symbol
        if self.counter['PL'] + self.counter['SP'] == 12:
            self.counter['PL'] -= 3
            self.counter['SP'] += 3
            if self.counter['SP'] > 12:
                self.counter['SP'] = 12
            if self.counter['PL'] < 0:
                self.counter['PL'] = 0
            self.symbols += symbol

    def upper(self, symbol):
        if self.counter['PL'] + self.counter['SP'] == 12:
            self.counter['PL'] += 3
            self.counter['SP'] -= 3
            if self.counter['SP'] < 0:
                self.counter['SP'] = 0
            if self.counter['PL'] > 12:
                self.counter['PL'] = 12
            self.symbols += symbol
        if self.counter['SP'] + self.counter['VI'] == 12:
            self.counter['SP'] += 6
            self.counter['VI'] -= 6
            if self.counter['VI'] < 0:
                self.counter['VI'] = 0
            if self.counter['SP'] > 12:
                self.counter['SP'] = 12
            self.symbols += symbol
        if self.counter['SP'] + self.counter['TA'] == 12:
            self.counter['SP'] += 6
            self.counter['TA'] -= 6
            if self.counter['TA'] < 0:
                self.counter['TA'] = 0
            if self.counter['SP'] > 12:
                self.counter['SP'] = 12
            self.symbols += symbol
        if self.counter['SP'] + self.counter['CL'] == 12:
            self.counter['SP'] += 3
            self.counter['CL'] -= 3
            if self.counter['CL'] < 0:
                self.counter['CL'] = 0
            if self.counter['SP'] > 12:
                self.counter['SP'] = 12
            self.symbols += symbol
        if self.counter['CL'] + self.counter['OP'] == 12:
            self.counter['CL'] += 2
            self.counter['OP'] -= 2
            if self.counter['CL'] > 12:
                self.counter['CL'] = 12
            if self.counter['OP'] < 0:
                self.counter['OP'] = 0
            self.symbols += symbol

    def make_affricate(self, last_symbol):
        self.symbols = last_symbol + self.symbols
        plosive_space = 12 - self.counter['PL']
        spirnt = self.counter['SP']
        self.counter['SP'] -= plosive_space/2
        self.counter['PL'] += plosive_space/2

    def name(self):
        if self.counter is not None:
            return ", ".join(feature_names[key] if self.counter[key] == 12 else f"{round(self.counter[key] / 0.12)}% {feature_names[key]}" for key in self.counter)

    def __str__(self):
        return f"{self.symbols}: {self.name()}"

    def symbol(self):
        return self.symbols

    def get_modifiers(self):
        return self.modifiers

    def has_modifiers(self):
        return len(self.modifiers) > 0

    def is_spirant(self):
        return 'NS' in self.features or 'SS' in self.features

    def is_plosive(self):
        return 'PL' in self.features

    def coronal(self):
        coronal = 0
        for feature in coronals.intersection(self.counter):
            coronal += self.counter[feature]
        return coronal

    def places(self):
        return places.intersection(self.counter)

    def has_same_place(self, other_ch):
        # TODO
        if self.coronal() >= 3 and other_ch.coronal() >= 3:
            return True
        if len(self.places().intersection(other_ch.places())) > 0:
            return True
        return False

    def distance(ch1, ch2):
        c1 = ch1.counter if hasattr(ch1, 'counter') else IPAChar(ch1).counter
        c2 = ch2.counter if hasattr(ch2, 'counter') else IPAChar(ch2).counter
        return sum((c1[f] - c2[f]) if c1[f] > c2[f] else (c2[f] - c1[f]) for f in feature_names)/12
