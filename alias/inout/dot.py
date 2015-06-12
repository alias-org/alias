from pyparsing import Word, Literal, alphas, alphanums, nums, OneOrMore, Suppress
from pyparsing import Forward, Optional, Keyword, Group

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
        from pyparsing import Forward, Optional, Keyword, Group, Suppress 
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
    edge_stmt = ((node_id | subg ) + edgeRHS)("attack*") + Optional(attr_list)
    attr_stmt = (graph | node | edge) + attr_list

    a_list << OneOrMore(ID + EQ + ID + Optional(SCOL | COMMA))
    attr_list << OneOrMore((LSQ + Optional(a_list) + RSQ))

    stmt = (edge_stmt | node_stmt | attr_stmt | (ID + EQ + ID) | subg)
    stmt_list << OneOrMore(stmt + Optional(SCOL))

    dot = Optional(strict) + (graph | digraph) + Optional(ID) + LBR + stmt_list + RBR

    framework = al.ArgumentationFramework()
    f = open(path, 'r')
    f.read()

    try:
        parsed = dot.parseString(f)
    except ParseException:
        raise ParseException()

    for arg in parsed['arg']:
        framework.add_argument(arg)

    for att in parsed['attack']:
        framework.add_attack(att[0], att[1])

def dot_out(framework, outloc):
    """
    TODO
    """





