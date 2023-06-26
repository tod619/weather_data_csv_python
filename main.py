# Working with csv files
# Read from a csv file and output the data to the user
# Import the built in csv library for the project
# 26/06/2023

import csv
import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# Use pandas to read the data and print to the terminal
data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# Convert the data to a dictionary
data_dict = data.to_dict()
print(data_dict)
