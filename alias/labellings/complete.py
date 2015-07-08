import alias as al
import copy

def generate_complete(af):
    potential_completes = []
    
    def transition_step(a, L):
        L.outargs.add(a)
        L.inargs.remove(a)
        for arg in L.outargs.copy():
            if L.af.get_arg_obj(arg).is_illegally_out(L):
                L.undecargs.add(arg)
                L.outargs.remove(arg)
        return L

    def find_completes(L):
        illegal = False
        for arg in L.inargs:
            if L.af.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            if L.is_complete():
                potential_completes.append(L)
                return
        else:
            sii = set()
            for arg in L.inargs:
                if L.af.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_completes(transition_step(sii.pop(), copy.deepcopy(L)))
            else:
                for arg in L.inargs:
                    if L.af.get_arg_obj(arg).is_illegally_in(L):
                        find_completes(transition_step(arg, copy.deepcopy(L)))

    find_completes(af.generate_all_in())
    return potential_completes