import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import math, csv


railHeight = 36
materialWidth = 1.5

# main function to create new doc, generate parts, and save as new .FCStd file
def generate_rail(counter):
    doc = create_doc()
    create_bottom_post(doc)
    create_top_post(doc)
    create_top_rail(doc)
    doc.recompute
    save_rail(doc, counter)

def create_doc():
    return App.newDocument("scripted rail")


def create_bottom_post(doc):

    botPost = doc.addObject("Part::Box", "vert_post01")

    botPost.Length = materialWidth
    botPost.Width = materialWidth
    botPost.Height = railHeight - materialWidth

# def angle_height():
#     return math.sin(railAngle) * materialWidth

def create_top_post(doc):
    topPost = doc.addObject("Part::Box", "vert_post02")

    topPost.Length = materialWidth
    topPost.Width = materialWidth
    topPost.Height = (railHeight - materialWidth)
    place_top_post(topPost)

def place_top_post(topPost):
    topPost.Placement=App.Placement(
        App.Vector(stairRun, 0, stairRise),
        App.Rotation(App.Vector(0,0,0),0),
        App.Vector(0,0,0)
        )

def create_top_rail(doc):
    topRail = doc.addObject("Part::Box", "top_rail01")

    topRail.Length = stairRun + 20
    topRail.Width = materialWidth
    topRail.Height = materialWidth
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