#print("Hello World")
#filename = "weights_2025030105.txt"
#print(filename)

#f = open(filename, "r")
#lines = f.read().splitlines()
#print(f.readlines())

# for line in lines:
#     x = line.split(",")
#     print(x)

# next step column headers
# identifying which rows to delete (1 second or weight threshold) - SOLVED MAX

# print(x)
#never forget to check that data is sorted correctly before grouping

import pandas as pd
df = pd.read_csv('outputFile2.csv')
# print(df)  #BEFORE

df['Visit'] = None
Visit = 0
for index, row in df.iterrows():
 if row['OBS_NO'] == 1: Visit = Visit +1 
 df.at[index, 'Visit'] = Visit #row['Age'] + 5 

# print(df) #AFTER
df.to_csv('gathered_Visit.csv', index=False)

df2 = pd.read_csv('gathered_Visit.csv')
# print(df2['Visit'].dtype)

# for i, rowi in grouped_visit.items():
# #  print(i,rowi)
# # print(type(grouped_visit))

# test_df = pd.DataFrame(columns=['DATE', 'TIME', 'WEIGHT', 'VISIT'])
# test_df.loc[1] = ['foo','bar','baz','quux']
# print(test_df)

#df['Visit'] = df['Visit'].astype('string')
#df['WEIGHT'] = df['WEIGHT'].astype(float)

max_weight_indices = df2.groupby('Visit')['WEIGHT'].idxmax()
# print('test',max_weight_indices)
#Then, use .loc to get the corresponding rows
max_weight_rows = df2.loc[max_weight_indices].reset_index(drop=True)
# # This will retain TIME, DATE, OBS.NO, WEIGHT, and VISIT for the max weight row of each VISIT group
# print(max_weight_rows)
max_weight_rows.to_csv("MaxWeightPerVisit.csv", index = False)

#TODO add all text files from

# # # grouped_visit['DATE'] = None
# # # grouped_visit['TIME'] = None
# # for i, rowi in grouped_visit.iterrows():
# #   for j, rowj in df.iterrows():
# #     if rowi['WEIGHT'] == rowj['WEIGHT'] and rowi['Visit'] == rowj['Visit']:
# #      grouped_visit.at[j, 'DATE'] = rowj['DATE']
# #      grouped_visit.at[j, 'TIME'] = rowj['TIME']
# #  # for Visit in grouped_visit
# #  print("GroupedbyVisit:\n", grouped_visit)

