import alias as al

class Labelling(object):

	def __init__(self, af):
		self.af = af
		self.inargs = set()
		self.outargs = set()
		self.undecargs = set()
		self.undefined = set()

	def is_complete():
		complete = True
		for arg in self.inargs:
			if self.af.get_arg_obj(arg).is_illegally_in:
				return False
		for arg in self.outargs:
			if self.af.get_arg_obj(arg).is_illegally_out:
				return False
		for arg in self.undecargs:
			if self.af.get_arg_obj(arg).is_illegally_undec:
				return False
class LabellingException(Exception):
	pass
