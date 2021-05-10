import csv
import math
import statistics

with open("data.csv",newline="") as f:
   reader= csv.reader(f)
   file_data=list(reader)
data=file_data[0]
#Finding Mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

#squaring and getting the values
squaredList=[]
for num in data:
    a=int(num)-mean(data)
    a=a**2
    squaredList.append(a)

#getting sum
sum=0
for y in squaredList:
    sum=sum+y

#dividing the sum by total values -1
result=sum/(len(data)-1)

std_deviation=math.sqrt(result)
print("The standard Deviation founded is: ",std_deviation)
stats=statistics.stdev(data)
print("The Statisstics founded is: ",str(stats))
