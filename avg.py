import csv
import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('108/pro.csv')
fig = ff.create_distplot([df["Avg"].tolist()],["Avg"],show_hist=False)
fig.show()