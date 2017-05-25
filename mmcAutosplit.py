def rmBlank(setta):
    while 1:
        try:
            del setta[setta.index('')]
        except ValueError:
            break
    return setta

def split(setta,splita):
    macro = [ x for x in setta]
    for n in splita:
        nacro = []
        for m in macro:
            nacro.extend(m.split(n))
        macro = [ x for x in nacro]
    return macro

def bindNote(setta,keyta):
    setta = rmBlank(setta)
    macro = [ x for x in setta]
    for n in keyta:
        while n in macro:
            for m in macro:
                if m == n:
                    a = macro.index(m)
                    macro[a] = macro[a]+macro[a+1]
                    del macro[a+1]
    return macro
