import alias

def extension_stable(af):
    pref = alias.extension_preferred(af)
    stab = []
    for p in pref:
        if p == af.argsU(p):
            stab.append(p)
    return stab
