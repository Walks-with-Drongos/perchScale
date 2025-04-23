import csv

TIME = 0
DATE = 1
OBS_NO = 2
WEIGHT = 3
STATUS = 4

def ConvertDate(date):
  pieces = date.split('/') 
  piecesnew = pieces[2]+ '/'+pieces[1]+ '/'+pieces[0]
  return piecesnew

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
    data.append([row[TIME], ConvertDate(row[DATE]), int(row[OBS_NO]), float(row[WEIGHT]), row[STATUS]]) 
    
    #TODO main 
    #TODO store as new file
    #TODO sort data
    #TODO havent grouped the data
    #TODO get max weight line with DATe and tIME retained
    

print('FINAL',data,'\n') #verify it works


