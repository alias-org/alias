import alias as al

def labelling_complete(af):
    complete = []

    def find_complete(L):
        illegal = False
        for arg in L.inargs:
            if L.framework[arg].is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            undec = False
            for arg in L.undecargs:
                if L.framework[arg].is_illegally_undec(L):
                    undec = True
                    break
            if undec:
                return
            else:
                exists = False
                for l in complete:
                    if L == l:
                        exists = True
                if not exists:
                    complete.append(L)
                return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                arg = sii.pop()
                find_complete(L.transition_step(arg))
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_illegally_in(L):
                    find_complete(L.transition_step(arg))
                        
    find_complete(af.generate_all_in())
    # Consider the all-undec labelling
    undec = False
    undeclab = af.generate_all_undec()
    for arg in undeclab.undecargs:
        if undeclab.framework[arg].is_illegally_undec(undeclab):
                    undec = True
                    break
    if not undec:
        complete.append(undeclab)
    return complete