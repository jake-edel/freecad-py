import sys
import this
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import math, csv


railHeight = 36
materialWidth = 1.5
partCount = 0

# main function to create new doc, generate parts, and save as new .FCStd file
def generate_rail(counter):
    doc = create_doc()
    create_bottom_post(doc)
    create_top_post(doc)
    create_top_rail(doc)
    doc.recompute
    save_rail(doc, counter)

# returns new document
def create_doc():
    return App.newDocument("scripted rail")

# adds new Box object to doc, gives object dimensions
class CreatePart:

    def post(doc, name, partCount):
        partCount += 1
        post = doc.addObject("Part::Box", name + str(partCount).zfill(2))

        post.Length = materialWidth
        post.Width = materialWidth
        post.Height = railHeight - materialWidth
        return post

    def top_rail(doc, name, partCount):
        partCount += 1
        rail = doc.addObject("Part::Box", name + str(partCount).zfill(2))

        rail.Length = stairRun + 20
        rail.Width = materialWidth
        rail.Height = materialWidth
        return rail
        

def create_bottom_post(doc):
    CreatePart.post(doc, 'bot_post', partCount)

def create_top_post(doc):
    topPost = CreatePart.post(doc, 'top_post', partCount)
    place_top_post(topPost)

def place_top_post(topPost):
    topPost.Placement=App.Placement(
        App.Vector(stairRun, 0, stairRise),
        App.Rotation(App.Vector(0,0,0),0),
        App.Vector(0,0,0)
        )

def create_top_rail(doc):
    topRail = CreatePart.top_rail(doc, 'top_rail', partCount)
    place_top_rail(topRail)

def place_top_rail(topRail):
    topRail.Placement=App.Placement(
        # App.Vector(0,0,railHeight - materialWidth),
        App.Vector(materialWidth,0,railHeight - materialWidth),
        App.Rotation(App.Vector(0,45,0),-(railAngle)),
        App.Vector(0,0,0))

def save_rail(doc, counter):
    doc.saveAs(u"/home/jakob/code/freecad/freecad_saves/generated_rail_" + str(counter).zfill(3) + ".FCStd")
 
with open('rise_run.csv', newline = '') as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(read)
    rail_counter = 1
    for row in read:
        stairRise = float(row[0].split(',')[0])
        stairRun = float(row[0].split(',')[1])
        railAngle = math.degrees(math.atan(stairRise/stairRun))
        generate_rail(rail_counter)
        rail_counter += 1