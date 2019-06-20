from IPA.IPAData import replace_with, letters, ignore_set, modifiers, features, places, coronals, vowels, feature_names, feature_distance_map, reversed_letters

class IPAChar:
    def __init__(self, symbols, printing=True, create_from_set=False):
        self.modifiers = set()
        self.symbols = ''
        self.features = None
        if create_from_set:
            self.create_from_set(symbols)
            return
        for i, symbol in enumerate(symbols):
            if symbol in replace_with:
                symbol = replace_with[symbol]
            if symbol in letters:
                if len(self.symbols) > 0:
                    ch = IPAChar(symbol, printing=False)
                    if ch.is_spirant() and self.is_plosive() and not self.has_modifiers() and self.has_same_place(ch) and self.has_same_voice(ch):
                        self.make_affricate(ch)
                    else:
                        raise Exception(f"\033[31mToo many symbols for one character\033[0m, context: {symbols}")
                else:
                    self.symbols += symbol
                    self.features = letters[symbol].copy()
            elif symbol in modifiers and len(self.features) > 0:
                method = modifiers[symbol]
                args = method['args']
                action = method['action']
                getattr(self, action)(symbol, *args)
                self.modifiers.add(symbol)
            elif symbol in ignore_set:
                continue
            else:
                raise ValueError(f"\033[31m {symbol} \033[0m, context: {symbols}")
        if printing:
            print(str(self))

    def create_from_set(self, feats):
        if 'X' in feats:
            feats.remove('X')
        self.features = feats
        tup = tuple(sorted(list(feats)))
        if tup in reversed_letters:
            self.symbols += reversed_letters[tup]
        if len(self.symbols) == 0:
            if 'NF' in self.features:
                pl = tuple(sorted(list((self.features - {'NF'}) | {'PL'})))
                sp = tuple(sorted(list((self.features - {'NF'}) | {'NS'})))
                if pl in reversed_letters and sp in reversed_letters:
                    self.symbols += reversed_letters[pl]
                    self.symbols += reversed_letters[sp]
            if 'SF' in self.features:
                pl = tuple(sorted(list((self.features - {'SF'}) | {'PL'})))
                sp = tuple(sorted(list((self.features - {'SF'}) | {'NS'})))
                if pl in reversed_letters and sp in reversed_letters:
                    self.symbols += reversed_letters[pl]
                    self.symbols += reversed_letters[sp]

    def delete_cost(self):
        return sum(feature_distance_map[(f, 'X')] for f in self.features)

    def create_cost(self):
        return sum(feature_distance_map[('X', f)] for f in self.features)

    def add(self, symbol, *args):
        for arg in args:
            self.features.add(arg)
        self.symbols += symbol

    def remove(self, symbol, *args):
        for arg in args:
            if arg in self.features:
                self.features.remove(arg)
        self.symbols += symbol

    def add_and_remove(self, symbol, *args):
        self.add(symbol, *args[0])
        self.remove('', *args[1])

    def make(self, symbol, *args):
        cluster = args[0]
        for feature in features[cluster]:
            if feature in self.features:
                self.features.remove(feature)
        feature = args[1]
        self.features.add(feature)
        self.symbols += symbol

    def dentalize(self, symbol):
        if 'LB' in self.features:
            self.add_and_remove(symbol, ['LD'], ['LB'])
        elif 'AL' in self.features:
            self.add_and_remove(symbol, ['DE'], ['AL'])
        elif 'PO' in self.features:
            self.add_and_remove(symbol, ['DE'], ['PO'])

    def advance(self, symbol):
        if 'LD' in self.features:
            self.add_and_remove(symbol, ['LB'], ['LD'])
        elif 'DE' in self.features:
            self.add_and_remove(symbol, ['LL'], ['DE'])
        elif 'AL' in self.features:
            self.add_and_remove(symbol, ['DE'], ['AL'])
        elif 'PO' in self.features:
            self.add_and_remove(symbol, ['AL'], ['PO'])
        elif 'RE' in self.features:
            self.add_and_remove(symbol, ['PO'], ['RE'])
        elif 'PA' in self.features:
            self.add(symbol, 'AL')
        elif 'NE' in self.features:
            if len(self.features & vowels) > 0:
                self.add(symbol, 'PZ')
            else:
                self.add_and_remove(symbol, ['PA'], ['NE'])
        elif 'VE' in self.features:
            if len(self.features & vowels) > 0:
                self.add_and_remove(symbol, ['VZ', 'NE'], ['VE'])
            else:
                self.add_and_remove(symbol, ['NE'], ['VE'])
        elif 'UV' in self.features:
            self.add_and_remove(symbol, ['VE'], ['UV'])
        elif 'PH' in self.features:
            self.add_and_remove(symbol, ['UV'], ['PH'])
        elif 'GL' in self.features:
            self.add_and_remove(symbol, ['PH'], ['GL'])

    def lower(self, symbol):
        if 'PL' in self.features:
            self.add_and_remove(symbol, ['NS'], ['PL'])
        elif 'NF' in self.features:
            self.add_and_remove(symbol, ['NS'], ['NF'])
        elif 'SF' in self.features:
            self.add_and_remove(symbol, ['SS'], ['SF'])
        elif 'NS' in self.features:
            self.add_and_remove(symbol, ['SV'], ['NS'])
        elif 'SS' in self.features:
            self.add_and_remove(symbol, ['SV'], ['SS'])
        elif 'VI' in self.features:
            self.add_and_remove(symbol, ['SV'], ['VI'])
        elif 'TA' in self.features:
            self.add_and_remove(symbol, ['SV'], ['TA'])
        elif 'SV' in self.features:
            self.add_and_remove(symbol, ['CL'], ['SV'])
        elif 'CL' in self.features:
            self.add_and_remove(symbol, ['NC'], ['CL'])
        elif 'NC' in self.features:
            self.add_and_remove(symbol, ['MC'], ['NC'])
        elif 'MC' in self.features:
            self.add_and_remove(symbol, ['MI'], ['MC'])
        elif 'MI' in self.features:
            self.add_and_remove(symbol, ['MO'], ['MI'])
        elif 'MO' in self.features:
            self.add_and_remove(symbol, ['NO'], ['MO'])
        elif 'NO' in self.features:
            self.add_and_remove(symbol, ['OP'], ['NO'])

    def upper(self, symbol):
        if 'NF' in self.features:
            self.add_and_remove(symbol, ['PL'], ['NF'])
        elif 'SF' in self.features:
            self.add_and_remove(symbol, ['PL'], ['SF'])
        elif 'NS' in self.features:
            self.add_and_remove(symbol, ['PL'], ['NS'])
        elif 'SS' in self.features:
            self.add_and_remove(symbol, ['PL'], ['SS'])
        elif 'VI' in self.features:
            self.add_and_remove(symbol, ['NS'], ['VI'])
        elif 'TA' in self.features:
            self.add_and_remove(symbol, ['PL'], ['TA'])
        elif 'SV' in self.features:
            self.add_and_remove(symbol, ['NS'], ['SV'])
        elif 'CL' in self.features:
            self.add_and_remove(symbol, ['SV'], ['CL'])
        elif 'NC' in self.features:
            self.add_and_remove(symbol, ['CL'], ['NC'])
        elif 'MC' in self.features:
            self.add_and_remove(symbol, ['NC'], ['MC'])
        elif 'MI' in self.features:
            self.add_and_remove(symbol, ['MC'], ['MI'])
        elif 'MO' in self.features:
            self.add_and_remove(symbol, ['MI'], ['MO'])
        elif 'NO' in self.features:
            self.add_and_remove(symbol, ['MO'], ['NO'])
        elif 'OP' in self.features:
            self.add_and_remove(symbol, ['NO'], ['OP'])

    def make_affricate(self, other_ch):
        self.features = other_ch.features.copy()
        if 'SS' in self.features:
            self.add_and_remove(other_ch.symbols, ['SF'], ['SS'])
        elif 'NS' in self.features:
            self.add_and_remove(other_ch.symbols, ['NF'], ['NS'])
        else:
            raise Exception(f"\033[31m Cannot make affricate from {self.symbols}\033[0m")

    def name(self):
        if self.features is not None:
            return ", ".join(feature_names[f] for f in self.features)

    def __str__(self):
        return f"{self.symbols}: {self.name()}"

    def __eq__(self, obj):
        return isinstance(obj, IPAChar) and obj.features == self.features

    def __ne__(self, obj):
        return not isinstance(obj, IPAChar) or obj.features != self.features

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

    def places(self):
        return places & self.features

    def has_same_place(self, other_ch):
        if 'AL' in self.features and len(coronals & other_ch.features) > 0:
            return True
        if len(self.places() & other_ch.places()) > 0:
            return True
        return False

    def has_same_voice(self, other_ch):
        if ('VO' in self.features and 'VO' in other_ch.features) or ('VO' not in self.features and 'VO' not in other_ch.features):
            return True
        return False
