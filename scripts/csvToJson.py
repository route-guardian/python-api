import json
import csv

# Open the CSV
csvFile = open('../data/Veiligheid_data_Rotterdam_raw.csv', 'r')
# Open the Json
jsonFile = open('../data/rotterdam_safety_data.json', 'w')

# Change each fieldname to the appropriate field name.
reader = csv.DictReader(csvFile)

# Initialize dictionary
areas = {}

# Parse the CSV into JSON
for row in reader:
    if row['gebied'] == '':
        continue

    # Check if 'gebied' is already in dictionary
    if row['gebied'] not in areas:
        areas[row['gebied']] = {}

    # make 'buurt' a new object
    areas[row['gebied']][row['BUURT85']] = {}
    # set id
    areas[row['gebied']][row['BUURT85']]['id'] = row['wijknr']

    # make copy of 'row' data and remove first 3 columns
    data = row.copy()
    data.pop('gebied')
    data.pop('BUURT85')
    data.pop('wijknr')
    # transform values to from sting to int
    for key, value in data.items():
        # check if value is actually a sting AND not a percentage
        if isinstance(value, str) and value[len(value)-1] != "%":
            # check if value is an integer
            try:
                data[key] = int(value)
            # otherwise handle it as float
            except ValueError:
                data[key] = float(value)

    # set data
    areas[row['gebied']][row['BUURT85']]['data'] = data

# dump parsed json data in the file
json.dump(areas, jsonFile)

print('JSON parsed!')
