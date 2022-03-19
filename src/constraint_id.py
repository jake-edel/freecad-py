import sys, json
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint


class ConstraintManager:

    def __init__(self, filePath):
        self.open_doc(filePath)

    def open_doc(self, filePath):
        self.doc = App.openDocument(filePath)
        self.sketchObj = self.doc.getObject('Sketch')
        self.constraints = self.collect_constraints()

    def print_constraints(self):
        pprint(self.constraints)

    def set_constraint(self, name, value):
        self.sketchObj.setDatum(self.constraints[name]['index'],App.Units.Quantity(value))
        self.doc.recompute()
        self.constraints = self.collect_constraints()

    def save_constraints(self, filePath):
        json.dump(self.constraints, open(filePath, 'w'))

    def save_doc(self, filePath):
        self.doc.saveAs(filePath)

    def collect_constraints(self):
        sketchConst = self.sketchObj.Constraints
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