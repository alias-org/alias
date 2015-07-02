import alias as al

def generate_stables(af):
	potential_stables = []
	allin = af.generate_all_in()

	def transition_step(a, L):
		L.outargs.add(a)
		L.inargs.remove(a)
		for arg in L.outargs.copy():
			if L.af.get_arg_obj(arg).is_illegally_out(L):
				L.undecargs.add(arg)
				L.outargs.remove(arg)

	def find_stables(L):
		if L.undecargs:
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
				transition_step(sii.pop(), L)
				find_stables(L)
			else:
				for arg in L.inargs.copy():
					if arg in L.inargs:
						if L.af.get_arg_obj(arg).is_illegally_in(L):
							transition_step(arg, L)
							find_stables(L)

	find_stables(allin)
	return potential_stables