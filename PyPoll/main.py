#You will be give a set of poll data called election_data.csv. 
#The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os 
import csv 

Vote_count = 0
Candidates = {}


Election_data_csv = os.path.join('PyPoll',"Resources","PyPoll_Resources_election_data.csv")

with open(Election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 

#The total number of votes cast
    for row in csvreader: 
        Vote_count = Vote_count + 1 

#A complete list of candidates who received votes
        if row [2] in Candidates: 
            Candidates[row[2]] += 1
        else: 
            Candidates[row[2]] = 1 

K_percent = "{:.3%}".format(Candidates['Khan'] / Vote_count)
C_percent = "{:.3%}".format(Candidates['Correy'] / Vote_count)
L_percent = "{:.3%}".format(Candidates['Li'] / Vote_count)
O_percent = "{:.3%}".format(Candidates["O'Tooley"] / Vote_count)
  
print("Election Results")
print("--------------------------")
print("Total Votes:", Vote_count)
print("--------------------------")
print("Khan:", (Candidates['Khan']), K_percent)
print("Correy:", (Candidates['Correy']), C_percent)
print("Li:", (Candidates['Li']), L_percent) 
print("O'Tooley:", (Candidates["O'Tooley"]), O_percent) 
print("--------------------------")
