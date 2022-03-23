import json
from pprint import pprint

constraintsFilePath = './data/constraints/rail01_constraints.json'

class ConstraintMapper:

    def __init__(self, filePath):
        self.constraints = self.open_constraints(filePath)

    def open_constraints(self, filePath):
        return json.load(open(filePath))
    
    def collect_constraints(self, part):
        part_constraints = {}

        for constraint in self.constraints:
            if constraint.startswith(part):
                part_constraints[constraint] = self.constraints[constraint]

        return part_constraints
