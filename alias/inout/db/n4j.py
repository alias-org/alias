import alias

def n4j_connect(dbaddress=None, port=None, u='', p=''):
    try:
        from py2neo import Graph
    except ImportError:
        raise ImportError("py2neo is required for n4j_connect()")

    if dbaddress:
        if port:
            graph_db = Graph('http://' + u + ':' + p + '@' + dbaddress + ':' + str(port) + '/db/data/')
        else:
            graph_db = Graph('http://' + u + ':' + p + '@' + dbaddress + ':7474' + '/db/data/')
    else:
        if port:
            graph_db = Graph('http://' + u + ':' + p + '@' + 'localhost' + ':' + port + '/db/data/')
        else:
            graph_db = Graph('http://' + u + ':' + p + '@localhost:7474' + '/db/data/')

    return graph_db

def to_neo4j(af, dbaddress='localhost', port=None, u='', p=''):
    try:
        from py2neo import Graph
    except ImportError:
        raise ImportError("py2neo is required for to_neo4j()")

    graph_db = n4j_connect(dbaddress, port, u, p)

    tx = graph_db.cypher.begin()
    nodestmt = "MERGE (n:Argument {name:{N}, framework:{O}})"
    relstmt = "MATCH (a:Argument { name: {A}}),(b:Argument { name: {B}}) MERGE (a)-[r:Attacks]->(b)"

    def add_args(args):
        for arg in args:
            tx.append(nodestmt, {"N": arg, "O" : af.name})
        tx.process()

    def add_atts(atts):
        for att in atts:
            tx.append(relstmt, {"A": att[0], "B" : att[1]})
        tx.process()

    add_args(af.get_arguments())
    add_atts(af.get_attacks())
    tx.commit()
    print 'Write to Neo4J Database Successful'

def from_neo4j(framework, dbaddress='localhost', port=None, u='', p=''):
    try:
        from py2neo import Graph
    except ImportError:
        raise ImportError("py2neo is required for from_neo4j()")

    af = alias.ArgumentationFramework(name = framework)

    graph_db = n4j_connect(dbaddress, port, u, p)
    argstmt = "MATCH (n:Argument) WHERE n.framework=\"" + framework + "\" RETURN n.name"
    attstmt = "MATCH (a:Argument)-->(b:Argument) WHERE a.framework = \"" + framework + "\" AND b.framework = \"" + framework +"\" RETURN a.name, b.name"

    nodes = []

    for r in graph_db.cypher.stream(argstmt):
        nodes.append(r[0])
        af.add_argument(r[0])

    for r in graph_db.cypher.stream(attstmt):
        af.add_attack((r[0],r[1]))

    return af
