import numpy as np
import csv

def getDataSource(data_path):
    marks_pg = []
    days_pg = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_pg.append(float(row["Marks In Percentage"]))
            days_pg.append(float(row["Days Present"]))

    return {"x" : marks_pg, "y": days_pg}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = ""# <--mam pls put the data link

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
