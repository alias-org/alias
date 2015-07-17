import alias as al
import copy

def generate_labellings_complete(af):
    potential_completes = []

    def find_completes(L):

        sii = set()
        for arg in L.inargs:
            if L.af.get_arg_obj(arg).is_super_illegally_in(L):
                sii.add(arg)
        if sii:
            find_completes(L.transition_step(sii.pop))
        else:
            for arg in L.inargs:
                if L.af.get_arg_obj(arg).is_illegally_in(L):
                    find_completes(L.transition_step(arg))

    find_completes(af.generate_all_in())
    return potential_completes