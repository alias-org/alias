import alias as al
import copy

def labelling_stable(af):
    potential_stables = []

    def find_stables(L):
        if L.undecargs:
            return

        illegal = False
        for arg in L.inargs:
            if L.af.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            potential_stables.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.af.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_stables(L.transition_step(sii.pop()))
            else:
                for arg in L.inargs:
                    if L.af.get_arg_obj(arg).is_illegally_in(L):
                        find_stables(L.transition_step(arg))

    find_stables(af.generate_all_in())
    return potential_stables