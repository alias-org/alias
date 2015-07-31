import json
import alias as al

class JsEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, al.ArgumentationFramework):
            arglist = []
            for arg in o.framework.values():
                arglist.append({"name" : arg.name, "attacks" : list(arg.attacksref)})
            encoded = {"name" : o.name, "arguments": arglist}
            return encoded
        if isinstance(o, al.Argument):
            encoded = {"name" : o.name, "attacks" : list(o.attacksref)}
            return encoded
        return json.JSONEncoder.default(self, o)

def write_json(obj, path=None):
    if path:
    	f = open(path, 'w')
    	json.dump(obj, f, cls=JsEncoder, sort_keys=False, indent=4, separators=(',', ': '))
    else:
    	print json.dump(obj, cls=JsEncoder, sort_keys=False, indent=4, separators=(',', ': '))

def read_json(path):
    f = open(path, 'r')
    decoded = json.loads(f.read())
    af = al.ArgumentationFramework(decoded['name'])
    for arg in decoded['arguments']:
        af.add_argument(arg['name'])
        for att in arg['attacks']:
            af.add_attack((arg['name'], att))
    return af