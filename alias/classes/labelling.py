import alias as al
from copy import deepcopy

class Labelling(object):

    def __init__(self, framework, name=''):
        self.framework = framework
        self.name = name
        self.inargs = set()
        self.outargs = set()
        self.undecargs = set()
        self.undefargs = set()

        for arg in self.framework.get_arguments():
        	self.undefargs.add(arg)

    def __str__(self):
        string = 'Labelling \'%s\' : {in : [' %self.name

        if self.inargs:
            argcount = 0
            for arg in self.inargs:
                if argcount < (len(self.inargs) - 1):
                    string = string + '\'%s\', ' %arg
                else:
                    string = string + '\'%s\']' %arg
                argcount = argcount + 1
        else:
            string = string + ']'

        string = string + ' out : ['
        if self.outargs:
            argcount = 0
            for arg in self.outargs:
                if argcount < (len(self.outargs) - 1):
                    string = string + '\'%s\', ' %arg
                else:
                    string = string + '\'%s\']' %arg
                argcount = argcount + 1
        else:
            string = string + ']'

        string = string + ' undecided : ['
        if self.undecargs:
            argcount = 0
            for arg in self.undecargs:
                if argcount < (len(self.undecargs) - 1):
                    string = string + '\'%s\', ' %arg
                else:
                    string = string + '\'%s\']' %arg
                argcount = argcount + 1
        else:
            string = string + ']'

        string = string + ' undefined : ['
        if self.undefargs:
            argcount = 0
            for arg in self.undefargs:
                if argcount < (len(self.undefargs) - 1):
                    string = string + '\'%s\', ' %arg
                else:
                    string = string + '\'%s\']' %arg
                argcount = argcount + 1
        else:
            string = string + ']'

        string = string + '}'
        return string

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
