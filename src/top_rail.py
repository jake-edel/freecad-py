import sys
from triangle_helper import TriangleHelper
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import Sketcher

class TopRail:
    def __init__(self, width, rise, run, mitreAngle, railAngle, botPost):
        self.length = TriangleHelper.find_hypotenuse(rise, run)
        # self.shortLeg = TriangleHelper.short_leg(length, mitreAngle, width)
        self.width = width
        self.railAngle = railAngle
        self.mitreAngle = mitreAngle

        # Origin
        self.origin = botPost.longPt
        # X: material width, Y: 0
        self.originOffset = botPost.shortPt
        # Long point of mitre cut
        self.longPt = self.origin + App.Vector(run, rise, 0)
        # Short point of mitre cut0
        self.shortPt = self.originOffset + App.Vector(run - width, rise - TriangleHelper.find_oppisite(railAngle, width), 0)


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

        ## Connect Points
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 5, 1, 1, 2))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 5, 2, 6, 1))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 6, 2, 7, 2))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 7, 1, 4, 2))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 4, 1, 1, 2))
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Coincident', 7, 1, 2, 2))

        ## Constrain Parallel
        sketchFile.sketch.addConstraint(Sketcher.Constraint('Parallel', 5, 7))


        # ## Constrain Horizontal and Vertical
        sketchFile.sketch.addConstraint(Sketcher.Constraint("Vertical", 6))



    def log_dimensions(self):
        print("Top Rail")
        print("Top Mitre: " + str(self.railAngle))
        print("Bottom Mitre: " + str(self.mitreAngle))
        print("Length (Long): " + str(self.length))
        print()
