import alias as al
import ntpath

def read_dot(path):
    """Generates an alias.ArgumentationFramework from a DOT graph
    description (.dot) file.

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

    """

    try:
        from pyparsing import Word, Literal, alphas, alphanums, nums, OneOrMore
        from pyparsing import Forward, Optional, Keyword, Group, Suppress, ParseException 
    except ImportError:
        raise ImportError("read_dot requires pyparsing")

    if not isinstance(path, str):
        return

    # Define DOT grammar
    # Punctuation and keywords
    LBR,RBR,SCOL,COMMA,EQ,LSQ,RSQ,COL = map(Literal, "{};,=[]:")
    strict,graph,digraph,node,edge,subgraph = map(Keyword, 
        "strict graph digraph node edge subgraph".split())

    # Recursive rules
    stmt_list = Forward()
    a_list = Forward()
    edgeRHS = Forward()
    attr_list = Forward()

    comp = (Literal("n") | Literal("ne") | Literal("e") | Literal("se") | Literal("s") |
    Literal("sw") | Literal("w") | Literal("nw") | Literal("c") | Literal("_")).setName("comp")
    ID = Word(alphas, alphanums).setName("ID")
    edgeop = Suppress(Literal("--") | Literal("->"))
    port = (COL + ID + Optional((COL + comp))) | (COL + comp)
    node_id = ID + Optional(port)
    subg = (subgraph + Optional(ID)) + LBR + stmt_list + RBR

    edgeRHS << OneOrMore(edgeop + (node_id | subg))

    # Statements & attributes
    node_stmt = node_id("arg*") + Optional(attr_list)
    edge_stmt = ((node_id | subg ) + edgeRHS)("att*") + Optional(attr_list)
    attr_stmt = (graph | node | edge) + attr_list

    a_list << OneOrMore(ID + EQ + ID + Optional(SCOL | COMMA))
    attr_list << OneOrMore((LSQ + Optional(a_list) + RSQ))

    stmt = (edge_stmt | node_stmt | attr_stmt | (ID + EQ + ID) | subg)
    stmt_list << OneOrMore(stmt + Optional(SCOL))

    dot = OneOrMore(Optional(strict) + (digraph | graph)("gtype") + Optional(ID)("gname") + LBR + stmt_list + RBR)

    f = open(path, 'r')
    f = f.read()

    try:
        parsed = dot.parseString(f)
    except ParseException, e:
        raise al.ParsingException(e)

    if parsed['gtype'] == 'graph':
        raise al.ParsingException('Graph must be a directed graph (digraph).')

    if 'gname' in parsed.keys():
        framework = al.ArgumentationFramework(parsed['gname'])
    else:
        head, tail = ntpath.split(path)
        framework = al.ArgumentationFramework(tail)

    if 'arg' in parsed.keys():
        for arg in parsed['arg']:
            framework.add_argument(arg)

    if 'att' in parsed.keys():
        for edge in parsed['att']:
            prev = -1
            for curr in edge:
                if prev >= 0:
                    framework.add_attack((edge[prev], curr))
                prev = prev + 1

    return framework

def write_dot(framework, outloc):
    f = open(outloc, 'w')
    f.write('digraph {\n\t')
    for arg in framework.get_arguments():
        f.write(arg + ';\n\t')
    for att in framework.get_attacks():
        f.write(att[0] + ' -> ' + att[1] + '\n\t')

    f.write('}')
    f.close()