import numpy as np
import csv
import plotly.express  as px 

def plotFigure(datapath):
    with open(datapath) as csv_file :
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(datapath) :
    icecreamsales=[]
    cooldrink = []
    with open(datapath) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            icecreamsales.append(float(row["Coffee in ml"]))
            cooldrink.append(float(row["sleep in hours"]))
    
    return{"x": icecreamsales , "y" : cooldrink}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Sleeping time vs coffee drunk :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()