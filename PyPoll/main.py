# Import dependencies
import os, csv
from pathlib import Path
# Assign file location
csvpath = os.path.join("Resources/election_data.csv")
# Declare Variables
total_votes = 0
Doane_votes = 0
Stockham_votes = 0
DeGette_votes = 0

with open(csvpath,newline="", encoding="utf-8") as elections:
   
    csvreader = csv.reader(elections,delimiter=",")
    header=next(csvreader)
   # print(header)
    for row in csvreader:
       
        total_votes +=1
       # print(row[2])
        # We have 3 candidates if the name is found, count the times it appears and store in a list
       
        if row[2] == "Charles Casper Stockham":
            Stockham_votes += 1
        elif row[2] == "Diana DeGette":
            DeGette_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_votes += 1
 # Find the winner! 
candidates = ["DeGette", "Doane", "Stockham"]
votes = [DeGette_votes, Doane_votes, Stockham_votes]
# We zip them together the list of candidate(key) and the total votes(value)
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

DeGette_percent = (DeGette_votes/total_votes) *100
Doane_percent = (Doane_votes/total_votes) * 100
Stockham_percent = (Stockham_votes/total_votes)* 100
# Print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Doane: {Doane_percent:.3f}% ({Doane_votes})")
print(f"Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")
output_file = Path("Elections_Results_Summary.txt")
with open(output_file,"w") as file:
# Write methods to print to Elections_Results_Summary
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
    file.write("\n")
    file.write(f"Doane: {Doane_percent:.3f}% ({Doane_votes})")
    file.write("\n")
    file.write(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")