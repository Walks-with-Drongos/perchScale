import tqdm
import csv
import glob
import sys
# USAGE
#python preprocesscsv.py  "D:\UCT Hot birds\Field work\2024\Whitney Fourie\Perch scale data\GA11\GA11 230125 0856"  "D:\UCT Hot birds\Field work\2024\Whitney Fourie\Perch scale data\GA13\GA13 230125 0752" "D:\UCT Hot birds\Field work\2024\Whitney Fourie\Perch scale data\GA29\GA29 311224" "D:\UCT Hot birds\Field work\2024\Whitney Fourie\Perch scale data\GA62\GA62 160325 1834"

data = []
TIME = 0
DATE = 1
OBS_NO = 2
WEIGHT = 3
STATUS = 4

def ConvertDate(date): # 14/11/2024
  pieces = date.split('/') 
  if len(pieces) <3: # in case DATE contains long incorrect dates
    print(date) # print bad date so can find manually 
  piecesnew = pieces[2]+ '/'+pieces[1]+ '/'+pieces[0]
  return piecesnew # 2024/11/14
   
def ExtractBox(path):
  # path = "D:\\UCT Hot birds\\Field work\\2024\\Whitney Fourie\\Perch scale data\\GA11\\GA11 230125 0856\\"
  parts = path.split("\\")
  BOX= parts[6]
  return BOX

def gather(folderPath, outputFile): #NOTE: take out the head row, if it exists. This will add it.
  with open(outputFile, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    print(folderPath)
    filenames = glob.glob(folderPath+'/weight*.txt')
    
    for filename in filenames:
      with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
          if len(row) >5:
            #if "-85239.00" in row:
            print(filename,row)
            continue
          if row[OBS_NO] == 'tare':
            continue
          if row[WEIGHT] == 'tare':
            continue
          data.append([ExtractBox(folderPath),ConvertDate(row[DATE]), row[TIME] , int(row[OBS_NO]), float(row[WEIGHT]), row[STATUS]]) 
  
def clean():
  print("clean")
  data.sort()
  data.insert(0,['BOX','DATE','TIME','OBS_NO','WEIGHT','STATUS'])
  
  with open('outputFile2.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for row in data:
      writer.writerow(row)

def group():
  print("group")
  
def filtering():
  print("filtering")
  

def main():
  dirs = sys.argv[1:]
  for dir in dirs:
    gather(dir, "gathered.csv")
  clean()
  group()
  filtering()

main()  






# ELEPHANT CODE GRAVEYARD

 #read in raw csv
  #OLD approach data = []
  # with open('gathered.csv', 'r') as file:
  #   reader = csv.reader(file)
  # for row in data:
    # if row[0] == 'TIME':
    #   continue