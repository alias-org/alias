import alias as al
from enum import Enum
from sets import Set

"""
Labelling Utilities
"""
# Defines a label
class Label(Enum):
    outlabel = -1
    undeclabel = 0
    inlabel = 1

# Defines a new label exception to raise if wrong argument method is called
class LabelException(Exception):
    pass

# Given an argumentation framework, generate a blank labelling dictionary and return it
def generate_labelling(framework):
    labelling = {}
    for arg in framework.get_arguments():
        labelling[arg] = None
    
    return labelling

# Given an argumentation framework, generate a labelling where all arguements are labelled in
def all_in(framework):
    allin = {}
    for arg in framework.get_arguments():
        allin[arg] = al.Label.inlabel

    return allin

# Given an argumentation framework, generate and return
# a labelling where all arguements are labelled out
def all_out(framework):
    allout = {}
    for arg in framework.get_arguments():
        allout[arg] = al.Label.outlabel

    return allout

# Given an argumentation framework, generate and return
# a labelling where all arguements are labelled in
def all_undec(framework):
    allundec = {}
    for arg in framework.get_arguments():
        undec[arg] = al.Label.undeclabel 

    return allundec

# Given a labelling, return the set of all in-labelled arguments
def in_args(labelling):
    inargs = set()
    for arg, label in labelling.iteritems():
        if label is al.Label.inlabel:
            inargs.add(arg)
    return inargs

# Given a labelling, return the set of all out-labelled arguments
def out_args(labelling):
    outargs = set()
    for arg, label in labelling.iteritems():
        if label is al.Label.outlabel:
            outargs.add(arg)
    return outargs

# Given a labelling, return the set of all undecided-labelled arguments
def undec_args(labelling):
    undecargs = set()
    for arg, label in labelling.iteritems():
        if label is al.Label.undeclabel:
            undecards.add(arg)
    return undecargs

# Returns a list of all possible labellings for a given framework
def power_labelling(framework):
    """TODO"""

"""
Argument Utilities
"""
# Determines whether a given argument is legally in within a given labelling
def is_legally_in(argument, framework, labelling):
    if labelling[argument] is not Label.inlabel:
        raise LabelException("Argument is not labelled IN")

    attackers = framework.get_attackers(argument)
    allout = True

    for att in attackers:
        if labelling[att] is not Label.outlabel:
            allout = False
            break
    if allout:
        return True
    else:
        return False

# Determines whether a given argument is legally out within a given labelling
def is_legally_out(argument, framework, labelling):
    if labelling[argument] is not Label.outlabel:
        raise LabelException("Argument is not labelled OUT")

    attackers = framework.get_attackers(argument)
    onein = False

    for att in attackers:
        if labelling[att] is Label.inlabel:
            onein = True
            break
    
    return onein

# Determines whether a given argument is legally undecided within a given labelling
def is_legally_undec(argument, framework, labelling):
    if labelling[argument] is not Label.undeclabel:
        raise LabelException("Argument is not labelled UNDECIDED")

    attackers = framework.get_attackers(argument)
    notallout = False
    notonein = True

    for att in attackers:
        if labelling[att] is Label.inlabel:
            notonein = False
            break
        if labelling[att] is Label.undeclabel:
            notallout = True

    return (notallout & notonein)

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