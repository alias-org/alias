import alias as al

def labelling_admissible(af):
    admissible = []

    def find_admissible(L):
        illegal = False
        for arg in L.inargs:
            if L.framework[arg].is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            exists = False
            for l in admissible:
                if L == l:
                    exists = True
            if not exists:
                admissible.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                arg = sii.pop()
                find_admissible(L.transition_step(arg))
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_illegally_in(L):
                    find_admissible(L.transition_step(arg))
                        
    find_admissible(af.generate_all_in())
    # Add the all-undec labelling
    admissible.append(af.generate_all_undec())
    return admissible