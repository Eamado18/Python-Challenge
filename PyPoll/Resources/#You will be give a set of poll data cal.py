#You will be give a set of poll data called election_data.csv. 
#The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os 
import csv 

Vote_count = 0
Candidates = {1: {'Name':'Khan', 'Votes': '2218231'}, 2: {'Name': 'Correy', 'Votes': '704200'}, 3: {'Name': 'Li', 'Votes': '492940'}, 4: {'Name': "O'Tooley", 'Votes': '105630'}} 

Election_data_csv = os.path.join('PyPoll',"Resources","PyPoll_Resources_election_data.csv")

with open(Election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 

#The total number of votes cast
    for row in csvreader: 
        Vote_count = Vote_count + 1 

#A complete list of candidates who received votes
  

print("Election Results")
print("--------------------------")
print("Total Votes:", Vote_count)
print("--------------------------")
print(Candidates)

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.