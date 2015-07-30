import alias as al
import copy

def labelling_preferred(af):
    potential_preferred = []

    def find_preferred(L):
        for Ldash in potential_preferred:
            if L.inargs < Ldash.inargs:
                return
        illegal = False
        for arg in L.inargs:
            if L.framework.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            for Ldash in potential_preferred:
                if Ldash.inargs < L.inargs:
                    potential_preferred.remove(Ldash)
            potential_preferred.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_preferred(L.transition_step(sii.pop()))
            else:
                for arg in L.inargs:
                    if L.framework.get_arg_obj(arg).is_illegally_in(L):
                        find_preferred(L.transition_step(arg))

    find_preferred(af.generate_all_in())
    return potential_preferred