import alias

def labelling_grounded(af):
    l = af.generate_blank_labelling()

    for arg in af.get_arguments():
        if not af.get_attackers(arg):
            l.undefargs.remove(arg)
            l.inargs.add(arg)

    iterate = True

    while iterate:
        iterate = False
        for arg in l.undefargs.copy():
            for att in af.get_attackers(arg):
                if att in l.inargs:
                    l.outargs.add(arg)
                    l.undefargs.remove(arg)
                    iterate = True
                    break

        for arg in l.undefargs.copy():
            allout = True
            for att in af.get_attackers(arg):
                if att not in l.outargs:
                    allout = False
                    break

            if allout:
                l.inargs.add(arg)
                l.undefargs.remove(arg)
                iterate = True

    for arg in l.undefargs.copy():
        l.undecargs.add(arg)
        l.undefargs.remove(arg)

    return l
