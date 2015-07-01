import alias as al

def transition_step(l, a, framework):
    l[a] = al.Label.outlabel
    for arg in l.keys():
        if l[arg] is al.Label.outlabel:
            if al.is_illegally_out(arg, framework, l):
                l[arg] = al.Label.undeclabel

def term_trans_sequence(l, framework):
    terminate = True
    for arg in l.keys():
        if l[arg] is al.Label.inlabel:
            if al.is_illegally_in(arg, framework, l):
                terminate = False
                break
    return terminate

def preferred_labellings(framework):
    candidatelabellings = []

    def find_labellings(labelling):
        def si():
            si = set()
            for arg in labelling.keys():
                if labelling[arg] is al.Label.inlabel:
                    if al.is_super_illegally_in(arg, framework, labelling):
                        si.add(arg)

            return si

        for l in candidatelabellings:
            if al.in_args(labelling) < al.in_args(l):
                return

        if term_trans_sequence(labelling, framework):
            for l in candidatelabellings:
                if al.in_args(l) < al.in_args(labelling):
                    candidatelabellings.remove(l)

            candidatelabellings.append(labelling)
            return
        else:
            si = si()
            if si:
                x = si.pop()
                transition_step(labelling, x, framework)
                find_labellings(labelling)
            else:
                for arg in labelling.keys():
                    if labelling[arg] is al.Label.inlabel:
                        if al.is_illegally_in(arg, framework, labelling):
                            transition_step(labelling, arg, framework)
                            find_labellings(labelling)

    
    find_labellings(al.all_in(framework))
    return candidatelabellings