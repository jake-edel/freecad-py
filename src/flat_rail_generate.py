import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App

railHeight = 36
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
    App.Vector(railLength - materialWidth, 0, 0),
    App.Rotation(App.Vector(0,0,0),0),
    App.Vector(0,0,0)
    )

topRail = doc.addObject("Part::Box", "top_rail01")

topRail.Length = railLength
topRail.Width = materialWidth
topRail.Height = materialWidth

topRail.Placement=App.Placement(
    App.Vector(0,0,railHeight - materialWidth),
    App.Rotation(App.Vector(0,0,0),0),
    App.Vector(0,0,0))


doc.recompute

doc.saveAs(u"/home/jakob/code/freecad/freecad_saves/python_generated_post.FCStd")
 