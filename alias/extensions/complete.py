import alias as al

def complete_labellings(framework):
	def transition_step(l, x):
		l1 = l.copy()
		l1[x] = al.Label.outlabel
		for a in l1:
			if l[a] is al.Label.outlabel:
				if al.is_illegally_out(a, f, l):
					l[x] = al.Label.undeclabel
