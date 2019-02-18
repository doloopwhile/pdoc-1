import json

import pdoc


def module_to_json(m: pdoc.Module) -> str:
    obj = {
        "functions":  [_function(x)  for x in m.functions()],
        "variables":  [_variable(x)  for x in m.variables()],
        "classes":    [_class(x)     for x in m.classes()],
        "submodules": [{"name": x.name} for x in m.submodules()],
    }
    return json.dumps(obj)

def _function(f: pdoc.Function):
    return {
        "name": f.name,
        "params": f.params(),
        "docstring": f.docstring
    }


def _variable(v: pdoc.Variable):
    return {
        "name": v.name,
        "docstring": v.docstring
    }


def _class(c: pdoc.Class):
    return {
        "class_variables":    [_variable(v) for v in c.class_variables()],
        "static_methods":     [_function(f) for f in c.functions()],
        "instance_variables": [_variable(v) for v in c.instance_variables()],
        "methods":            [_function(f) for f in c.methods()],
        "mro":                [{"name": x.refname} for x in c.mro()],
        "subclasses":         [{"name": x.refname} for x in c.subclasses()],
    }
