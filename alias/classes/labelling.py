import alias as al
from copy import deepcopy

class Labelling(object):

    def __init__(self, af):
        self.af = af
        self.inargs = set()
        self.outargs = set()
        self.undecargs = set()
        self.undefargs = set()
        for arg in af.get_arguments():
        	self.undefargs.add(arg)

    def label_in(self, arg):
        if arg in self.inargs:
            return
        elif arg in self.outargs:
            self.outargs.remove(arg)
            self.inargs.add(arg)
        elif arg in self.undecargs:
            self.undecargs.remove(arg)
            self.inargs.add(arg)
        elif arg in self.undefargs:
            self.undefargs.remove(arg)
            self.inargs.add(arg)
        else:
            raise LabellingException('Argument not present in labelling')

    def label_out(self, arg):
        if arg in self.inargs:
            self.inargs.remove(arg)
            self.outargs.add(arg)
        elif arg in self.outargs:
            return
        elif arg in self.undecargs:
            self.undecargs.remove(arg)
            self.outargs.add(arg)
        elif arg in self.undefargs:
            self.undefargs.remove(arg)
            self.outargs.add(arg)
        else:
            raise LabellingException('Argument not present in labelling')

    def label_undec(self, arg):
        if arg in self.inargs:
            self.inargs.remove(arg)
            self.undecargs.add(arg)
        elif arg in self.outargs:
            self.outargs.remove(arg)
            self.undecargs.add(arg)
        elif arg in self.undecargs:
            return
        elif arg in self.undefargs:
            self.undefargs.remove(arg)
            self.undecargs.add(arg)
        else:
            raise LabellingException('Argument not present in labelling')

    def label_undefined(self,arg):
        if arg in self.inargs:
            self.inargs.remove(arg)
            self.undefargs.add(arg)
        elif arg in self.outargs:
            self.outargs.remove(arg)
            self.undefargs.add(arg)
        elif arg in self.undecargs:
            self.undecargs.remove(arg)
            self.undefargs.add(arg)
        elif arg in self.undefargs:
            return
        else:
            raise LabellingException('Argument not present in labelling')

    def lab2ext(self):
        return self.inargs

    def transition_step(self, x):
        l = deepcopy(self)
        l.label_out(x)
        for arg in self.outargs:
            if l.af.get_arg_obj(arg).is_illegally_out(l):
                l.label_undec(arg)
        return l

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
