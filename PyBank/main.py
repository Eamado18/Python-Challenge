import os 
import csv 

#Your task is to create a Python script that analyzes the records to calculate each of the following:
Bank_csv = os.path.join('PyBank',"Resources","budget_data.csv")

Date_rows = 0
Net_total = 0 

with open(Bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)


#The total number of months included in the dataset
    for row in csvreader:
      Date_rows = Date_rows + 1 
    
#The net total amount of "Profit/Losses" over the entire period
      Net_total = Net_total + int(row[1]) 
    print ("Total : ", "$", (Net_total))
    print ("Total Months : ", (Date_rows)) 
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period