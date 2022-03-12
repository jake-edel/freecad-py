import sys, math
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import Part
import Sketcher


class Sketch:
    def __init__(self):
        self.doc = self.create_doc()
        self.sketch = self.create_sketch()

    def create_doc(self):
        return App.newDocument("sketcher script")

    def save_doc(self):
        self.doc.recompute
        self.doc.saveAs(u"/home/jakobedel/code/freecad-py/freecad_saves/test_doc.FCStd")
        print("Sketch saved sucessfully")

    def create_sketch(self):
        return self.doc.addObject("Sketcher::SketchObject", "Sketch")

    def add_line(self, v1, v2):
        self.sketch.addGeometry(Part.LineSegment(v1, v2))

    # def add_constraint(self, type, line1, line2, pt1, pt2):
    #     sketch.addConstraint(Sketcher.Constraint(type, line1, line2, pt1, pt2))

postHeight = 36
materialWidth = 1.5
railAngle = 0
mitreAngle = abs(railAngle - 90) / 2
negMitreAngle = mitreAngle * -1


def find_oppisite(angle, adj):
    return math.tan(math.radians(angle)) * adj

def short_leg(height, angle, adj):
    return height - find_oppisite(angle, adj)

origin = App.Vector(0, 0, 0)
originWidth = App.Vector(materialWidth, 0, 0)

longPt = App.Vector(0, postHeight, 0)
shortPt = App.Vector(materialWidth, short_leg(postHeight, mitreAngle, materialWidth), 0)


sketch = Sketch()

# Lines
base = sketch.add_line(origin, originWidth)
sketch.add_line(origin, longPt)
sketch.add_line(longPt, shortPt)
sketch.add_line(originWidth, shortPt)

sketch.sketch.addConstraint(Sketcher.Constraint("Horizontal", 0))
sketch.sketch.addConstraint(Sketcher.Constraint("Vertical", 1))
sketch.sketch.addConstraint(Sketcher.Constraint("Parallel", 1, 3))
# sketch.sketch.addConstraint(Sketcher.Constraint("Angle", 2, 45.0))

# sketch.sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 1, 1))

sketch.save_doc()