import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App

railHeight = float(sys.argv[1])
railLength = float(sys.argv[2])
materialWidth = 1.5

doc = App.newDocument("scripted rail")

post1 = doc.addObject("Part::Box", "vert_post01")

post1.Length = materialWidth
post1.Width = materialWidth
post1.Height = railHeight - materialWidth

post2 = doc.addObject("Part::Box", "vert_post02")

post2.Length = materialWidth
post2.Width = materialWidth
post2.Height = railHeight - materialWidth

post2.Placement=App.Placement(App.Vector(railLength - materialWidth,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))

topRail = doc.addObject("Part::Box", "top_rail01")

topRail.Length = railLength
topRail.Width = materialWidth
topRail.Height = materialWidth

topRail.Placement=App.Placement(App.Vector(0,0,railHeight - materialWidth), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))


doc.recompute

doc.saveAs(u"/home/jakob/Documents/FreeCAD/python_generated_post.FCStd")
 
