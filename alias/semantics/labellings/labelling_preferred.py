import alias
import copy

def labelling_preferred(af):
    potential_preferreds = []

    def find_preferreds(L):
        for Ldash in potential_preferreds:
            if Ldash.inargs >= L.inargs:
                return

        illegal = False
        for arg in L.inargs:
            if L.framework.get_arg_obj(arg).is_illegally_in(L):
                illegal = True
                break
        if not illegal:
            for Ldash in potential_preferreds:
                if L.inargs >= Ldash.inargs:
                    potential_preferreds.remove(Ldash)
            potential_preferreds.append(L)
            return
        else:
            sii = set()
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_super_illegally_in(L):
                    sii.add(arg)
            if sii:
                find_preferreds(L.transition_step(sii.pop()))
            for arg in L.inargs:
                if L.framework.get_arg_obj(arg).is_illegally_in(L):
                    find_preferreds(L.transition_step(arg))

    find_preferreds(af.generate_all_in())
    return potential_preferreds
