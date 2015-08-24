import alias as alias

def extension_complete(af):
    comp = []
    for s in af.generate_powerset():
        if af.is_complete(s):
            comp.append(s)
    return comp