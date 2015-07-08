import alias as al
import copy

def generate_semi_stables(af):
	potential_semi_stables = []

	def transition_step(a, L):
        L.outargs.add(a)
        L.inargs.remove(a)
        for arg in L.outargs.copy():
            if L.af.get_arg_obj(arg).is_illegally_out(L):
                L.undecargs.add(arg)
                L.outargs.remove(arg)
        return L

	def find_semistables(L):
		for Ldash in potential_stables:
			if Ldash.undecargs <= L.undecargs:
				return

		illegal = False
		for arg in L.inargs:
			if L.af.get_arg_obj(arg).is_illegally_in(L):
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
				if L.af.get_arg_obj(arg).is_super_illegally_in(L):
					sii.add(arg)
			if sii:
				find_semi_stables(transition_step(sii.pop(), copy.deepcopy(L)))
			else:
				for arg in L.inargs:
					if L.af.get_arg_obj(arg).is_illegally_in(L):
						find_semi_stables(transition_step(arg, copy.deepcopy(L)))

	find_semi_stables(af.generate_all_in())
	return potential_semi_stables