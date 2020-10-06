import csv

csvData = [['Name of Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
