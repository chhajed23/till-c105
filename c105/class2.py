import csv
import pandas as pd
import plotly.express as px

with open("class2.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
totalMarks=0
totalEntries=len(file_data)

for marks in file_data:
    totalMarks+=float(marks[1])
mean=totalMarks/totalEntries
print("The mean found out is: ",str(mean))

df=pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(
        type="line",
        y0=mean,
        y1=mean,
        x0=0,
        x1=totalEntries
    )
])
fig.update_yaxes(rangemode="tozero")
fig.show()