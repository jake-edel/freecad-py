from ast import Constant
import sys
from unittest import skip
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint



filePath = 'freecad_saves/sketcher_script001.FCStd'

App.openDocument(filePath)
sketchObj = App.getDocument('sketcher_script001').getObject('Sketch')
sketchConst = sketchObj.Constraints

# pprint(vars(sketchConst[35]))

for constraint in sketchConst:
    if constraint.Name == '':
        skip
    else:
        print('-----')
        print("Index: " + str(sketchConst.index(constraint)))
        print(constraint.Name)
        print(constraint.Value)
        print(constraint.Type)
        print("Is Driving? " + str(constraint.Driving))

# App.getDocument('stringer').getObject('Sketch').setDatum(11,App.Units.Quantity('999.00000 mm'))
# App.getDocument('stringer').recompute()


sketchObj = App.getDocument('sketcher_script001').getObject('Sketch')
App.getDocument('sketcher_script001').saveAs('stringer12345.FCStd')