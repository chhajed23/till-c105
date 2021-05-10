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
newData.sort()
if n%2==0:
    m1=float(newData[n//2])
    m2=float(newData[n//2-1])
    median=(m1+m2)/2
else:
    median=newData[n//2]
print("Median is= ",str(median))


