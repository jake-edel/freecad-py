import json
from pprint import pprint

constraintsFilePath = './data/constraints/rail01_constraints.json'
constraints = json.load(open(constraintsFilePath))

parts = ["bot_post", "top_rail", "top_post"]

def collect_constraints(part):
    part_constraints = {}

    for constraint in constraints:
        if constraint.startswith(part):
            part_constraints[constraint] = constraints[constraint]

    return part_constraints

pprint(collect_constraints("bot_post"))
pprint(collect_constraints("top_post"))
pprint(collect_constraints("top_rail"))
