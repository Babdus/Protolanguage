from IPA.IPAChar import IPAChar
from IPA.IPAData import letters, modifiers, ignore_set

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
