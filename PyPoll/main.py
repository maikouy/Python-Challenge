#Import file/ open the file to CHANGE 
import os
import csv

#Path to collect data from the Resource folder
election_data = os.path.join("Resources", "election_data.csv")
#print(election_data)

#Indicate values
voter_id = []
county = []
candidate = []
candidate_name = []
votes = []

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


with open(election_data, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    #print(csv_header)

    #Start the loop:
    for row in csvreader:
        #print(row)

        voter_id.append(int(row["Voter ID"]))
        county.append(row["County"])
        candidate.append(row["Candidate"])

        #Calculate the number of votes casted:
        #print(len(voter_id)) 

        #Indicate the candidates
        #candidate_name = row["Candidate"]

        #Loop through the "Candidate" list to categorize each name to a diff list
        if row["Candidate"] == "Khan":
            khan_votes += 1
        elif row["Candidate"] == "Correy":
            correy_votes += 1
        elif row["Candidate"] == "Li":
            li_votes += 1
        elif row["Candidate"] == "O'Tooley":
            otooley_votes += 1

#The total number of votes casted:
print(len(voter_id))

#Now, focus only on candidate category and their number of votes
#zip both categories to one csv:
candidates_and_votes = {"Khan", "Correy", "Li", "O'Tooley"} 
votes = ["khan_votes", "correy_votes", "li_votes", "otooley_votes"]

#zip all 2 lists together:
list = zip(candidates_and_votes, votes)

#save the output file path to a 'Write' csv file:
output_path = os.path.join("final.csv")

with open(output_path, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Candidate", "Votes"])
    writer.writerows(list)
 
print(votes)
#A complete list of candidates who received votes:
print(candidates_and_votes)
#The total number of votes each candidate won:
print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)

#Get the percentage of votes for each (4) candidates:
khan_percent = (khan_votes/(len(voter_id))) * 100
print(khan_percent)
correy_percent = (correy_votes/(len(voter_id))) * 100
print(correy_percent)
li_percent = (li_votes/(len(voter_id))) * 100
print(li_percent)
otooley_percent = (otooley_votes/(len(voter_id))) * 100
print(otooley_percent)



#Analysis
print(f'Election Results')
print(f'------------------------------------')
print(f'Total Votes:' + str(len(voter_id)))
print(f'-------------------------------------')
print(f'Khan:' + str(khan_percent) + '%' + "(" + str(khan_votes) + ")")
print(f'Correy:' + str(correy_percent) + '%' + "(" + str(correy_votes) + ")") 
print(f'Li:' + str(li_percent) + '%' + "(" + str(li_votes) + ")") 
print(f'O''Tooley:' + str(otooley_percent) + '%' + "(" + str(otooley_votes) + ")") 
print(f'------------------------------------')
print(f'Winner:' 'Khan')
print(f'------------------------------------')
    
    