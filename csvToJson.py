import json
import csv

# Open the CSV
csvFile = open( 'data/Veiligheid_data_Rotterdam_raw.csv', 'r' )
jsonFile = open('data/rotterdam_safety_data.json', 'w')

# Change each fieldname to the appropriate field name.
reader = csv.DictReader(csvFile)

# Parse the CSV into JSON
# out = json.dumps([ row for row in reader ] )

jsonFile.write('{ \n')
i = 0
for row in reader:
    jsonFile.write(f'"{i}" : ')
    json.dump(row, jsonFile)
    jsonFile.write(', \n')
    i += 1

jsonFile.write('} \n')

print("JSON parsed!")