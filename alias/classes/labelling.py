import alias as al
from enum import Enum

class Label(Enum):
    inlabel = 1
    outlabel = -1
    undeclabel = 0
    undefined = None

class Labelling(object):

    def __init__(self, af):
        self.af = af
        self.labelling = {arg : al.Label.undefined for arg in af.get_arguments()}
        self.inargs = set()
        self.outargs = set()
        self.undecargs = set()
        self.undefargs = set()
        for arg in af.get_arguments():
        	self.undefargs.add(arg)

class LabellingException(Exception):
    pass
