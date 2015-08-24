import alias as al
import copy

def labelling_stable(af):
    potential_stable = []

    def find_stable(L):
        if L.undecargs:
            return

        illegal = False
        for arg in L.inargs:
            if L.framework.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            exists = False
            for Ldash in potential_stable:
                if L == Ldash:
                    exists = True
                    break
            if not exists:
                potential_stable.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_stable(L.transition_step(sii.pop()))
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_illegally_in(L):
                    find_stable(L.transition_step(arg))

    find_stable(af.generate_all_in())
    return potential_stable