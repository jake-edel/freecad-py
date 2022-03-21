from constraint_id import ConstraintManager
from location_id import LocationFinder
import csv

filePath = 'sketcher_named_constraints.FCStd'

cm = ConstraintManager(filePath)


with open('data/rise_run.csv', newline = '') as csvfile:
    csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(csv)

    counter = 1

    input("RAIL GENERATOR: Presss ENTER to generate rail.")

    for row in csv:

        rise = float(row[0].split(',')[0])
        run = float(row[0].split(',')[1])

        cm.set_constraint('Run', run)
        cm.set_constraint('Rise', rise)

        cm.save_constraints('./data/constraints/rail' + str(counter).zfill(2) + '_constraints.json')
        cm.save_doc(cadFilePath)

        lf = LocationFinder('./data/freecad_saves/rail' + str(counter).zfill(2) + '.FCStd')
        lf.collect_locations()
        lf.save_locations('./data/locations/rail' + str(counter).zfill(2) + '_locations.json')

        input("Generated rail with a " + str(rise) + '" rise and a ' + str(run) + '" run')
        
        counter += 1