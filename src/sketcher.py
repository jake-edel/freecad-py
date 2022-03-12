import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import FreeCADGui as Gui
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

    def create_sketch(self):
        return self.doc.addObject("Sketcher::SketchObject", "Sketch")

    def add_line(self, v1, v2):
        self.sketch.addGeometry(Part.LineSegment(v1, v2))
        # sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 2, 1))

origin = App.Vector(0, 0, 0)
postHeight = App.Vector(0, 36, 0)
materialWidth = App.Vector(1.5, 0, 0)

sketch = Sketch()
sketch.add_line(origin, postHeight)
sketch.add_line(origin, materialWidth)
sketch.save_doc()