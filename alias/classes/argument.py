import alias as al

class Argument(object):
    
    def __init__(self, name, framework):
        self.name = name
        self.framework = framework
        self.attacks = set()
        self.attacksref = set()

    def __repr__(self):
        return '\'' + self.name + '\''

    def __str__(self):
        string = 'Argument \'' + self.name + '\' : ['
        atts = []
        for att in self.attacks:
            atts.append('\'' + att.name + '\'')
        string = string + (', '.join(atts))
        string = string + ']'
        return string

    def __iter__(self):
        for arg in self.attacks:
            yield arg

    def __getitem__(self,arg):
        if arg in self.attacks:
            return self.framework[arg]
        else:
            raise al.FrameworkException('Argument \'%s\' is not attacked by argument \'%s\'' %(arg, self.name))

    # Determines whether the argument is legally in within a given labelling
    def is_legally_in(self, labelling):
        if not (labelling.framework.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.inargs:
            raise al.LabellingException("Argument is not labelled in.")
        allout = True
        for att in labelling.framework.get_attackers(self.name):
            if att in labelling.inargs:
                allout = False
                break
            if att in labelling.undecargs:
                allout = False
                break
        return allout

    # Determines whether the argument is legally out within a given labelling
    def is_legally_out(self, labelling):
        if not (labelling.framework.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.outargs:
            raise al.LabellingException("Argument is not labelled out.")

        onein = False
        for att in labelling.framework.get_attackers(self.name):
            if att in labelling.inargs:
                onein = True
                break

        return onein

    # Determines whether the argument is legally undecided within a given labelling
    def is_legally_undec(self, labelling):
        if not (labelling.framework.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.undecargs:
            raise al.LabellingException("Argument is not labelled undecided.")

        allout = True
        onein = False

        for att in labelling.framework.get_attackers(self.name):
            if att not in labelling.outargs:
                allout = False
            if att in labelling.inargs:
                onein = True
                break

        return not (allout | onein)

    def is_illegally_in(self, labelling):
        return not self.is_legally_in(labelling)

    def is_illegally_out(self, labelling):
        return not self.is_legally_out(labelling)

    def is_illegally_undec(self, labelling):
        return not self.is_legally_undec(labelling)

    def is_super_illegally_in(self, labelling):
        if not (labelling.framework.argument_exists(self.name)):
            raise ArgumentException("Argument does not exist in this framework/labelling.")
        if self.name not in labelling.inargs:
            raise al.LabellingException("Argument is not labelled in.")

        sii = False
        if self.is_illegally_in(labelling):
            for att in labelling.framework.get_attackers(self.name):
                if att in labelling.inargs:
                    if labelling.framework.get_arg_obj(att).is_legally_in(labelling):
                        sii = True
                        break
                if att in labelling.undecargs:
                    if labelling.framework.framework[att].is_legally_undec(labelling):
                        sii = True
                        break

        return sii 
