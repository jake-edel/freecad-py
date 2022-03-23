import sys, json
from constraint_id import ConstraintManager
from constraint_mapper import ConstraintMapper
FREECADPATH = '/usr/lib/freecad-python3/lib'
sys.path.append(FREECADPATH)
import FreeCAD as App
from pprint import pprint

templateFile = './data/templates/part_template.FCStd'
constraintFile = './data/constraints/rail01_constraints.json'

template = ConstraintManager(templateFile)

cm = ConstraintMapper(constraintFile)

parts = ["bot-post", "top-rail", "top-post"]

pprint(template.constraints)
pprint(cm.collect_constraints("bot-post"))

driving_constrants = cm.collect_constraints("bot-post")

for constraint in driving_constrants:
    print(constraint.split("_")[1]['value'])

# template.set_constraint