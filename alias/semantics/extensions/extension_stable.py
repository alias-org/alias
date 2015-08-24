import alias as al

def extension_stable(af):
    pref = al.extension_preferred(af)
    stab = []
    for p in pref:
        if p == af.argsU(p):
            stab.append(p)
    return stab