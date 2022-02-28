import sys
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
import FreeCADGui as Gui

docName = 'python_script'

doc = App.newDocument(docName)
# doc_gui = Gui.newDocument(doc)

box = doc.addObject("Part::Box", "vert_post01")

box.Length = 1.5
box.Width = 1.5
box.Height = 34.8125

box2 = doc.addObject("Part::Box", "vert_post02")

box2.Length = 1.5
box2.Width = 1.5
box2.Height = 34.8125

box2.Placement=App.Placement(App.Vector(10,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))

# Gui.getDocument("python_generated_post").getObject("vert_post01").Visibility=True

# Gui.getDocument("python_generated_post").getObject("vert_post02").Visibility=True

doc.recompute

doc.saveAs(u"/home/jakob/Documents/FreeCAD/python_generated_post.FCStd")
 
