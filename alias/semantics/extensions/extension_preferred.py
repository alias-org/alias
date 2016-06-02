import alias

def extension_preferred(af):
    comp = alias.extension_complete(af)
    pref = []
    for c in comp:
        subset = False
        for d in comp:
            if c < d:
                subset = True
        if not subset:
            pref.append(c)

    return pref
