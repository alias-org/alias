import alias as al
import copy

def generate_preferred(af):
    potential_preferred = []

    def transition_step(a, L):
        L.outargs.add(a)
        L.labelling[a] = al.Label.outlabel
        L.inargs.remove(a)
        for arg in L.outargs.copy():
            if L.af.get_arg_obj(arg).is_illegally_out(L):
                L.undecargs.add(arg)
                L.outargs.remove(arg)
                L.labelling[arg] = al.Label.undeclabel

        return L

    def find_preferred(L):
        for Ldash in potential_preferred:
            if L.undecargs < Ldash.undecargs:
                return

        illegal = False
        for arg in L.inargs:
            if L.af.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break

        if not illegal:
            for Ldash in list(potential_preferred):
                if L.inargs < Ldash.inargs:
                    potential_preferred.remove(Ldash)
            potential_preferred.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.af.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_preferred(transition_step(sii.pop(), copy.deepcopy(L)))
            else:
                for arg in L.inargs:
                    if L.af.get_arg_obj(arg).is_illegally_in(L):
                        find_preferred(transition_step(arg, copy.deepcopy(L)))

    find_preferred(af.generate_all_in())
    return potential_preferred