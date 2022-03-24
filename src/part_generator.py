import sys, json
from constraint_manager import ConstraintManager
from constraint_finder import ConstraintFinder
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint

templateFile = './templates/part_template.FCStd'
constraintFile = './data/constraints/rail01_constraints.json'

template = ConstraintManager(templateFile)

cf = ConstraintFinder(constraintFile)

parts = ["bot-post", "top-rail", "top-post"]

for part in parts:
    driving_constrants = cf.find_constraints(part)

    for constraint in driving_constrants:
        # print("Constraint Name: " + constraint.split("_")[1])
        # print("Constraint Type: " + driving_constrants[constraint]['type'])
        # print("Constraint Value: " + driving_constrants[constraint]['value'])
        # print("Template Value: " + template.constraints[constraint.split("_")[1]]['value'])
        # print()
        if driving_constrants[constraint]['type'].startswith("Distance"):
            template.set_distance_constraint(constraint.split("_")[1], driving_constrants[constraint]['value'])
        else:
            template.set_angle_constraint(constraint.split("_")[1], driving_constrants[constraint]['value'])

    template.save_doc('./data/parts/rail01_' + part)
