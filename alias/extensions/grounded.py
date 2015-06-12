import alias as al

# Implementation of Dung's grounded labelling framework extension semantics.
# Takes an AF as input and returns the framework with the semantics implemented and arguments labelled.
def grounded_labelling(framework):
    newlabel = True
    arguments = framework.get_arguments()
    inargs = []
    outargs = []

    while(newlabel == True):
        newlabel = False

        for arg in arguments:
            if len(framework.get_attackers(arg)) == 0:
                if ((arg.label is None) or (arg.label == al.Label.outlabel)):
                    arg.label = al.Label.inlabel
                    inargs.append(arg.name)
                    newlabel = True

        for arg in arguments:
            for att in framework.get_attackers(arg):
                if (att.name in inargs):
                    if ((arg.label is None) or (arg.label == al.Label.inlabel)):
                        arg.label = al.Label.outlabel
                        outargs.append(arg.name)
                        newlabel = True

        for arg in arguments:
            allout = True
            for att in framework.get_attackers(arg):
                if (att.name not in outargs):
                    allout = False

            if allout == True:
                if ((arg.label is None) or (arg.label == al.Label.outlabel)):
                    arg.label = al.Label.inlabel
                    inargs.append(arg.name)
                    newlabel = True

    for arg in arguments:
        if arg.label is None:
            arg.label = al.Label.undeclabel

    newframework = al.ArgumentationFramework()

    for arg in arguments:
    	newframework.add_argument(arg.name)
   	
   	for att in framework.get_attacks():
   		newframework.add_attack(att[0].name, att[1].name)

   	return newframework 