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
        self.sketchObj = self.doc.getObject('Sketch001')

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

    def save_locations(self, filePath):
        json.dump(self.locations, open(filePath, 'w'))