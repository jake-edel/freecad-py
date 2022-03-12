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
        self.doc.saveAs(u"/home/jakobedel/code/freecad-py/freecad_saves/sketcher_script.FCStd")
        print("Sketch saved sucessfully")

    def create_sketch(self):
        return self.doc.addObject("Sketcher::SketchObject", "Sketch")

    def add_line(self, v1, v2):
        self.sketch.addGeometry(Part.LineSegment(v1, v2))


## Math Helper Functions

# Find oppisite leg given angle and adjacent leg
def find_oppisite(angle, adj):
    opp = round(math.tan(math.radians(angle)) * adj, 3)
    print("Opposite Leg = " + str(opp))
    return round(math.tan(math.radians(angle)) * adj, 3)

# Find short leg of post
def short_leg(height, angle, adj):
    return height - find_oppisite(angle, adj)

# Calculate Rail Angle
def rail_angle(rise, run):
    angle = round(math.degrees(math.atan(rise/run)), 3)
    print("Rail Angle = " + str(angle))
    return math.degrees(math.atan(rise/run))

# Calculate miter angle
def mitre_angle(angle):
   return abs(angle - 90) / 2


postHeight = 36
materialWidth = 1.5
rise = 3
run = 4
railAngle = rail_angle(rise, run)
mitreAngle = mitre_angle(railAngle)
negMitreAngle = mitreAngle * -1


## Bottom Post
### Points
# Base
origin = App.Vector(0, 0, 0)


originWidth = App.Vector(materialWidth, 0, 0)

longPt = App.Vector(0, postHeight, 0)
shortPt = App.Vector(materialWidth, short_leg(postHeight, mitreAngle, materialWidth), 0)


sketch = Sketch()

### Lines

# Base
sketch.add_line(origin, originWidth)
# Long Leg
sketch.add_line(origin, longPt)
# Cut Face
sketch.add_line(longPt, shortPt)
# Short Leg
sketch.add_line(originWidth, shortPt)

# sketch.sketch.addConstraint(Sketcher.Constraint("Horizontal", 0))
# sketch.sketch.addConstraint(Sketcher.Constraint("Vertical", 1))
# sketch.sketch.addConstraint(Sketcher.Constraint("Parallel", 1, 3))
# sketch.sketch.addConstraint(Sketcher.Constraint('Coincident',0,1,1,1))
# sketch.sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 3, 2))

sketch.save_doc()