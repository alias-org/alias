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

    # Add an argument to the AF, takes the argument's name as input.  If the argument already exists, break
    def add_argument(self, argumentname):
        if self.__contains__(argumentname):
            return
        else:
            newarg = al.Argument(argumentname)
            self.framework[argumentname] = newarg
            for l in self.labellings:
                l.undefined.add(argumentname)

    # Adds an attack to the AF, if the attacker or target do not exist, add them to the AF
    def add_attack(self, attacker, target):
        self.add_argument(attacker)
        self.add_argument(target)
        self.framework[attacker].attacks.add(target)

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
            l.labelling[arg] = al.Label.inlabel
        self.labellings.append(l)
        return l

    def generate_all_out(self):
        l = al.Labelling(self)
        for arg in self.get_arguments():
            l.labelling[arg] = al.Label.outlabel
        self.labellings.append(l)
        return l

    def generate_all_undecided(self):
        l = al.Labelling(self)
        for arg in self.get_arguments():
            l.labelling[arg] = al.Label.undeclabel
        self.labellings.append(l)
        return l

    def generate_power_labelling(self):
        labellings = []
        l = self.generate_all_in()
        labellings.append(l)
        return l

    def generate_grounded(self):
        return al.generate_grounded(self)