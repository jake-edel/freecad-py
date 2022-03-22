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
        self.locations = self.collect_locations()

    def collect_locations(self):
        locations = {}

        parts = ["bot_post", "top_rail", "top_post"]

        for index, point in enumerate(self.sketchObj.Geometry):
            locations[parts[index]] = {
                'x': point.X,
                'y': point.Y,
                'tag': point.Tag
            }
        return locations

    def save_locations(self, filePath):
        json.dump(self.locations, open(filePath, 'w'))

    def print_locations(self):
        pprint(self.locations)