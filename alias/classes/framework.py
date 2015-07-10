import alias as al

class ArgumentationFramework(object):

    def __init__(self):
        self.framework = {}
        self.labellings = []

    def __contains__(self, arg):
        return arg in self.framework

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
                    newarg = al.Argument(argumentname)
                    self.framework[argumentname] = newarg
                    for l in self.labellings:
                        l.undefined.add(argumentname)

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
                self.framework[att[0]].attacks.add(att[1])
        
        if atts:
            for a in atts:
                self.add_argument(a[0])
                self.add_argument(a[1])
                self.framework[a[0]].attacks.add(a[1])

    # Returns a list of all the arguments that a given argument attacks
    def get_attacking(self, argument):
        assert self.__contains__(argument)
        return self.framework[argument].attacks

    # Returns a list of all of the attackers of a given argument in the framework
    def get_attackers(self, argument):
        attackers = []
        assert self.__contains__(argument)
        for att in self.get_attacks():
            if att[1] == argument:
                attackers.append(att[0])
        return attackers

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
                attacks.append((arg, target))
        return attacks

    """
    Labelling Creation Methods
    """

    def generate_blank_labelling(self):
        l = al.Labelling(self)
        self.labellings.append(l)
        return l

    def generate_all_in(self):
        l = al.Labelling(self)
        for arg in self.get_arguments():
            l.inargs.add(arg)
            l.undefargs.remove(arg)
        self.labellings.append(l)
        return l

    def generate_all_out(self):
        l = al.Labelling(self)
        for arg in self.get_arguments():
            l.outargs.add(arg)
            l.undefargs.remove(arg)
        self.labellings.append(l)
        return l

    def generate_all_undec(self):
        l = al.Labelling(self)
        for arg in self.get_arguments():
            l.undecargs.add(arg)
            l.undefargs.remove(arg)
        self.labellings.append(l)
        return l

    def generate_grounded(self):
        return al.generate_grounded(self)

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

class FrameworkException(Exception):
    pass
