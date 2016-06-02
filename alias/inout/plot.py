import alias

def draw_framework(af, labelling=None):
    """
    Utilises NetworkXs draw fucntionality to produce a matplotlib of the framework
    """

    try:
        import networkx as nx
    except ImportError:
        raise ImportError("Networkx required for draw_framework()")

    try:
        import matplotlib.pyplot as plt
        import numpy
    except ImportError:
        raise ImportError("Matplotlib required for draw_framework")

    n = alias.to_networkx(af)

    if labelling:
        colors = ['g'] * len(labelling.inargs) + ['r'] * len(labelling.outargs) + ['y'] * len(labelling.undecargs)
        nl = list(labelling.inargs)
        nl.extend(list(labelling.outargs))
        nl.extend(list(labelling.undecargs))
        nx.draw_networkx(n,with_labels=True, nodelist=nl, node_color=colors)
    else:
        nx.draw_networkx(n,with_labels=True)
