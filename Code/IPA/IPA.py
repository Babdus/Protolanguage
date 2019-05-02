from collections import Counter

letters = {'p': {'LB': 12, 'PL': 12}, 'b': {'LB': 12, 'PL': 12, 'VO': 12}, 't': {'AL': 12, 'PL': 12}, 'd': {'AL': 12, 'PL': 12, 'VO': 12}, 'ʈ': {'RE': 12, 'PL': 12}, 'ɖ': {'RE': 12, 'PL': 12, 'VO': 12}, 'c': {'PA': 12, 'PL': 12}, 'ɟ': {'PA': 12, 'PL': 12, 'VO': 12}, 'k': {'VE': 12, 'PL': 12}, 'g': {'VE': 12, 'PL': 12, 'VO': 12}, 'ɡ': {'VE': 12, 'PL': 12, 'VO': 12}, 'q': {'UV': 12, 'PL': 12}, 'ɢ': {'UV': 12, 'PL': 12, 'VO': 12}, 'ʡ': {'PH': 12, 'PL': 12}, 'ʔ': {'GL': 12, 'PL': 12}, 'm': {'LB': 12, 'NA': 12, 'VO': 12}, 'ɱ': {'LD': 12, 'NA': 12, 'VO': 12}, 'n': {'AL': 12, 'NA': 12, 'VO': 12}, 'ṅ': {'AL': 12, 'NA': 12, 'VO': 12, 'replace_with': 'n'}, 'ṇ': {'AL': 12, 'NA': 12, 'VO': 12, 'replace_with': 'n'}, 'ɳ': {'RE': 12, 'NA': 12, 'VO': 12}, 'ɲ': {'PA': 12, 'NA': 12, 'VO': 12}, 'ñ': {'PA': 12, 'NA': 12, 'VO': 12, 'replace_with': 'ɲ'}, 'ŋ': {'VE': 12, 'NA': 12, 'VO': 12}, 'ɴ': {'UV': 12, 'NA': 12, 'VO': 12}, 'ʙ': {'LB': 12, 'VI': 12, 'VO': 12}, 'r': {'AL': 12, 'VI': 12, 'VO': 12}, 'ʀ': {'UV': 12, 'VI': 12, 'VO': 12}, 'ʜ': {'PH': 12, 'VI': 12}, 'ʢ': {'PH': 12, 'VI': 12, 'VO': 12}, 'ⱱ': {'LD': 12, 'TA': 12, 'VO': 12}, 'ɾ': {'AL': 12, 'TA': 12, 'VO': 12}, 'ɽ': {'RE': 12, 'TA': 12, 'VO': 12}, 'ɸ': {'LB': 12, 'SP': 12}, 'β': {'LB': 12, 'SP': 12, 'VO': 12}, 'f': {'LD': 12, 'SP': 12}, 'v': {'LD': 12, 'SP': 12, 'VO': 12}, 'θ': {'DE': 12, 'SP': 12}, 'ð': {'DE': 12, 'SP': 12, 'VO': 12}, 's': {'AL': 12, 'SP': 12}, 'z': {'AL': 12, 'SP': 12, 'VO': 12}, 'ʃ': {'PO': 12, 'SP': 12}, 'ʒ': {'PO': 12, 'SP': 12, 'VO': 12}, 'ʂ': {'RE': 12, 'SP': 12}, 'ʐ': {'RE': 12, 'SP': 12, 'VO': 12}, 'ç': {'PA': 12, 'SP': 12}, 'ʝ': {'PA': 12, 'SP': 12, 'VO': 12}, 'x': {'VE': 12, 'SP': 12}, 'ɣ': {'VE': 12, 'SP': 12, 'VO': 12}, 'χ': {'UV': 12, 'SP': 12}, 'ʁ': {'UV': 12, 'SP': 12, 'VO': 12}, 'ħ': {'PH': 12, 'SP': 12}, 'ʕ': {'PH': 12, 'SP': 9, 'CL': 3, 'VO': 12}, 'h': {'GL': 12, 'SP': 9, 'CL': 3}, 'ḥ': {'GL': 12, 'SP': 9, 'CL': 3, 'replace_with': 'h'}, 'ɦ': {'GL': 12, 'SP': 9, 'CL': 3, 'VO': 12}, 'ɬ': {'AL': 12, 'SP': 12, 'LA': 12}, 'ɮ': {'AL': 12, 'SP': 12, 'LA': 12, 'VO': 12}, 'ʋ': {'LD': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɹ': {'AL': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɻ': {'RE': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'j': {'PA': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɰ': {'VE': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'l': {'AL': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ɭ': {'RE': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ʎ': {'PA': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ʟ': {'VE': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ʘ': {'LB': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǀ': {'DE': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǃ': {'AL': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, '‼': {'RE': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǂ': {'PA': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ʞ': {'VE': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǁ': {'PL': 12, 'LA': 12, 'EJ': 6, 'IN': 6}, 'ɓ': {'LB': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ɗ': {'AL': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ᶑ': {'RE': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ʄ': {'PA': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ɠ': {'VE': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ʛ': {'UV': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ʍ': {'LB': 6, 'VE': 6, 'SP': 6, 'CL': 6, 'VO': 12}, 'w': {'LB': 6, 'VE': 6, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɥ': {'LB': 6, 'PA': 6, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɫ': {'AL': 6, 'VE': 6, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ɺ': {'AL': 12, 'TA': 12, 'LA': 12, 'VO': 12}, 'ɕ': {'AL': 6, 'PA': 6, 'SP': 12}, 'ʑ': {'AL': 6, 'PA': 6, 'SP': 12, 'VO': 12}, 'ɧ': {'PO': 6, 'VE': 6, 'SP': 12}, 'i': {'PA': 12, 'CL': 12, 'VO': 12}, 'í': {'PA': 12, 'CL': 12, 'VO': 12, 'replace_with': 'i'}, 'y': {'LB': 6, 'PA': 6, 'CL': 12, 'VO': 12}, 'ɨ': {'PA': 6, 'VE': 6, 'CL': 12, 'VO': 12}, 'ʉ': {'LB': 6, 'PA': 3, 'VE': 3, 'CL': 12, 'VO': 12}, 'ɯ': {'VE': 12, 'CL': 12, 'VO': 12}, 'u': {'LB': 6, 'VE': 6, 'CL': 12, 'VO': 12}, 'ù': {'LB': 6, 'VE': 6, 'CL': 12, 'VO': 12, 'replace_with': 'u'}, 'ú': {'LB': 6, 'VE': 6, 'CL': 12, 'VO': 12, 'replace_with': 'u'}, 'ɪ': {'PA': 8, 'VE': 4, 'CL': 10, 'OP': 2, 'VO': 12}, 'ʏ': {'LB': 6, 'PA': 4, 'VE': 2, 'CL': 10, 'OP': 2, 'VO': 12}, 'ʊ': {'LB': 6, 'PA': 2, 'VE': 4, 'CL': 10, 'OP': 2, 'VO': 12}, 'e': {'PA': 12, 'CL': 8, 'OP': 4, 'VO': 12}, 'é': {'PA': 12, 'CL': 8, 'OP': 4, 'VO': 12, 'replace_with': 'e'}, 'ø': {'LB': 6, 'PA': 6, 'CL': 8, 'OP': 4, 'VO': 12}, 'ɘ': {'PA': 6, 'VE': 6, 'CL': 8, 'OP': 4, 'VO': 12}, 'ɵ': {'LB': 6, 'PA': 3, 'VE': 3, 'CL': 8, 'OP': 4, 'VO': 12}, 'ɤ': {'VE': 12, 'CL': 8, 'OP': 4, 'VO': 12}, 'o': {'LB': 6, 'VE': 6, 'CL': 8, 'OP': 4, 'VO': 12}, 'ó': {'LB': 6, 'VE': 6, 'CL': 8, 'OP': 4, 'VO': 12, 'replace_with': 'o'}, 'ò': {'LB': 6, 'VE': 6, 'CL': 8, 'OP': 4, 'VO': 12, 'replace_with': 'o'}, 'ə': {'PA': 6, 'VE': 6, 'CL': 6, 'OP': 6, 'VO': 12}, 'ɛ': {'PA': 12, 'CL': 4, 'OP': 8, 'VO': 12}, 'œ': {'LB': 6, 'PA': 6, 'CL': 4, 'OP': 8, 'VO': 12}, 'ɜ': {'PA': 6, 'VE': 6, 'CL': 4, 'OP': 8, 'VO': 12}, 'ɞ': {'LB': 6, 'PA': 3, 'VE': 3, 'CL': 4, 'OP': 8, 'VO': 12}, 'ʌ': {'VE': 12, 'CL': 4, 'OP': 8, 'VO': 12}, 'ɔ': {'LB': 6, 'VE': 6, 'CL': 4, 'OP': 8, 'VO': 12}, 'æ': {'PA': 12, 'CL': 2, 'OP': 10, 'VO': 12}, 'ɐ': {'PA': 6, 'VE': 6, 'CL': 2, 'OP': 10, 'VO': 12}, 'a': {'PA': 12, 'OP': 12, 'VO': 12}, 'á': {'PA': 12, 'OP': 12, 'VO': 12, 'replace_with': 'a'}, 'ā': {'PA': 12, 'OP': 12, 'VO': 12, 'replace_with': 'a'}, 'à': {'PA': 12, 'OP': 12, 'VO': 12, 'replace_with': 'a'},'ɶ': {'LB': 6, 'PA': 6, 'OP': 12, 'VO': 12}, 'ä': {'PA': 6, 'VE': 6, 'OP': 12, 'VO': 12}, 'ɑ': {'VE': 12, 'OP': 12, 'VO': 12}, 'ɒ': {'LB': 6, 'VE': 6, 'OP': 12, 'VO': 12}, 'ɚ': {'AL': 6, 'PA': 3, 'VE': 3, 'CL': 6, 'OP': 6, 'VO': 12}, 'ɝ': {'AL': 6, 'PA': 3, 'VE': 3, 'CL': 4, 'OP': 8, 'VO': 12}}

ignore_set = {'.', 'ˈ', 'ː', '*', '´', '˧', '˩', '˨', '˦', '˥', '1', '2', '/', '(', ')', '⟨', '⟩', ' ',
              u'\u0300', u'\u0320', u'\u0361', u'\u032F', u'\u0301', u'\u0304', u'\u0330' }

modifiers = {'ʲ': {'action': 'add', 'args': ['PA']},
             'ᵝ': {'action': 'add', 'args': ['LB']},
             'ʰ': {'action': 'add', 'args': ['AS']},
             'ʱ': {'action': 'add', 'args': ['AS', 'VO']},
             'ˠ': {'action': 'add', 'args': ['VE']},
             'ʷ': {'action': 'add', 'args': ['LB', 'VE']},
             u'\u0303': {'action': 'add', 'args': ['NA']},
             u'\u0325': {'action': 'devoice', 'args': []},
             u'\u031f': {'action': 'advance', 'args': []},
             u'\u031e': {'action': 'lower', 'args': []},
             u'\u032a': {'action': 'dentalize', 'args': []},
             u'\u0339': {'action': 'half_labialize', 'args': []},
             u'\u02be': {'action': 'half_labialize', 'args': []},
             'ṃ': {'action': 'add', 'args': ['NA'], 'replace_with': u'\u0303'}
             }

coronals = {'DE', 'AL', 'PO', 'RE'}
places = {'LB', 'LD', 'LL', 'DE', 'AL', 'PO', 'RE', 'PA', 'VE', 'UV', 'PH', 'GL'}
manners = {'PL', 'SP', 'VI', 'TA', 'CL', 'OP'}
nasalization = {'NA'}
lateralization = {'LA'}
voiceness = {'VO'}
airflows = {'AS', 'EJ', 'IN'}
features = {'places': places,
            'manners': manners,
            'nasalization': nasalization,
            'lateralization': lateralization,
            'voiceness': voiceness,
            'airflows': airflows}

feature_names = {'LB': 'Labial', 'LD': 'Labiodental', 'LL': 'Labiolingual', 'DE': 'Dental',
                 'AL': 'Alveolar', 'PO': 'Postalveolar', 'RE': 'Retroflex', 'PA': 'Palatal',
                 'VE': 'Velar', 'UV': 'Uvular', 'PH': 'Phalingeal', 'GL': 'Glotal',
                 'PL': 'Plosive', 'SP': 'Fricative', 'VI': 'Vibrant', 'TA': 'Tap',
                 'CL': 'Closed', 'OP': 'Opened', 'NA': 'Nasal', 'LA': 'Lateral',
                 'VO': 'Voiced', 'AS': 'Aspirated', 'EJ': 'Ejective', 'IN': 'Ingressive'}

class IPAString:
    def __init__(self, symbols):
        self.chars = []
        for symbol in symbols:
            if symbol in letters:
                ch = IPAChar(symbol)
                if ch.is_spirant() and len(self.chars) > 0 and self.chars[-1].is_plosive() and len(self.chars[-1].get_modifiers()) == 0 and ch.has_same_place(self.chars[-1]):
                    ch.make_affricate(self.chars[-1].symbol())
                    self.chars[-1] = ch
                else:
                    self.chars.append(ch)
            elif symbol in modifiers or symbol in ignore_set:
                if symbol not in ignore_set and len(self.chars) > 0:
                    method = modifiers[symbol]
                    args = method['args']
                    action = method['action']
                    last_ch = self.chars[-1]
                    if 'replace_with' in method:
                        symbol = method['replace_with']
                    getattr(last_ch, action)(symbol, *args)
            else:
                raise ValueError(f"\033[31m {symbol} \033[0m, context: {symbols}")

    def __str__(self):
        return '\n'.join(str(char) for char in self.chars)

class IPAChar:
    def __init__(self, symbols):
        self.modifiers = []
        self.symbols = symbols
        self.counter = None
        for i, symbol in enumerate(symbols):
            if symbol in letters:
                if 'replace_with' in letters[symbol]:
                    self.symbols = self.symbols[:i] + letters[symbol]['replace_with']
                    features = {feature:letters[symbol][feature] for feature in letters[symbol] if feature != 'replace_with'}
                else:
                    features = letters[symbol]
                self.counter = Counter(features)
            elif symbol in modifiers:
                action = modifiers[symbol]
                if action != 'Ignore':
                    self.modifiers.append(symbol)
                    getattr(self, action)()
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

    def dentalize(self, symbol):
        if self.counter['LB'] > 0:
            self.counter['LD'] += self.counter['LB']
            del self.counter['LB']
        if self.counter['AL'] > 0:
            self.counter['DE'] += self.counter['AL']
            del self.counter['AL']
        if self.counter['PO'] > 0:
            self.counter['DE'] += self.counter['PO']
            del self.counter['PO']
        if self.counter['PO'] > 0:
            self.counter['DE'] += self.counter['PO']
            del self.counter['PO']
        self.symbols += symbol

    def advance(self, symbol):
        if self.counter['LD'] > 0:
            self.counter['LB'] += self.counter['LD']
            del self.counter['LD']
        if self.counter['DE'] > 0:
            self.counter['LL'] += self.counter['DE']/2
            self.counter['DE'] /= 2
        if self.counter['AL'] > 0:
            self.counter['DE'] += self.counter['AL']
            del self.counter['AL']
        if self.counter['PO'] > 0:
            self.counter['AL'] += self.counter['PO']
            del self.counter['PO']
        if self.counter['RE'] > 0:
            self.counter['PO'] += self.counter['RE']
            del self.counter['RE']
        if self.counter['VE'] > 0:
            fraction = 1/2
            if self.counter['CL'] + self.counter['OP'] == 12:
                fraction = 1/4
            self.counter['PA'] += self.counter['VE']*fraction
            self.counter['VE'] -= self.counter['VE']*fraction
        if self.counter['UV'] > 0:
            self.counter['VE'] += self.counter['UV']/2
            self.counter['UV'] /= 2
        if self.counter['PH'] > 0:
            self.counter['UV'] += self.counter['PH']
            del self.counter['PH']
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
        if self.counter['SP'] + self.counter['CL'] == 12:
            self.counter['SP'] -= 3
            self.counter['CL'] += 3
            if self.counter['CL'] > 12:
                self.counter['CL'] = 12
            if self.counter['SP'] < 0:
                self.counter['SP'] = 0
        if self.counter['SP'] + self.counter['VI'] == 12:
            self.counter['SP'] -= 6
            self.counter['VI'] += 6
            if self.counter['VI'] > 12:
                self.counter['VI'] = 12
            if self.counter['SP'] < 0:
                self.counter['SP'] = 0
        if self.counter['PL'] + self.counter['SP'] == 12:
            self.counter['PL'] -= 3
            self.counter['SP'] += 3
            if self.counter['SP'] > 12:
                self.counter['SP'] = 12
            if self.counter['PL'] < 0:
                self.counter['PL'] = 0
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
        return f"\033[34;1m{self.symbols}\033[0m: {self.name()}"

    def symbol(self):
        return self.symbols

    def get_modifiers(self):
        return self.modifiers

    def is_spirant(self):
        return self.counter['SP'] > 8

    def is_plosive(self):
        return self.counter['PL'] > 8

    def coronal(self):
        coronal = 0
        for feature in coronals.intersection(self.counter):
            coronal += self.counter[feature]
        return coronal

    def places(self):
        return places.intersection(self.counter)

    def has_same_place(self, other_ch):
        if self.coronal() >= 3 and other_ch.coronal() >= 3:
            return True
        if len(self.places().intersection(other_ch.places())) > 0:
            return True
        return False
