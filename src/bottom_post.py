import sys
from triangle_helper import TriangleHelper
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import Sketcher

class BottomPost:
    def __init__(self, width, length, mitreAngle, railAngle):
        self.length = length
        self.shortLeg = TriangleHelper.short_leg(length, mitreAngle, width)
        self.width = width
        self.railAngle = railAngle
        self.mitreAngle = mitreAngle

        # Origin
        self.origin = App.Vector(0, 0, 0) + App.Vector(1, 1, 1)
        # X: material width, Y: 0
        self.originOffset = App.Vector(width, 0, 0)
        # Long point of mitre cut
        self.longPt = App.Vector(0, length, 0)
        # Short point of mitre cut0
        self.shortPt = App.Vector(width, self.shortLeg, 0)


    def draw_lines(self, sketchFile):
        # Base - 0
        sketchFile.add_line(self.origin, self.originOffset)
        # Long Leg - 1
        sketchFile.add_line(self.origin, self.longPt)
        # Cut Face - 2
        sketchFile.add_line(self.longPt, self.shortPt)
        # Short Leg - 3
        sketchFile.add_line(self.originOffset, self.shortPt)

    def add_constraints(self, sketchFile):
       ## Constrain Base to Origin
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', -1,1,0,1))

        ## Connect Points
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident',0,1,1,1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 3, 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 2, 2, 3, 2))

        ## Constrain Horizontal and Vertical
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Horizontal", 0))
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Vertical", 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Vertical", 3))

        ## Constrain Length + Width
        sketchFile.sketch.addConstraint(Sketcher.Constraint('DistanceX', 0, 1, 0, 2, App.Units.Quantity(self.width)))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('DistanceY', 1, 1, 1, 2, App.Units.Quantity(self.length)))

        ## Constrain Angle
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Angle', 1, 2, 2, 1, App.Units.Quantity('{0} deg'.format(str(TriangleHelper.alt_angle(self.railAngle))))))


    def log_dimensions(self):
        print("Bottom Post")
        print("Rail Angle: " + str(self.railAngle))
        print("Mitre Angle: " + str(self.mitreAngle))
        print("Length (Long): " + str(self.length))
        print("Length (Short): " + str(TriangleHelper.short_leg(self.length, self.mitreAngle, self.width)))

