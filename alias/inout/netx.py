import alias

def to_networkx(af):
    try:
        import networkx as nx
    except ImportError:
        raise ImportError("Networkx required for to_networkx()")

    n = nx.DiGraph()
    for arg in af.get_arguments():
        n.add_node(arg)

    for att in af.get_attacks():
        n.add_edge(att[0], att[1])

    return n

def from_networkx(n):
    try:
        import networkx as nx
    except ImportError:
        raise ImportError("Networkx required for from_networkx()")

    try:
        assert isinstance(n, nx.DiGraph)
    except AssertionError:
        raise AssertionError("Input must be NetworkX DiGraph()")

    af = alias.ArgumentationFramework()

    for node in n.nodes():
        af.add_argument(node)

    for edge in n.edges():
        af.add_attack(edge)

    return af
