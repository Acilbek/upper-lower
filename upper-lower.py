uppers = {
    'a':'A',
    'b':'B',
    'c':'C',
    'd':'D',
    'e':'E',
    'f':'F',
    'g':'G',
    'h':'H',
    'i':'I',
    'j':'J',
    'k':'K',
    'l':'L',
    'm':'M',
    'n':'N',
    'o':'O',
    'p':'P',
    'q':'Q',
    'r':'R',
    's':'S',
    't':'T',
    'u':'U',
    'v':'V',
    'w':'W',
    'x':'X',
    'y':'Y',
    'z':'Z'
    }

lowers = {}

for key, value in uppers.items():
    lowers[value] = key

def tp_upper(a):
    for i in a:
        if i in uppers.keys():
            a = a.replace(i, uppers[i])
    return a

def to_lower(b):
    for i in b:
        if i in lowers.keys():
            b = b.replace(i, lowers[i])
    return b
