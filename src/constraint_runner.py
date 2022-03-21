from constraint_id import ConstraintManager
import csv

filePath = 'freecad_saves/sketcher_named_constraints.FCStd'

cm = ConstraintManager(filePath)
cm.print_constraints()

with open('data/rise_run.csv', newline = '') as csvfile:
    csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(csv)
    counter = 1
    input("RAIL GENERATOR: Presss ENTER to generate rail.")
    for row in csv:
        riseRun = row[0].split(',')
        rise = float(riseRun[0])
        run = float(riseRun[1])
        cm.set_constraint('Run', run)
        cm.set_constraint('Rise', rise)
        cm.save_constraints('./data/new_constraints' + str(counter).zfill(2) + '.json')
        cm.save_doc('./freecad_saves/constraints_new' + str(counter).zfill(2) + '.FCStd')
        input("Generated rail with a " + str(rise) + '" rise and a ' + str(run) + '" run')
        counter += 1