from collections import Counter

letters = {'p': {'LB': 12, 'PL': 12}, 'b': {'LB': 12, 'PL': 12, 'VO': 12}, 't': {'AL': 12, 'PL': 12}, 'd': {'AL': 12, 'PL': 12, 'VO': 12}, 'ʈ': {'RE': 12, 'PL': 12}, 'ɖ': {'RE': 12, 'PL': 12, 'VO': 12}, 'c': {'PA': 12, 'PL': 12}, 'ɟ': {'PA': 12, 'PL': 12, 'VO': 12}, 'k': {'VE': 12, 'PL': 12}, 'g': {'VE': 12, 'PL': 12, 'VO': 12}, 'ɡ': {'VE': 12, 'PL': 12, 'VO': 12}, 'q': {'UV': 12, 'PL': 12}, 'ɢ': {'UV': 12, 'PL': 12, 'VO': 12}, 'ʡ': {'PH': 12, 'PL': 12}, 'ʔ': {'GL': 12, 'PL': 12}, 'm': {'LB': 12, 'NA': 12, 'VO': 12}, 'ɱ': {'LD': 12, 'NA': 12, 'VO': 12}, 'n': {'AL': 12, 'NA': 12, 'VO': 12}, 'ɳ': {'RE': 12, 'NA': 12, 'VO': 12}, 'ɲ': {'PA': 12, 'NA': 12, 'VO': 12}, 'ñ': {'PA': 12, 'NA': 12, 'VO': 12}, 'ŋ': {'VE': 12, 'NA': 12, 'VO': 12}, 'ɴ': {'UV': 12, 'NA': 12, 'VO': 12}, 'ʙ': {'LB': 12, 'VI': 12, 'VO': 12}, 'r': {'AL': 12, 'VI': 12, 'VO': 12}, 'ʀ': {'UV': 12, 'VI': 12, 'VO': 12}, 'ʜ': {'PH': 12, 'VI': 12}, 'ʢ': {'PH': 12, 'VI': 12, 'VO': 12}, 'ⱱ': {'LD': 12, 'TA': 12, 'VO': 12}, 'ɾ': {'AL': 12, 'TA': 12, 'VO': 12}, 'ɽ': {'RE': 12, 'TA': 12, 'VO': 12}, 'ɸ': {'LB': 12, 'SP': 12}, 'β': {'LB': 12, 'SP': 12, 'VO': 12}, 'f': {'LD': 12, 'SP': 12}, 'v': {'LD': 12, 'SP': 12, 'VO': 12}, 'θ': {'DE': 12, 'SP': 12}, 'ð': {'DE': 12, 'SP': 12, 'VO': 12}, 's': {'AL': 12, 'SP': 12}, 'z': {'AL': 12, 'SP': 12, 'VO': 12}, 'ʃ': {'PO': 12, 'SP': 12}, 'ʒ': {'PO': 12, 'SP': 12, 'VO': 12}, 'ʂ': {'RE': 12, 'SP': 12}, 'ʐ': {'RE': 12, 'SP': 12, 'VO': 12}, 'ç': {'PA': 12, 'SP': 12}, 'ʝ': {'PA': 12, 'SP': 12, 'VO': 12}, 'x': {'VE': 12, 'SP': 12}, 'ɣ': {'VE': 12, 'SP': 12, 'VO': 12}, 'χ': {'UV': 12, 'SP': 12}, 'ʁ': {'UV': 12, 'SP': 12, 'VO': 12}, 'ħ': {'PH': 12, 'SP': 12}, 'ʕ': {'PH': 12, 'SP': 9, 'CL': 3, 'VO': 12}, 'h': {'GL': 12, 'SP': 9, 'CL': 3}, 'ɦ': {'GL': 12, 'SP': 9, 'CL': 3, 'VO': 12}, 'ɬ': {'AL': 12, 'SP': 12, 'LA': 12}, 'ɮ': {'AL': 12, 'SP': 12, 'LA': 12, 'VO': 12}, 'ʋ': {'LD': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɹ': {'AL': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɻ': {'RE': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'j': {'PA': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɰ': {'VE': 12, 'SP': 6, 'CL': 6, 'VO': 12}, 'l': {'AL': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ɭ': {'RE': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ʎ': {'PA': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ʟ': {'VE': 12, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ʘ': {'LB': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǀ': {'DE': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǃ': {'AL': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, '‼': {'RE': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǂ': {'PA': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ʞ': {'VE': 12, 'PL': 12, 'EJ': 6, 'IN': 6}, 'ǁ': {'PL': 12, 'LA': 12, 'EJ': 6, 'IN': 6}, 'ɓ': {'LB': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ɗ': {'AL': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ᶑ': {'RE': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ʄ': {'PA': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ɠ': {'VE': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ʛ': {'UV': 12, 'PL': 12, 'VO': 12, 'IN': 12}, 'ʍ': {'LB': 6, 'VE': 6, 'SP': 6, 'CL': 6, 'VO': 12}, 'w': {'LB': 6, 'VE': 6, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɥ': {'LB': 6, 'PA': 6, 'SP': 6, 'CL': 6, 'VO': 12}, 'ɫ': {'AL': 6, 'VE': 6, 'SP': 6, 'CL': 6, 'LA': 12, 'VO': 12}, 'ɺ': {'AL': 12, 'TA': 12, 'LA': 12, 'VO': 12}, 'ɕ': {'AL': 6, 'PA': 6, 'SP': 12}, 'ʑ': {'AL': 6, 'PA': 6, 'SP': 12, 'VO': 12}, 'ɧ': {'PO': 6, 'VE': 6, 'SP': 12}, 'i': {'PA': 12, 'CL': 12, 'VO': 12}, 'y': {'LB': 6, 'PA': 6, 'CL': 12, 'VO': 12}, 'ɨ': {'PA': 6, 'VE': 6, 'CL': 12, 'VO': 12}, 'ʉ': {'LB': 6, 'PA': 3, 'VE': 3, 'CL': 12, 'VO': 12}, 'ɯ': {'VE': 12, 'CL': 12, 'VO': 12}, 'u': {'LB': 6, 'VE': 6, 'CL': 12, 'VO': 12}, 'ɪ': {'PA': 8, 'VE': 4, 'CL': 10, 'OP': 2, 'VO': 12}, 'ʏ': {'LB': 6, 'PA': 4, 'VE': 2, 'CL': 10, 'OP': 2, 'VO': 12}, 'ʊ': {'LB': 6, 'PA': 2, 'VE': 4, 'CL': 10, 'OP': 2, 'VO': 12}, 'e': {'PA': 12, 'CL': 8, 'OP': 4, 'VO': 12}, 'ø': {'LB': 6, 'PA': 6, 'CL': 8, 'OP': 4, 'VO': 12}, 'ɘ': {'PA': 6, 'VE': 6, 'CL': 8, 'OP': 4, 'VO': 12}, 'ɵ': {'LB': 6, 'PA': 3, 'VE': 3, 'CL': 8, 'OP': 4, 'VO': 12}, 'ɤ': {'VE': 12, 'CL': 8, 'OP': 4, 'VO': 12}, 'o': {'LB': 6, 'VE': 6, 'CL': 8, 'OP': 4, 'VO': 12}, 'ə': {'PA': 6, 'VE': 6, 'CL': 6, 'OP': 6, 'VO': 12}, 'ɛ': {'PA': 12, 'CL': 4, 'OP': 8, 'VO': 12}, 'œ': {'LB': 6, 'PA': 6, 'CL': 4, 'OP': 8, 'VO': 12}, 'ɜ': {'PA': 6, 'VE': 6, 'CL': 4, 'OP': 8, 'VO': 12}, 'ɞ': {'LB': 6, 'PA': 3, 'VE': 3, 'CL': 4, 'OP': 8, 'VO': 12}, 'ʌ': {'VE': 12, 'CL': 4, 'OP': 8, 'VO': 12}, 'ɔ': {'LB': 6, 'VE': 6, 'CL': 4, 'OP': 8, 'VO': 12}, 'æ': {'PA': 12, 'CL': 2, 'OP': 10, 'VO': 12}, 'ɐ': {'PA': 6, 'VE': 6, 'CL': 2, 'OP': 10, 'VO': 12}, 'a': {'PA': 12, 'OP': 12, 'VO': 12}, 'ɶ': {'LB': 6, 'PA': 6, 'OP': 12, 'VO': 12}, 'ä': {'PA': 6, 'VE': 6, 'OP': 12, 'VO': 12}, 'ɑ': {'VE': 12, 'OP': 12, 'VO': 12}, 'ɒ': {'LB': 6, 'VE': 6, 'OP': 12, 'VO': 12}, 'ɚ': {'AL': 6, 'PA': 3, 'VE': 3, 'CL': 6, 'OP': 6, 'VO': 12}, 'ɝ': {'AL': 6, 'PA': 3, 'VE': 3, 'CL': 4, 'OP': 8, 'VO': 12}}

modifiers = {'.': 'Ignore',
             'ʲ': {'action': 'add', 'args': ['PA']},
             'ˈ': 'Ignore',
             'ː': 'Ignore',
             '*': 'Ignore',
             '˩': 'Ignore',
             '˧': 'Ignore',
             '˨': 'Ignore',
             u'\u0300': 'Ignore',
             u'\u0320': 'Ignore',
             u'\u0361': 'Ignore',
             '/': 'Ignore',
             '(': 'Ignore',
             ')': 'Ignore',
             u'\u0303': {'action': 'add', 'args': ['NA']},
             'ᵝ': {'action': 'add', 'args': ['LB']},
             'ʰ': {'action': 'add', 'args': ['AS']},
             u'\u0325': {'action': 'devoice', 'args': []},
             'ṃ': {'action': 'add', 'args': ['NA']}
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
            elif symbol in modifiers:
                method = modifiers[symbol]
                if method != 'Ignore' and len(self.chars) > 0:
                    args = method['args']
                    action = method['action']
                    last_ch = self.chars[-1]
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
        for symbol in symbols:
            if symbol in letters:
                self.counter = Counter(letters[symbol])
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
                    for feature in value:
                        whole = True
                        if feature in self.counter:
                            self.counter[feature] /= 2
                            whole = False
                    self.counter[arg] += 12 if whole else 6
        self.symbols += symbol

    def devoice(self, symbol):
        self.counter['VO'] = 0
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
