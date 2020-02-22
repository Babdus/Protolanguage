from IPA.IPAChar import IPAChar
from IPA.IPAData import replace_with, letters, modifiers, ignore_set

class IPAString:
    def __init__(self, symbols, create_from_char_array=False):
        self.chars = []
        if create_from_char_array:
            self.chars = symbols
            return
        for symbol in symbols:
            if symbol in replace_with:
                symbol = replace_with[symbol]
            if symbol in letters:
                ch = IPAChar(symbol, printing=False)
                if ch.is_spirant() and len(self.chars) > 0 and self.chars[-1].is_plosive() and not self.chars[-1].has_modifiers() and self.chars[-1].has_same_place(ch) and self.chars[-1].has_same_voice(ch):
                    self.chars[-1].make_affricate(ch)
                else:
                    self.chars.append(ch)
            elif symbol in modifiers or symbol in ignore_set:
                if symbol not in ignore_set and len(self.chars) > 0:
                    method = modifiers[symbol]
                    args = method['args']
                    action = method['action']
                    last_ch = self.chars[-1]
                    getattr(last_ch, action)(symbol, *args)
                    last_ch.modifiers.add(symbol)
            else:
                raise ValueError(f"\033[31m {symbol} \033[0m, context: {symbols}")

    def to_ipa(self):
        return ''.join(char.symbols for char in self.chars)

    def __str__(self):
        return '\n'.join(str(char) for char in self.chars)

    def __len__(self):
        return len(self.chars)

    def __repr__(self):
        return self.__str__()
