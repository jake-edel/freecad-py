import sys
import sketch_io
from triangle_helper import TriangleHelper
from bottom_post import BottomPost
from top_rail import TopRail
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App

class RailBuilder:
    def __init__(self, rise, run):
        self.postHeight = 36
        self.materialWidth = 1.5
        self.rise = rise
        self.run = run
        self.railAngle = TriangleHelper.rail_angle(rise, run)
        self.mitreAngle = TriangleHelper.mitre_angle(self.railAngle)
        self.sketchFile = sketch_io.SketchFile()

    def generate_rail(self):
        botPost = BottomPost(self.materialWidth, self.postHeight, self.mitreAngle, self.railAngle)
        # topRail = TopRail(self.materialWidth, self.postHeight, self.mitreAngle, self.railAngle, botPost)
        # topPost = TopPost(self.materialWidth, self.postHeight, self.mitreAngle, self.railAngle)
        self.draw_lines(botPost)
        self.add_constraints(botPost)
        self.log_dimensions(botPost)
        self.save_doc()

    def draw_lines(self, part):
        part.draw_lines(self.sketchFile)

    def add_constraints(self, part):
        part.add_constraints(self.sketchFile)

    def log_dimensions(self, part):
        part.log_dimensions()

    def save_doc(self):
        self.sketchFile.save_doc()
