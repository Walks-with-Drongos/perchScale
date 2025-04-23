import csv

TIME = 0
DATE = 1
OBS_NO = 2
WEIGHT = 3
STATUS = 4

#read in raw csv
data = []
with open('TESTTAREPYTHON.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    if row[0] == 'TIME':
      continue
    #TODO if TARE, skip it
    if row[OBS_NO] == 'tare':
      continue
    print(row) #print whole row
    data.append([row[TIME], row[DATE], int(row[OBS_NO]), float(row[WEIGHT]), row[STATUS]]) 
    
    #TODO write function to convert date 01/03/2025 -> 2025/03/01
    #TODO use the new function

print('FINAL',data,'\n') #verify it works


