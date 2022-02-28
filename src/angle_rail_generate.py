import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import math

stairRise = float(sys.argv[1])
stairRun = float(sys.argv[2])
railAngle = math.degrees(math.atan(stairRise/stairRun))

# Bot => Top
railHeight = 36

# Out => Out
railLength = 60

materialWidth = 1.5

doc = App.newDocument("scripted rail")

botPost = doc.addObject("Part::Box", "vert_post01")

botPost.Length = materialWidth
botPost.Width = materialWidth
botPost.Height = railHeight - materialWidth

topPost = doc.addObject("Part::Box", "vert_post02")

topPost.Length = materialWidth
topPost.Width = materialWidth
topPost.Height = railHeight - materialWidth

# 38.61

topPost.Placement=App.Placement(
    # Magic number is tan(railAngle) x stairRun
    App.Vector(stairRun, 0, stairRise),
    App.Rotation(App.Vector(0,0,0),0),
    App.Vector(0,0,0)
    )

topRail = doc.addObject("Part::Box", "top_rail01")

topRail.Length = railLength + 30
topRail.Width = materialWidth
topRail.Height = materialWidth

topRail.Placement=App.Placement(
    App.Vector(materialWidth,0,railHeight - materialWidth),
    # App.Rotation(App.Vector(0,0,0),-0),
    App.Rotation(App.Vector(0,45,0),-(railAngle)),
    App.Vector(0,0,0))


doc.recompute

doc.saveAs(u"/home/jakob/code/freecad/freecad_saves/python_generated_post.FCStd")
 