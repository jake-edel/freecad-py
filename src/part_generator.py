import sys, json

from constraint_id import ConstraintManager
from location_id import LocationFinder
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint

constraintsFilePath = './data/constraints/rail01_constraints.json'
constraints = open(constraintsFilePath)

constraints = json.load(constraints)

def find_part_constraints():
    part_constraints = []


    for key in constraints.keys():
        part_constraints.append(key)

    return part_constraints

constraints = find_part_constraints()
print(constraints)