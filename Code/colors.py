from random import randrange, choice

def color(text, color=39, bg=49, lighter=False, lighter_bg=False,
            bold=False, dim=False, underline=False, italic=False,
            inverted=False, stroke=False):
    base = f'\033['
    color += 60 if lighter else 0
    bg += 60 if lighter_bg else 0
    base += f'{color};{bg}'
    base += f';{1}' if bold else ''
    base += f';{2}' if dim else ''
    base += f';{3}' if italic else ''
    base += f';{4}' if underline else ''
    base += f';{7}' if inverted else ''
    base += f';{9}' if stroke else ''
    base += f'm{text}\033[0m'
    return base

def black(text, **kw_args):
    return color(text, color=30, **kw_args)

def red(text, **kw_args):
    return color(text, color=31, **kw_args)

def green(text, **kw_args):
    return color(text, color=32, **kw_args)

def yellow(text, **kw_args):
    return color(text, color=33, **kw_args)

def blue(text, **kw_args):
    return color(text, color=34, **kw_args)

def magenta(text, **kw_args):
    return color(text, color=35, **kw_args)

def cyan(text, **kw_args):
    return color(text, color=36, **kw_args)

def white(text, **kw_args):
    return color(text, color=37, **kw_args)

def random_color(text, **kw_args):
    return color(text, color=randrange(30, 38), lighter=choice((True, False)), **kw_args)
