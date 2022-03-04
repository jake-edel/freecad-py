import sys
# import this
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import math, csv

railHeight = 36
materialWidth = 1.5


# adds new Box object to doc, gives object dimensions
class CreatePart:

    def post(doc, name):
        post = doc.addObject("Part::Box", name)

        post.Length = materialWidth
        post.Width = materialWidth
        post.Height = railHeight - materialWidth
        return post

    def top_rail(doc, name):
        rail = doc.addObject("Part::Box", name)

        rail.Length = stairRun + 20
        rail.Width = materialWidth
        rail.Height = materialWidth
        return rail


# takes parts as args and places in model
class PlacePart:
    def top_post(post):
        post.Placement=App.Placement(
        App.Vector(stairRun, 0, stairRise),
        App.Rotation(App.Vector(0,0,0),0),
        App.Vector(0,0,0)
        )

    def top_rail(rail):
        rail.Placement=App.Placement(
        App.Vector(materialWidth,0,railHeight - materialWidth),
        App.Rotation(App.Vector(0,45,0),-(railAngle)),
        App.Vector(0,0,0))

# main function to create new doc, generate parts, and save as new .FCStd file
class RailGenerator:

    def generate_rail(counter):
        doc = RailGenerator.create_doc()
        RailGenerator.create_bottom_post(doc)
        RailGenerator.create_top_post(doc)
        RailGenerator.create_top_rail(doc)
        doc.recompute
        RailGenerator.save_rail(doc, counter)

    def create_doc():
        return App.newDocument("scripted rail")

    def create_bottom_post(doc):
        CreatePart.post(doc, 'bot_post')

    def create_top_post(doc):
        topPost = CreatePart.post(doc, 'top_post')
        PlacePart.top_post(topPost)

    def create_top_rail(doc):
        topRail = CreatePart.top_rail(doc, 'top_rail')
        PlacePart.top_rail(topRail)

    def save_rail(doc, counter):
        doc.saveAs(u"/home/jakob/code/freecad/freecad_saves/generated_rail_" + str(counter).zfill(3) + ".FCStd")
 
with open('rise_run.csv', newline = '') as csvfile:
    csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(csv)
    rail_counter = 1
    input("RAIL GENERATOR: Presss ENTER to generate rail.")
    for row in csv:
        riseRun = row[0].split(',')
        stairRise = float(riseRun[0])
        stairRun = float(riseRun[1])
        railAngle = math.degrees(math.atan(stairRise/stairRun))
        RailGenerator.generate_rail(rail_counter)
        input("Generated rail with a " + str(stairRise) + '" in rise and a ' + str(stairRun) + '" in run')
        rail_counter += 1