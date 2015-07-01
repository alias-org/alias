import alias as al

class Argument(object):
    
    def __init__(self, name):
        self.name = name
        self.attacks = set()

    # Determines whether the argument is legally in within a given labelling
    def is_legally_in(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework.")
        if self.name not in labelling.inargs:
            raise al.LabellingException("Argument is not labelled in.")

        allout = True
        for att in labelling.af.get_attackers(self.name):
            if att not in labelling.outargs:
                allout = False
                break
        return allout

    # Determines whether the argument is legally out within a given labelling
    def is_legally_out(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework.")
        if self.name not in labelling.outargs:
            raise al.LabellingException("Argument is not labelled out.")

        onein = False
        for att in labelling.af.get_attackers(self.name):
            if att in labelling.inargs:
                onein = True
                break

        return onein

    # Determines whether the argument is legally undecided within a given labelling
    def is_legally_undec(argument, framework, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework.")
        if labelling[argument] is not Label.undeclabel:
            raise LabelException("Argument is not labelled undecided")

        attackers = framework.get_attackers(argument)
        notallout = False
        notonein = True

class ArgumentException(Exception):
    pass

