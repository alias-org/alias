import alias as al
"""
Argument Utilities
"""
# Determines whether a given argument is illegally in within a given labelling
def is_illegally_in(argument, framework, labelling):
    if labelling[argument] is not Label.inlabel:
        raise LabelException("Argument is not labelled IN")
    return not is_legally_in(argument, framework, labelling)

# Determines whether a given argument is illegally out within a given labelling
def is_illegally_out(argument, framework, labelling):
    if labelling[argument] is not Label.outlabel:
        raise LabelException("Argument is not labelled OUT")
    return not is_legally_out(argument, framework, labelling)

# Determines whether a given argument is illegally undecided within a given labelling
def is_illegally_undec(argument, framework, labelling):
    if labelling[argument] is not Label.undeclabel:
        raise LabelException("Argument is not labelled UNDECIDED")
    return not is_legally_undec(argument, framework, labelling)

# Determines whether a given argument is super-illegaly in for a given labelling
def is_super_illegally_in(argument, framework, labelling):
    if labelling[argument] is not Label.inlabel:
        raise LabelException("Argument is not labelled IN")

    attackers = framework.get_attackers(argument)
    sii = False

    for att in attackers:
        if labelling[att] is Label.inlabel:
            if is_legally_in(att, framework, labelling):
                sii = True
                break
    return sii

# Determines whether a given labelling is an admissible labelling
def is_admissible(framework, labelling):
    admissible = True
    for arg, l in labelling.iteritems():
        if l is Label.inlabel:
            if is_illegally_in(arg, framework, labelling):
                admissible = False
                break
        if l is Label.outlabel:
            if is_illegally_out(arg, framework, labelling):
                admissible = False
                break
    return admissible

# Determines whether a given set of arguments is conflict free
def is_conflict_free(argset, framework, labelling):
    conflictfree = True
    for arg in argset:
        if labelling[arg] is Label.inlabel:
            labelledin = False
            for att in framework.get_attackers(arg):
                if labelling[att] is Label.inlabel:
                    labelledin = True
                    break
            if labelledin == True:
                conflictfree = False
        if not conflictfree:
            break

        onelabelledin = False
        if labelling[arg] is Label.outlabel:
            for att in framework.get_attackers(arg):
                if labelling[att] is Label.inlabel:
                    onelabelledin = True
                    break

        if not onelabelledin:
            conflictfree = False
            break

    return conflictfree

"""
Set Utilities
"""

# Returns the power set of a given framework
def powerset(framework):
    powerset = [[]]
    for arg in framework.get_arguments():
        powerset.extend([subset + [arg] for subset in powerset])
    return powerset

# Returns a list of all possible labellings of a given framework - recursive function
def powerlabelling(framework, labellings):
    l = all_undec(framework)