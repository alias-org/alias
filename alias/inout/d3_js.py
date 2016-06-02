import alias
import json

class D3Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, alias.ArgumentationFramework):
            args = {}
            arglist = []
            attlist = []
            jid = 0
            for arg in o.framework.values():
                args[arg.name] = jid
                arglist.append({"name": arg.name, "id": jid})
                jid = jid + 1

            for att in o.get_attacks():
                attlist.append({"ref": att, "source": args[att[0]], "target": args[att[1]]})

            encoded = {"name": o.name, "directed": "true", "nodes": arglist, "links": attlist}
            return encoded
        return json.JSONEncoder.default(self, o)

def write_d3js(obj, path=None):
    if path:
        f = open(path, 'w')
        json.dump(obj, f, cls=D3Encoder, sort_keys=False, indent=4, separators=(',', ': '))
    else:
        json.dump(obj, cls=JsEncoder, sort_keys=False, indent=4, separators=(',', ': '))

def read_d3js(path):
    f = open(path, 'r')
    decoded = json.loads(f.read())
    af=alias.ArgumentationFramework(decoded['name'])
    for arg in decoded['nodes']:
        af.add_argument(arg)
    for att in decoded['edges']:
        af.add_attack((att['source'], att['target']))
