#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
#(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#
#You will be give a set of poll data called election_data.csv. 
#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv

totVotes=0
candidates={}#dictionary to hold keyed pairs
cand_votes={}
win_votes=0

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv,newline="") as csvElection:
    csvreader=csv.reader(csvElection,delimiter=",")
    next(csvreader, None)  # skip the headers

    for row in csvreader:
        totVotes=totVotes+1#count each row basically
        cand=row[2] #declare 3rd row as candidate name
        if cand in candidates: #iterate through empty dictionary
            candidates[cand]=candidates[cand] +1# add one if 1 exists
        else:
            candidates[cand] =1# add one if not exist
#print(totVotes)
#   # print(row)
#print(candidates.items())# fucntion of the dictionary

for nominee,votes in candidates.items():# iterate through the candidates dictionary
    cand_votes[nominee]="{0:.3%}".format(votes/totVotes)# appending to new dictionary, first value will be "nominee" second will be the percent
    if votes>win_votes:# iterate through di
        win_votes=votes
        winner=nominee

#print(candidates)    
#print(cand_votes) 
#print(win_votes)
#print(winner)   

# print out results
print("Election Results")
print("..........................")
print(f"Total Votes: {totVotes}")
print("..........................")
for nominee, votes in candidates.items():
    print(f"{nominee}: {cand_votes[nominee]} ({votes})")
    
print("..........................")
print(f"Winner: {winner}")
print("..........................")


#- Replicate the to terminal and file



   
    
linebreak=".........................."
cg="\r\n"

f=open("ElectionResults.txt","w+")
f.write("Election Results"+cg)
f.write(linebreak+cg)
f.write(f"Total Votes: {totVotes}"+cg)
f.write(linebreak+cg)
for nominee, votes in candidates.items():
    f.write(f"{nominee}: {cand_votes[nominee]} ({votes})"+cg)
f.write(linebreak+cg)
f.write(f"Winner: {winner}"+cg)
f.write(linebreak)
f.close
    


    
    
#       profit= max(min_max, key=lambda row: int(row[1]))
#    loss= min(min_max, key=lambda row: int(row[1])),
#        
#The total number of votes cast
#
#A complete list of candidates who received votes
#
#The percentage of votes each candidate won
#
#The total number of votes each candidate won
#
#The winner of the election based on popular vote.