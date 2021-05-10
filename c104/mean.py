import csv

with open("height.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newData=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newData.append(float(num))

n=len(newData)
total=0
for x in newData:
    total+=x
mean=total/n 
print("mean = ",str(mean))