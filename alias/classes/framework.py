import alias
import sys
from itertools import product

class ArgumentationFramework(object):

    def __init__(self, name=""):
        self.name = name
        self.framework = {}
        self.labellings = []

    def __contains__(self, arg):
        return arg in self.framework

    def __str__(self):
        com = ', '
        if self.name != '':
            string = 'ArgumentationFramework \'%s\' : {' %self.name
        else:
            string = '{ '
        argcount = 0
        for arg in self.get_arguments():
            argcount = argcount + 1
            atts = []
            for a in self.framework[arg].attacks:
                atts.append(('\'' + a.name + '\''))
            atts = com.join(atts)
            string = string + ('\'' + arg + '\'' + ' : [' + atts)
            if argcount < (len(self.get_arguments())):
                string = string + ('], ')
            else:
                string = string + (']')
        string = string + ('}')
        return string

    def __len__(self):
        return len(self.framework)

    def __iter__(self):
        return iter(self.framework)

    def __getitem__(self, arg):
        return self.framework[arg]

    # Return a list of all arguments in the AF
    def get_arguments(self):
        return self.framework.keys()

    def get_arg_obj(self, argref):
        return self.framework[argref]

    # Return a list of all attack tuples in the AF
    def get_attacks(self):
        return self.__generate_attacks()

    def arg_in(self, arg):
        return a in self.framework

    # Add an argument to the AF, takes the argument's name as input.  If the argument already exists, break
    def add_argument(self, args):
        def add(argumentname):
            if not isinstance(argumentname, basestring):
                raise FrameworkException('Only string based argument name references can be added to a framework')
            else:
                if self.__contains__(argumentname):
                    return
                else:
                    newarg = alias.Argument(argumentname, self)
                    self.framework[argumentname] = newarg
                    for l in self.labellings:
                        l.undefargs.add(argumentname)

        if isinstance(args, basestring):
            add(args)
        else:
            for arg in args:
                add(arg)


    # Adds an attack to the AF, if the attacker or target do not exist, add them to the AF
    def add_attack(self, att = (None, None), atts = None):
        if att[0]:
            if att[1]:
                self.add_argument(att[0])
                self.add_argument(att[1])
                self.framework[att[0]].add_attack(self.framework[att[1]])

        if atts:
            for a in atts:
                self.add_argument(a[0])
                self.add_argument(a[1])
                self.framework[a[0]].add_attack(self.framework[a[1]])

    def remove_argument(self, args):
        def remove(argumentname):
            if not isinstance(argumentname, basestring):
                raise FrameworkException('Only string based argument name references can be removed from a framework')
            else:
                if not self.__contains__(argumentname):
                    return
                else:
                    del self.framework[argumentname]
                    for l in self.labellings:
                        if argumentname in l.inargs:
                            l.inargs.remove(argumentname)
                        elif argumentname in l.outargs:
                            l.outargs.remove(argumentname)
                        elif argumentname in l.undecargs:
                            l.undecargs.remove(argumentname)
                        elif argumentname in l.undefargs:
                            l.undefargs.remove(argumentname)

        if isinstance(args, basestring):
            remove(args)
        else:
            for arg in args:
                add(arg)

    def remove_attack(self, att=(None, None), atts=None):
        def remove(a):
            if a in self.get_attacks():
                self.framework[a[0]].remove_attack(a[1])
            else:
                raise alias.FrameworkException('Attack %s does not exist in the framework' %str(a))

        if att[0]:
            if att[1]:
                remove(att)

        if atts:
            for a in atts:
                remove(a)

    def clear(self):
        self.name = ''
        self.framework.clear()
        self.labellings.clear()

    # Returns a list of all the arguments that a given argument attacks
    def get_attacking(self, argument):
        assert self.__contains__(argument)
        attacks = set()
        for att in self.framework[argument].attacks:
            attacks.add(att.name)
        return attacks

    # Returns a list of all of the attackers of a given argument in the framework
    def get_attackers(self, argument):
        attackers = []
        assert self.__contains__(argument)
        for att in self.get_attacks():
            if att[1] == argument:
                attackers.append(att[0])
        return set(attackers)

    def argument_exists(self, argument):
        return argument in self.framework

    def num_arguments(self):
        return len(self.framework)

    def num_attacks(self):
        return len(self.get_attacks())

    def __generate_attacks(self):
        attacks = []
        for arg in self.get_arguments():
            for target in self.framework[arg].attacks:
                attacks.append((arg, target.name))
        return attacks

    """
    Labelling Creation Methods
    """

    def generate_power_labelling(self):
        args = self.get_arguments()
        labellings = []
        for i in product([0,1,2], repeat=len(args)):
            l = alias.Labelling(self)
            j = 0
            while j < len(args):
                if i[j] == 0:
                    l.label_out(args[j])
                if i[j] == 1:
                    l.label_in(args[j])
                if i[j] == 2:
                    l.label_undec(args[j])
                j = j + 1
            labellings.append(l)
        return labellings

    def generate_blank_labelling(self):
        l = alias.Labelling(self)
        self.labellings.append(l)
        return l

    def generate_all_in(self):
        l = alias.Labelling(self, name='All-In')
        for arg in self.get_arguments():
            l.inargs.add(arg)
            l.undefargs.remove(arg)
        self.labellings.append(l)
        return l

    def generate_all_out(self):
        l = alias.Labelling(self)
        for arg in self.get_arguments():
            l.outargs.add(arg)
            l.undefargs.remove(arg)
        self.labellings.append(l)
        return l

    def generate_all_undec(self):
        l = alias.Labelling(self)
        for arg in self.get_arguments():
            l.undecargs.add(arg)
            l.undefargs.remove(arg)
        self.labellings.append(l)
        return l

    def generate_grounded(self):
        return alias.generate_grounded(self)

    """
    Set Creation Methods
    """
    # Returns a list of sets containing all possible combinations of arguments within the framework
    # Adapted from example at: http://rosettacode.org/wiki/Power_set
    def generate_powerset(self):
        def list_powerset(lst):
            return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])

        return frozenset(map(frozenset, list_powerset(list(self.get_arguments()))))

    def argsP(self, sargs):
        attacked = set()
        for arg in sargs:
            attacked.update(self.get_attacking(arg))
        return attacked

    def argsM(self, sargs):
        attackers = set()
        for arg in sargs:
            attackers.update(self.get_attackers(arg))
        return attackers

    def argsD(self, sargs):
        defended = set()
        for arg in self.get_arguments():
            attackers = self.get_attackers(arg)
            defen = True
            for att in attackers:
                if att not in self.argsP(sargs):
                    defen = False
                    break
            if defen:
                defended.add(arg)
        return defended

    def argsU(self,sargs):
        return (set(self.get_arguments()) - self.argsP(sargs))

    """
    Set Semantic Methods
    """
    # Given a set of arguments within the framework - determines whether that set of arguments is conflict-free
    def is_conflict_free(self, sargs):
        if self.argsP(sargs).intersection(sargs):
            return False
        return True

    def is_admissible(self, sargs):
        if self.is_conflict_free(sargs):
            if self.argsM(sargs):
                if self.argsP(sargs) >= self.argsM(sargs):
                    return True
                else:
                    return False
            else:
                return True
        return False

    def is_complete(self, sargs):
        if self.is_admissible(sargs):
            allin = True
            for arg in self.argsD(sargs):
                if arg not in sargs:
                    allin = False
                    break
            return allin
        else:
            return False
