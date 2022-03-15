import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import Part


class SketchFile:
    def __init__(self):
        self.doc = self.create_doc()
        self.sketch = self.create_sketch()

    def create_doc(self):
        return App.newDocument("sketcher script")

    def save_doc(self, counter ):
        self.doc.recompute
        self.doc.saveAs(u"/home/jakobedel/code/freecad-py/freecad_saves/sketcher_script" + str(counter).zfill(3) + ".FCStd")
        print("Sketch saved sucessfully")

    def create_sketch(self):
        return self.doc.addObject("Sketcher::SketchObject", "Sketch")

    def add_line(self, v1, v2):
        self.sketch.addGeometry(Part.LineSegment(v1, v2))
