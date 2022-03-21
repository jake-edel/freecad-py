from pydoc import doc
import sys, json
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint

class LocationFinder:
    def __init__(self, filePath):
        self.open_doc(filePath)

    def open_doc(self, filePath):
        self.doc = App.openDocument(filePath)
        # print(vars(self.doc))
        self.sketchObj = self.doc.getObject('Sketch001')
        print("Geometry Variables: " + str(vars(self.sketchObj)))
        print(self.sketchObj.Geometry)
        print(self.sketchObj.Geometry[0])
        # print(self.sketchObj.Constraints)

    def collect_locations(self):
        self.locations = {}

        parts = ["bot_post", "top_rail", "top_post"]

        counter = 0
        for index, point in enumerate(self.sketchObj.Geometry):
            self.locations[parts[index]] = {
                'x': point.X,
                'y': point.Y,
                'tag': point.Tag
            }

filePath = "./freecad_saves/sketcher_named_constraints.FCStd"

lf = LocationFinder(filePath)
lf.collect_locations()
print(lf.locations)