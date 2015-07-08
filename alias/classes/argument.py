import alias as al

class Argument(object):
    
    def __init__(self, name):
        self.name = name
        self.attacks = set()

    # Determines whether the argument is legally in within a given labelling
    def is_legally_in(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.inargs:
            raise al.LabellingException("Argument is not labelled in.")

        allout = True
        for att in labelling.af.get_attackers(self.name):
            if att in labelling.inargs:
                allout = False
                break
        return allout

    # Determines whether the argument is legally out within a given labelling
    def is_legally_out(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.outargs:
            raise al.LabellingException("Argument is not labelled out.")

        onein = False
        for att in labelling.af.get_attackers(self.name):
            if att in labelling.inargs:
                onein = True
                break

        return onein

    # Determines whether the argument is legally undecided within a given labelling
    def is_legally_undec(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.undecargs:
            raise al.LabellingException("Argument is not labelled undecided.")

        notallout = False
        notonein = True

        for att in labelling.af.get_attackers(self.name):
            if att in labelling.inargs:
                notonein = False
                break
            if att in labelling.undecargs:
                notallout = True

        return (notallout & notonein)

    def is_illegally_in(self, labelling):
        return not self.is_legally_in(labelling)

    def is_illegally_out(self, labelling):
        return not self.is_legally_out(labelling)

    def is_illegally_undec(self, labelling):
        return not self.is_legally_undec(labelling)

    def is_super_illegally_in(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.inargs:
            raise al.LabellingException("Argument is not labelled in.")

        sii = False

        for att in labelling.af.get_attackers(self.name):
            if att in labelling.inlabel is al.Label.inlabel:
                if labelling.af.framework[att].is_legally_in(labelling):
                    sii = True
                    break

        return sii 

class ArgumentException(Exception):
    pass

