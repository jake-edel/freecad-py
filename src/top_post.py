from cProfile import run
from lib2to3.pgen2.token import RIGHTSHIFTEQUAL
import sys
from triangle_helper import TriangleHelper
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import Sketcher

class TopPost:
    def __init__(self, width, length, rise, run, mitreAngle, railAngle):
        self.length = length
        # self.shortLeg = TriangleHelper.short_leg(length, mitreAngle, width)
        self.width = width
        # self.railAngle = railAngle
        # self.mitreAngle = mitreAngle
        self.run = run
        self.rise = rise

        # Origin
        self.origin = App.Vector(run, rise, 0)
        # X: material width, Y: 0
        self.originOffset = self.origin + App.Vector(width, 0, 0)
        # Long point of mitre cut
        self.longPt = self.origin + App.Vector(0, length, 0)
        # Short point of mitre cut
        self.shortPt = self.origin + App.Vector(width, length, 0)


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
        # sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', -1,1,0,1))

        ## Connect Points
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 8, 1, 9, 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 9, 2, 10, 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 10, 2, 11, 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 11, 2, 8, 2))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 9, 2, 5, 2))

        ## Constrain Horizontal, Vertical, Parallel
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Horizontal", 8))
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Vertical", 9))
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Parallel", 9, 11))
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Parallel", 8, 10))

        ## Constrain Length + Width
        sketchFile.sketch.addConstraint(Sketcher.Constraint('DistanceX', 8, 1, 8, 2, App.Units.Quantity(self.width)))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('DistanceY', 9, 1, 9, 2, App.Units.Quantity(self.length)))
        ## Constrain Rise + Run
        sketchFile.sketch.addConstraint(Sketcher.Constraint('DistanceX', -1, 1, 8, 1, App.Units.Quantity(self.run)))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('DistanceY', -1, 1, 8, 1, App.Units.Quantity(self.rise)))



    def log_dimensions(self):
        print("Bottom Post")
        print("Rail Angle: " + str(self.railAngle))
        print("Mitre Angle: " + str(self.mitreAngle))
        print("Length (Long): " + str(self.length))
        print("Length (Short): " + str(TriangleHelper.short_leg(self.length, self.mitreAngle, self.width)))

