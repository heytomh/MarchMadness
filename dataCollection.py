import os
import csv

# This will be the starting point for getting data for March Madness

# create or open the directory
dataDir = os.path.join('C:\\', 'Data', 'Python Projects', 'MarchMadness', 'MMDataFiles')

# print(dataDir)
# isItThere = os.path.exists(dataDir)
# print(isItThere)
# myFile = open((dataDir + '\\testfile.txt'), 'w')
# myFile.write('Test Data')
# myFile.close()
# myFile = open((dataDir + '\\testfile.txt'), 'a')
# myFile.write('Test More Data')
# myFile.close()

with open((dataDir + '\\testdatafile.csv'), mode='w') as theFile:
    dataWriter = csv.writer(theFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dataWriter.writerow(['John', 'Guard', 'UNLV'])
    dataWriter.writerow(['Barry', 'Guard', 'UCLA'])

