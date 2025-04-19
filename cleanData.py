#print("Hello World")
filename = "weights_2025030105.txt"
print(filename)

f = open(filename, "r")
lines = f.read().splitlines()
#print(f.readlines())

for line in lines:
    x = line.split(",")
    print(x)

# next step column headers
# identifying which rows to delete (1 second or weight threshold)

print(x)

#import pandas as pd
#df = pd.DataFrame(x)
#df.columns = ['TIME', 'DATE', 'OBS', 'WEIGHT','STATUS']
#print(df)