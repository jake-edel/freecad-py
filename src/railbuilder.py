import sys
import sketch_io
from triangle_helper import TriangleHelper
from bottom_post import BottomPost
from top_rail import TopRail
from top_post import TopPost
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App

class RailBuilder:
    def __init__(self, rise, run, counter):
        self.postHeight = 36
        self.materialWidth = 1.5
        self.rise = rise
        self.run = run
        self.railAngle = TriangleHelper.rail_angle(rise, run)
        self.mitreAngle = TriangleHelper.mitre_angle(self.railAngle)
        self.sketchFile = sketch_io.SketchFile()
        self.counter = counter

    def generate_rail(self):
        botPost = BottomPost(self.materialWidth, self.postHeight, self.mitreAngle, self.railAngle)
        topRail = TopRail(self.materialWidth, self.rise, self.run, self.mitreAngle, self.railAngle, botPost)
        topPost = TopPost(self.materialWidth, self.postHeight, self.rise, self.run, self.mitreAngle, self.railAngle)
        self.draw_lines(botPost)
        self.draw_lines(topRail)
        self.draw_lines(topPost)
        self.add_constraints(botPost)
        self.add_constraints(topRail)
        self.add_constraints(topPost)
        self.log_rail_dimensions()
        self.log_part_dimensions(botPost)
        self.log_part_dimensions(topRail)
        self.log_part_dimensions(topPost)
        self.save_doc(self.counter)

    def draw_lines(self, part):
        part.draw_lines(self.sketchFile)

    def add_constraints(self, part):
        part.add_constraints(self.sketchFile)

    def log_part_dimensions(self, part):
        part.log_dimensions()

    def log_rail_dimensions(self):
        print("Rail Generated")
        print("Material Width: " + str(self.materialWidth))
        print("Rise: " + str(self.rise))
        print("Run: " + str(self.run))
        print("Rail Angle: " + str(self.railAngle))
        print()

    def save_doc(self, counter):
        self.sketchFile.save_doc(counter)
