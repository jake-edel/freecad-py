import sys, json
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint



filePath = 'freecad_saves/sketcher_script001.FCStd'

doc = App.openDocument(filePath)
sketchObj = doc.getObject('Sketch')
sketchConst = sketchObj.Constraints

def collect_constraints():
    constraints = {}

    for constraint in sketchConst:
        if constraint.Name == '':
            continue
        else:
            constraints[constraint.Name] = {
                "value": str(constraint.Value),
                "type": constraint.Type,
                "index": sketchConst.index(constraint),
                "isDriving?": constraint.Driving
            }

    return constraints


constraints = collect_constraints()

pprint(constraints)
json.dump(constraints, open('data/constraints.json', 'w'))



sketchObj.setDatum(constraints['Rise']['index'],App.Units.Quantity('75 mm'))
doc.recompute()



# sketchObj = App.getDocument('sketcher_script001').getObject('Sketch')
App.getDocument('sketcher_script001').saveAs('test_rail.FCStd')

doc = App.openDocument('test_rail.FCStd')
sketchObj = doc.getObject('Sketch')
sketchConst = sketchObj.Constraints

constraints = collect_constraints()
json.dump(constraints, open('data/constraints_new.json', 'w'))