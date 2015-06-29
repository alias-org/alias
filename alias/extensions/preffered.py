import alias as al

def preffered_labellings(framework):
    allin = al.all_in(framework)

    def transition_step(l, x):
        l[x] = al.Label.outlabel
        for arg in l.keys():
            if l[arg] is al.Label.outlabel:
                if al.is_illegally_out(arg, framework, l):
                    l[arg] = al.Label.undeclabel

    candidates = []
    candidates.append(allin)

    for l in candidates:
        for arg in l.keys():
            if l[arg] is al.Label.inlabel:
                if al.is_illegally_in(arg, framework, l):
                    transition_step(l, arg)