import csv
import glob
import sys

#python preprocesscsv.py  "D:\UCT Hot birds\Field work\2024\Whitney Fourie\Perch scale data\GA11\GA11 230125 0856"
# GA29 311224
TIME = 0
DATE = 1
OBS_NO = 2
WEIGHT = 3
STATUS = 4

def ConvertDate(date):
  pieces = date.split('/') 
  if len(pieces) <3:
    print(date)
  piecesnew = pieces[2]+ '/'+pieces[1]+ '/'+pieces[0]
  return piecesnew

    
    #TODO main() 
    #TODO store as new file
    #TODO sort data
    #TODO havent grouped the data
    #TODO get max weight line with DATe and tIME retained
    

def gather(folderPath, outputFile): #NOTE: take out the head row, if it exists. This will add it.


  with open(outputFile, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    # writer.writerow(['TIME','DATE','OBS.NO','WEIGHT','STATUS']) #TODO fill out header CHECK IF BELOW WORKS THEN RM

    print(folderPath)
    filenames = glob.glob(folderPath+'/weight*.txt')
    print(filenames)
    for filename in filenames:
      with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        print(filename)
        for row in reader:
          # print(row)
          # if "95867.00" in row:
          #   print(filename,row)
          writer.writerow(row)
  
def clean():
  print("clean")
  #read in raw csv
  data = []
  with open('gathered.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      # if row[0] == 'TIME':
      #   continue
    
      if row[OBS_NO] == 'tare':
        continue
      if row[WEIGHT] == 'tare':
        continue
      data.append([ConvertDate(row[DATE]), row[TIME] , int(row[OBS_NO]), float(row[WEIGHT]), row[STATUS]]) 
    data.sort()
    data.insert(0,['DATE','TIME','OBS_NO','WEIGHT','STATUS'])
  # print('FINAL',data,'\n') #verify it works
  with open('outputFile2.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for row in data:
      # print(row)
      writer.writerow(row)

def group():
  print("group")
  
def filtering():
  print("filtering")
  

def main():
  dir = sys.argv[1]
  gather(dir, "gathered.csv")
  clean()
  group()
  filtering()

main()  


