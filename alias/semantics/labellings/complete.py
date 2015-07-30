import alias as al
import copy

def labelling_complete(af):
    potential_complete = []

    def find_complete(L):
        illegal = False
        for arg in L.inargs:
            if L.framework.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            potential_complete.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_complete(L.transition_step(sii.pop()))
            else:
                for arg in L.inargs:
                    if L.framework.get_arg_obj(arg).is_illegally_in(L):
                        find_complete(L.transition_step(arg))

    find_complete(af.generate_all_in())
    return potential_complete