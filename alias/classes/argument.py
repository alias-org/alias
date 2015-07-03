import alias as al

class Argument(object):
    
    def __init__(self, name):
        self.name = name
        self.attacks = set()

    # Determines whether the argument is legally in within a given labelling
    def is_legally_in(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if labelling.labelling[self.name] is not al.Label.inlabel:
            raise al.LabellingException("Argument is not labelled in.")

        allout = True
        for att in labelling.af.get_attackers(self.name):
            if labelling.labelling[att] is al.Label.inlabel:
                allout = False
                break
        return allout

    # Determines whether the argument is legally out within a given labelling
    def is_legally_out(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if labelling.labelling[self.name] is not al.Label.outlabel:
            raise al.LabellingException("Argument is not labelled out.")

        onein = False
        for att in labelling.af.get_attackers(self.name):
            if labelling.labelling[att] is al.Label.inlabel:
                onein = True
                break

        return onein

    # Determines whether the argument is legally undecided within a given labelling
    def is_legally_undec(self, labelling):
        if not (labelling.af.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if labelling.labelling[self.name] is not al.Label.undeclabel:
            raise al.LabellingException("Argument is not labelled undecided.")

        notallout = False
        notonein = True

        for arg in labelling.af.get_attackers(self.name):
            if labelling[att] is al.Label.inlabel:
                notonein = False
                break
            if labelling[att] is al.Label.undeclabel:
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
        if labelling.labelling[self.name] is not al.Label.inlabel:
            raise al.LabellingException("Argument is not labelled in.")

        sii = False

        for att in labelling.af.get_attackers(self.name):
            if labelling.labelling[att] is al.Label.inlabel:
                if labelling.af.framework[att].is_legally_in(labelling):
                    sii = True
                    break

        return sii 

class ArgumentException(Exception):
    pass

