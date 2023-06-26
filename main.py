# Working with csv files
# Read from a csv file and output the data to the user
# Import the built in csv library for the project
# 26/06/2023

import csv
import pandas as pd

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
