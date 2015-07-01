import alias as al

class Labelling(object):

	def __init__(self, af):
		self.af = af
		self.inargs = set()
		self.outargs = set()
		self.undecargs = set()
		self.undefined = set()

class LabellingException(Exception):
	pass
