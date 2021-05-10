import csv
from collections import Counter

with open("height.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newData=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newData.append(float(num))

data=Counter(newData)
mode_for_data_range={"50-60":0,"60-70":0,"70-80":0}
for height,occurence in data.items():
    if 50<float(height)<60:
        mode_for_data_range["50-60"]+=occurence
    elif 60<float(height)<70:
        mode_for_data_range["60-70"]+=occurence
    elif 70<float(height)<80:
        mode_for_data_range["70-80"]+=occurence
modeRange,modeOcurrence=0,0
for range,occurence in mode_for_data_range.items():
    if occurence>modeOcurrence:
        modeRange,modeOcurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((modeRange[0]+modeRange[1])/2)
print("Mode is= ", str(mode))
    


