import plotly_express as px
import csv 
import numpy as np

def drawGraph():
    with open("tvsize.csv") as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Size of TV", y="	Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(data_path):
    sizeOfTv = []
    timeSpent = []

    with open(data_path) as csvFile:
        data = csv.DictReader(csvFile)
        for row in data:
            sizeOfTv.append(float(row["Size of TV"]))
            timeSpent.append(float(row["	Average time spent watching TV in a week (hours)"]))
        
    return{"x": sizeOfTv, "y": timeSpent}

def calcCorr(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation)

def main():
    data_path = "tvsize.csv"
    datasource = getDataSource(data_path)
    calcCorr(datasource)

    drawGraph()

main()
    
    


    

