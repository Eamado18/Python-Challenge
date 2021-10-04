import os 
import csv 

#Your task is to create a Python script that analyzes the records to calculate each of the following:
Bank_csv = os.path.join('PyBank',"Resources","budget_data.csv")

Date_rows = 0
Net_total = 0 
Profit_Losses = []
Profit_Losses_change = []  
Months = []

with open(Bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

#The total number of months included in the dataset
    for row in csvreader:
      Date_rows = Date_rows + 1 
    
#The net total amount of "Profit/Losses" over the entire period
      Net_total = Net_total + int(row[1]) 

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
      Profit_Losses.append(int(row[1])) 
      
      for i in range(len(Profit_Losses)-1):
        Profit_Losses_change.append(Profit_Losses[i+1]-Profit_Losses[i])
        Months.append(row[0])

max_increase_value = max(Profit_Losses_change)
max_increase_month = Profit_Losses_change.index(max(Profit_Losses_change)) 
max_decrease_value = min(Profit_Losses_change)
max_decrease_month = Profit_Losses_change.index(min(Profit_Losses_change))
 
print ("Financial Analysis")
print ("-----------------------------")
print ("Total : ", "$", (Net_total))
print ("Total Months : ", (Date_rows)) 
print (f"Average Change: {round(sum(Profit_Losses_change)/len(Profit_Losses_change),2)}")
print ("Greatest Increase in Profits: ", Months[max_increase_month], f"${(int(max_increase_value))}") 
print ("Greatest Decrease in Profits: ", Months[max_decrease_month], f"${(int(max_decrease_value))}") 

output_file = os.path.join("PyBank", "Analysis","Analysis.txt") 

with open(output_file, "w") as file: 
    file.write("Financial Analysis")
    file.write('\n' +"-----------------------------")
    file.write('\n' +"Total : $" + str(Net_total))
    file.write('\n' +"Total Months :" + str(Date_rows)) 
    file.write('\n' +f"Average Change: {round(sum(Profit_Losses_change)/len(Profit_Losses_change),2)}")
    file.write('\n' +"Greatest Decrease in Profits: " + (Months[max_decrease_month] + (f" (${(str(max_decrease_value))})")))
    file.write('\n' +"Greatest Increase in Profits: " + (Months[max_increase_month] + (f" (${(str(max_increase_value))})")))
