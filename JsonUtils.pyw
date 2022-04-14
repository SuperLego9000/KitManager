import json
def write(what,where):
    what=what
    clear(where)
    with open(where, 'w') as f:
        json.dump(what, f)
    return True
def clear(what):
    with open(what,'w') as cleared:cleared.close()
    return True
def read(read):
    with open(read,'r') as f:
        return json.load(f)