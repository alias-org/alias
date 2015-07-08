import alias as al
"""
Argument Utilities
"""

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