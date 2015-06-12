import alias as al

def preffered_labellings(framework):
	def all_in(framework):
		allin = al.generate_labelling(framework)
		for arg in allin.keys():
			allin[arg] = al.Label.inlabel
		return allin

	def transition_step(l, x):
		l[arg] = Label.outlabel
		for a in l.keys():
			if is_illegally_out(a, framework, l):
				l[a] = label.undeclabel

	candidates = []
	candidates.append(all_in(framework))

	for arg in candidates[0].keys():
		if al.is_illegally_in(arg, framework, candidates[0]):
			print arg
			# transition_step(candidates[0], arg)

	return 

