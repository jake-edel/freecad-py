from constraint_id import ConstraintManager
from location_id import LocationFinder
import csv

filePath = './data/templates/main_template.FCStd'

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

        railName ='rail' + str(counter).zfill(2)
        cm.save_constraints('./data/constraints/' + railName + '_constraints.json')
        cm.save_doc('./data/freecad_saves/' + railName + '.FCStd')

        lf = LocationFinder('./data/freecad_saves/' + railName + '.FCStd')
        lf.collect_locations()
        lf.save_locations('./data/locations/' + railName + '_locations.json')

        input("Generated rail with a " + str(rise) + '" rise and a ' + str(run) + '" run')
        
        counter += 1