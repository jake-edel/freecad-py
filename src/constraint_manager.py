import sys, json, math
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

    def set_distance_constraint(self, name, value):
        self.sketchObj.setDatum(self.constraints[name]['index'], App.Units.Quantity(str(value) + ' mm'))
        self.doc.recompute()
        self.constraints = self.collect_constraints()

    def set_angle_constraint(self, name, value):
        if math.degrees(float(value)) == 90:
            return
    
        self.sketchObj.setDatum(self.constraints[name]['index'], App.Units.Quantity(str(math.degrees(float(value))) + ' deg'))
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

    def generate_part_names(self):
        partNames = []

        for constraint in self.constraints:
            firstLetter = constraint.split("_")[0][0]
            if firstLetter.islower() and constraint.split("_")[0] not in partNames:
                partNames.append(constraint.split("_")[0])

        json.dump(partNames, open('./data/parts/partlist.json', 'w'))