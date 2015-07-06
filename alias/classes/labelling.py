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

    def is_complete(self):
        complete = True
        if self.undefargs:
            raise LabellingException('Undefined arguments exist: ' )
        for arg in (self.af.get_arguments()):
            if arg in self.inargs:
                if self.af.get_arg_obj(arg).is_illegally_in(self):
                    complete = False
                    break
            if arg in self.outargs:
                if self.af.get_arg_obj(arg).is_illegally_out(self):
                    complete = False
                    break
            if arg in self.undecargs:
                if self.af.get_arg_obj(arg).is_illegally_undec(self):
                    complete = False
                    break

        return complete


class LabellingException(Exception):
    pass
