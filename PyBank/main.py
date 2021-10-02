import os 
import csv 

#Your task is to create a Python script that analyzes the records to calculate each of the following:
Budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
Path = /Users/estefany/Documents/Python-Challenge/PyBank/Resources 
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

#The total number of months included in the dataset
 

#The net total amount of "Profit/Losses" over the entire period
 
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire periodrr