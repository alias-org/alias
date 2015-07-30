import alias as al
import copy

def labelling_semi_stable(af):
    potential_semi_stables = []

    def find_semistables(L):
        for Ldash in potential_stables:
            if Ldash.undecargs < L.undecargs:
                return

        illegal = False
        for arg in L.inargs:
            if L.framework.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            for Ldash in potential_semi_stables.copy():
                if L.undecargs <= Ldash.undecargs:
                    potential_semi_stables.remove(Ldash)
            potential_semi_stables.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_stables(L.transition_step(sii.pop()))
            else:
                for arg in L.inargs:
                    if L.framework.get_arg_obj(arg).is_illegally_in(L):
                        find_stables(L.transition_step(arg))

    find_semi_stables(af.generate_all_in())
    return potential_semi_stables