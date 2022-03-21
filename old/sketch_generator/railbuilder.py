import sketch_io
from old.sketch_generator.railing import Railing


class RailBuilder:
    def __init__(self, rise, run, counter):
        self.rise = rise
        self.run = run
        self.sketchFile = sketch_io.SketchFile()
        self.counter = counter

    def generate_rail(self):
        self.rail = Railing(self.rise, self.run)
        self.draw_lines(self.rail.partsList)
        self.add_constraints(self.rail.partsList)
        self.log_part_dimensions(self.rail.partsList)
        self.save_doc(self.counter)

    def draw_lines(self, parts):
        for part in parts:
            part.draw_lines(self.sketchFile)

    def add_constraints(self, parts):
        for part in parts:
            part.add_constraints(self.sketchFile)

    def log_part_dimensions(self, parts):
        print("Rail Generated")
        print("Rail Height: " + str(self.rail.postHeight))
        print("Material Width: " + str(self.rail.materialWidth))
        print("Rise: " + str(self.rise))
        print("Run: " + str(self.run))
        print("Rail Angle: " + str(self.rail.railAngle))
        print()

        for part in parts:
            part.log_dimensions()

    def save_doc(self, counter):
        self.sketchFile.save_doc(counter)
