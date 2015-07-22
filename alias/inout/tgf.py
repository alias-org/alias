import alias as al
import ntpath

def read_tgf(path):
    """Generates an alias.ArgumentationFramework from a Trivial Graph Format (.tgf) file.

    Trivial Graph Format (TGF) is a simple text-based file format for describing graphs. \
    It consists of a list of node definitions, which map node IDs to labels, followed by \
    a list of edges, which specify node pairs and an optional edge label. \
    Node IDs can be arbitrary identifiers, whereas labels for both nodes and edges are plain strings.

    Parameters
    ----------
    path : file or string
        File, directory or filename to be read.

    Returns
    -------
    framework : alias ArgumentationFramework

    Examples
    --------

    References
    ----------
    http://en.wikipedia.org/wiki/Trivial_Graph_Format 
    """

    try:
        from pyparsing import Word, alphanums, ZeroOrMore, White, Suppress, Group, ParseException, Optional
    except ImportError:
        raise ImportError("read_tgf requires pyparsing")

    if not isinstance(path, str):
        return

    # Define tgf grammar
    s = White(" ")
    tag = Word(alphanums)
    arg = Word(alphanums)
    att = Group(arg + Suppress(s) + arg + Optional(Suppress(s) + tag))
    nl = Suppress(White("\n"))

    graph = Group(ZeroOrMore(arg + nl)) + Suppress("#") + nl + Group(ZeroOrMore(att + nl) + ZeroOrMore(att))
    
    
    f = open(path, 'r')
    f = f.read()

    head, tail = ntpath.split(path)
    framework = al.ArgumentationFramework(tail)

    try:
        parsed = graph.parseString(f)
    except ParseException, e:
        raise al.ParsingException(e)

    for arg in parsed[0]:
        framework.add_argument(arg)

    for att in parsed[1]:
        framework.add_attack((att[0], att[1]))

    return framework

def write_tgf(framework, outloc):
    """Outputs a Trivial Graph Format (.tgf) file from an alias.ArgumentationFramework.

    Trivial Graph Format (TGF) is a simple text-based file format for describing graphs. \
    It consists of a list of node definitions, which map node IDs to labels, followed by \
    a list of edges, which specify node pairs and an optional edge label. \
    Node IDs can be arbitrary identifiers, whereas labels for both nodes and edges are plain strings.

    Parameters
    ----------
    framework :
        alias ArgumentationFramework
    outloc : string
        Directory location for file to be written to.

    Returns
    -------
    

    Examples
    --------

    References
    ----------
    http://en.wikipedia.org/wiki/Trivial_Graph_Format 
    """
    f = open(outloc, 'w')

    for arg in framework.get_arguments():
        f.write(arg + "\n")
    f.write("#\n")
    for att in framework.get_attacks():
        f.write(att[0] + " " + att[1] + "\n")
    f.close()
