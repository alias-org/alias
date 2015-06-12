import alias as al
from enum import Enum

class ArgumentationFramework(object):

    def __init__(self):
        self.framework = {}
        self.labellings = {}

    def __contains__(self, arg):
        return arg in self.framework

    # Return a list of all arguments in the AF
    def get_arguments(self):
        return self.framework.keys()

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

    # Adds an attack to the AF, if the attacker or target do not exist, add them to the AF
    def add_attack(self, attacker, target):
        self.add_argument(attacker)
        self.add_argument(target)
        self.framework[attacker].attacks.append(target)

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

    def __generate_attacks(self):
        attacks = []
        for arg in self.get_arguments():
            for target in self.framework[arg].attacks:
                attacks.append((arg, target))
        return attacks

"""
class _Labelling(object):
    def __init__(self):
        self.inargs = []
        self.outargs = []
        self.undecargs = []

    def __str__(self):
        string = '{\'in\': ' + str(self.inargs) + ', ' + '\'out\': ' + str(self.outargs) + ', ' + '\'undec\': ' + str(self.undecargs) + '}'
        return string   
"""