import alias as al
import copy

def generate_stables(af):
    potential_stables = []

    def transition_step(a, L):
        L.outargs.add(a)
        L.inargs.remove(a)
        for arg in L.outargs.copy():
            if L.af.get_arg_obj(arg).is_illegally_out(L):
                L.undecargs.add(arg)
                L.outargs.remove(arg)
        return L

    def find_stables(L):
        for Ldash in potential_stables:
            if Ldash.undecargs:
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
                find_stables(transition_step(sii.pop(), copy.deepcopy(L)))
            else:
                for arg in L.inargs:
                    if L.af.get_arg_obj(arg).is_illegally_in(L):
                        find_stables(transition_step(arg, copy.deepcopy(L)))

    find_stables(af.generate_all_in())
    return potential_stables