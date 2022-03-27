from matplotlib.font_manager import json_dump
from constraint_manager import ConstraintManager
from location_id import LocationFinder
import csv, json

filePath = './templates/main_template.FCStd'

mainTemplate = ConstraintManager(filePath)
mainTemplate.generate_part_names()


with open('templates/rise_run.csv', newline = '') as csvfile:
    csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(csv)

    counter = 1

    input("RAIL GENERATOR: Presss ENTER to generate rail.")

    railNames = []

    for row in csv:

        rise = float(row[0].split(',')[0])
        run = float(row[0].split(',')[1])

        mainTemplate.set_distance_constraint('Run', run)
        mainTemplate.set_distance_constraint('Rise', rise)

        railName ='rail' + str(counter).zfill(2)
        railNames.append(railName)

        mainTemplate.save_constraints('./data/constraints/' + railName + '_constraints.json')
        mainTemplate.save_doc('./data/freecad_saves/' + railName + '.FCStd')

        lf = LocationFinder('./data/freecad_saves/' + railName + '.FCStd')
        lf.collect_locations()
        lf.save_locations('./data/locations/' + railName + '_locations.json')

        input("Generated rail with a " + str(rise) + '" rise and a ' + str(run) + '" run')
        
        counter += 1

json.dump(railNames, open('./data/parts/rail_list.json', 'w'))