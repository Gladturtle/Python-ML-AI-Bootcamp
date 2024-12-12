import pandas as pd
from plotly.offline import init_notebook_mode,plot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
df = pd.read_excel('D:\\Programs\\Python\\Refactored_Py_DS_ML_Bootcamp-master\\Unemployment USA(1980-2018) choropleth map\\emp-unemployment.xlsx',sheet_name = 'States')
df.drop(index = 0,inplace = True)
list =[]
Balls = True
while Balls:
    year = 0
    while year<1980 or year>2018:
        year = input("Enter years from (1980-2008)")
        year = int(year)
    i = 0
    for area in df['Area']:
        text = area + "\nUnemployment Rate " + str(df.iloc[i][year])
        list.append(text)
        i += 1
    df.insert(1,"Text",value = list)
    csv1 = pd.read_csv("D:\\Programs\\Python\\Refactored_Py_DS_ML_Bootcamp-master\\Unemployment USA(1980-2018) choropleth map\\us-state-ansi-fips.csv")
    list = []
    for name in df['Area']:
        list.append(csv1[' stusps'].loc[csv1['stname']==name].iloc[0].strip())
    df.insert(1,"StCode",value= list)
    data = dict(type = 'choropleth',
            colorscale='ylorbr', 
            locations = df['StCode'],
            locationmode = 'USA-states',
            z =df[year],text = df['Text'],
            colorbar = {'title':'Unemployment Rate'},
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2 )))
    layout = dict(title = 'Unemployment '+str(year),geo = dict(scope = 'usa',showlakes = True, lakecolor = 'rgb(85,173,240)'))
    choromap = go.Figure(data = [data],layout = layout)
    plot(choromap)
    while Balls not in ['True','False']:
        Balls = input("Input True if you want another plot else press False")
    Balls = bool(Balls)
