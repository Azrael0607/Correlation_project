import csv
import pandas as pd
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    percentage = []
    days_present = []
    
    with open (data_path) as (csv_file):
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            percentage.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
    return{'x': percentage ,'y': days_present}

def find_correlation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print('correlation between days present and marks of a student is', correlation[0,1])

def setup():
    data_path = 'Student Marks vs Days Present.csv'
    datasource = getDataSource(data_path)
    find_correlation(datasource)
setup()

