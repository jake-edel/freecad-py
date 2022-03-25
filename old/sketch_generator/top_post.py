import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import Sketcher

class TopPost:
    def __init__(self, width, length, rise, run, mitreAngle, railAngle):
        self.length = length
        self.width = width

        self.run = run
        self.rise = rise

        self.origin = App.Vector(run, rise, 0)
        self.originOffset = self.origin + App.Vector(width, 0, 0)
        self.longPt = self.origin + App.Vector(0, length, 0)
        self.shortPt = self.origin + App.Vector(width, length, 0)


    def draw_lines(self, sketchFile):
        sketchFile.add_line(self.origin, self.originOffset)
        sketchFile.add_line(self.origin, self.longPt)
        sketchFile.add_line(self.longPt, self.shortPt)
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
        print("Top Post")
        print("Length: " + str(self.length))
        print()

