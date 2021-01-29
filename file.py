import pandas as pd 
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df,x = "data",y = "cases",
title = "corona cases",size = "cases",color = "country",size_max = 60)
fig.show()