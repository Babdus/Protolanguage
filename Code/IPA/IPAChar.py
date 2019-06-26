from IPA.IPAData import replace_with, letters, ignore_set, modifiers, features, places, coronals, vowels, feature_names, feature_distance_map, reversed_letters

class IPAChar:
    def __init__(self, symbols, printing=True, create_from_set=False):
        self.modifiers = set()
        self.symbols = ''
        self.features = None
        if create_from_set:
            self.create_from_set(symbols)
            if printing:
                print(str(self))
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
        self.remaining_features = self.features.copy()
        tup = tuple(sorted(list(feats)))
        if tup in reversed_letters:
            self.symbols += reversed_letters[tup]
        plosive = ''
        if len(self.symbols) == 0:
            if 'NF' in self.remaining_features:
                pl = (self.remaining_features & (places | {'VO'})) | {'PL'}
                if 'PO' in pl:
                    pl.remove('PO')
                    pl.add('AL')
                if 'DE' in pl:
                    pl.remove('DE')
                    pl.add('AL')
                if 'NE' in pl:
                    pl.remove('NE')
                    pl.add('VE')
                tup = tuple(sorted(list(pl)))
                if tup in reversed_letters:
                    plosive = reversed_letters[tup]
                    self.remaining_features.remove('NF')
                    self.remaining_features.add('NS')
                    tup = tuple(sorted(list(self.remaining_features)))
                    if tup in reversed_letters:
                        self.symbols += reversed_letters[tup]

            if 'SF' in self.remaining_features:
                pl = (self.remaining_features & (places | {'VO'})) | {'PL'}
                if 'PO' in pl:
                    pl.remove('PO')
                    pl.add('AL')
                if 'DE' in pl:
                    pl.remove('DE')
                    pl.add('AL')
                if 'NE' in pl:
                    pl.remove('NE')
                    pl.add('VE')
                tup = tuple(sorted(list(pl)))
                if tup in reversed_letters:
                    plosive = reversed_letters[tup]
                    self.remaining_features.remove('SF')
                    self.remaining_features.add('SS')
                    tup = tuple(sorted(list(self.remaining_features)))
                    if tup in reversed_letters:
                        self.symbols += reversed_letters[tup]



        if len(self.symbols) == 0:
            not_found = True
            if not_found and 'NE' in self.remaining_features:
                if len(self.remaining_features & vowels) == 0:
                    self.modifiers.add(u'\u031f')
                    self.remaining_features.remove('NE')
                    self.remaining_features.add('VE')
                    tup = tuple(sorted(list(self.remaining_features)))
                    if tup in reversed_letters:
                        self.symbols += reversed_letters[tup]
                        not_found = False
            if not_found and 'NZ' in self.remaining_features:
                self.modifiers.add(u'\u0303')
                self.remaining_features.remove('NZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'IT' in self.remaining_features:
                self.modifiers.add(u'\u0348')
                self.remaining_features.remove('IT')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'LH' in self.remaining_features:
                self.modifiers.add(u'\u0339')
                self.remaining_features.remove('LH')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'AS' in self.remaining_features:
                if 'VO' in self.remaining_features:
                    self.modifiers.add('ʱ')
                else:
                    self.modifiers.add('ʰ')
                self.remaining_features.remove('AS')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'EJ' in self.remaining_features:
                self.modifiers.add('ʼ')
                self.remaining_features.remove('EJ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and len(self.remaining_features & {'NO', 'MI', 'NC'}) > 0:
                vowel_dict = {'NO': 'MO', 'NC': 'CL', 'MI': 'MC'}
                vowel = (self.remaining_features & {'NO', 'MI', 'NC'}).pop()
                self.remaining_features.remove(vowel)
                vowel = vowel_dict[vowel]
                self.remaining_features.add(vowel)
                self.modifiers.add(u'\u031e')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and len({'LZ', 'VZ'} & self.remaining_features) > 1:
                self.modifiers.add('ʷ')
                self.remaining_features.remove('LZ')
                self.remaining_features.remove('VZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'LZ' in self.remaining_features:
                self.modifiers.add('ᵝ')
                self.remaining_features.remove('LZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'RZ' in self.remaining_features:
                self.modifiers.add('˞')
                self.remaining_features.remove('RZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'PZ' in self.remaining_features:
                self.modifiers.add('ʲ')
                self.remaining_features.remove('PZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'VZ' in self.remaining_features:
                self.modifiers.add('ˠ')
                self.remaining_features.remove('VZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'HZ' in self.remaining_features:
                self.modifiers.add('ˁ')
                self.remaining_features.remove('HZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'GZ' in self.remaining_features:
                self.modifiers.add('ˀ')
                self.remaining_features.remove('GZ')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
            if not_found and 'LA' in self.remaining_features:
                self.modifiers.add('ˡ')
                self.remaining_features.remove('LA')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and 'SV' in self.remaining_features:
                self.modifiers.add(u'\u031e')
                self.remaining_features.remove('SV')
                self.remaining_features.add('NS')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False
                else:
                    self.modifiers.remove(u'\u031e')
                    self.remaining_features.add('SV')
                    self.remaining_features.remove('NS')

            if not_found and 'NS' in self.remaining_features and len(coronals & self.remaining_features) > 0:
                self.modifiers.add(u'\u031e')
                self.remaining_features.remove('NS')
                self.remaining_features.add('SS')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and 'DE' in self.remaining_features:
                self.modifiers.add(u'\u032a')
                self.remaining_features.remove('DE')
                self.remaining_features.add('AL')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and 'LD' in self.remaining_features:
                self.modifiers.add(u'\u032a')
                self.remaining_features.remove('LD')
                self.remaining_features.add('LB')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and len({'AL', 'PA', 'PL'} & self.remaining_features) == 3:
                self.modifiers.add(u'\u031f')
                self.remaining_features.remove('AL')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and 'IN' in self.remaining_features:
                self.modifiers.add('↓')
                self.remaining_features.remove('IN')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and 'VO' in self.remaining_features:
                self.modifiers.add(u'\u032c')
                self.remaining_features.remove('VO')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

            if not_found and 'VO' not in self.features:
                self.modifiers.add(u'\u030a')
                self.remaining_features.add('VO')
                tup = tuple(sorted(list(self.remaining_features)))
                if tup in reversed_letters:
                    self.symbols += reversed_letters[tup]
                    not_found = False

        if len(self.symbols) < 1:
            raise ValueError("Don't know how to interpret", str(self.features))

        for modifier in self.modifiers:
            if modifier >= u'\u0300' and modifier < u'\u0400':
                self.symbols += modifier
        for modifier in self.modifiers:
            if modifier < u'\u0300' or modifier >= u'\u0400':
                self.symbols += modifier

        self.symbols = plosive + self.symbols


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
