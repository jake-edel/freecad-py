docName = 'python_script'

doc = FreeCAD.newDocument(docName)
App.setActiveDocument(docName)  

box = doc.addObject("Part::Box", "int_post")

box.Length = 1.5
box.Width = 1.5
box.Height = 34.8125

doc.recompute

App.getDocument(docName).saveAs(u"/home/jakob/Documents/FreeCAD/python_generated_post.FCStd")
 
