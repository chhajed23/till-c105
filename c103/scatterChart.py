import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
fig=px.scatter(df,x="Population",y="InternetUsers",size="Percentage",color="Country",size_max=70)
fig.show()