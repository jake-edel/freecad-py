import csv
from railbuilder import RailBuilder

with open('rise_run.csv', newline = '') as csvfile:
    csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(csv)
    rail_counter = 1
    for row in csv:
        riseRun = row[0].split(',')
        rise = float(riseRun[0])
        run = float(riseRun[1])
        input("RAIL BUILDER: Presss ENTER to generate rail with " + str(rise) + " rise and " + str(run) + " run.")
        rb = RailBuilder(rise, run, rail_counter)
        rb.generate_rail()
        rail_counter += 1