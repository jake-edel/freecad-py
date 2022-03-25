from constraint_manager import ConstraintManager
from constraint_finder import ConstraintFinder
import json

templateFile = './templates/part_template.FCStd'
template = ConstraintManager(templateFile)

rails = json.load(open('./data/parts/rail_names.json'))

for rail in rails:
    constraintFile = './data/constraints/' + rail + '_constraints.json'
    cf = ConstraintFinder(constraintFile)

    parts = json.load(open('./data/parts/partlist.json'))

    for part in parts:
        driving_constrants = cf.find_constraints(part)

        for constraint in driving_constrants:
            if driving_constrants[constraint]['type'].startswith("Distance"):
                template.set_distance_constraint(constraint.split("_")[1], driving_constrants[constraint]['value'])
            else:
                template.set_angle_constraint(constraint.split("_")[1], driving_constrants[constraint]['value'])

        template.save_doc('./data/parts/' + rail + '_' + part)
