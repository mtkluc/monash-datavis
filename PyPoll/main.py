# import os and csv and path
import os
import csv

votes_csv = os.path.join("Resources", "election_data.csv")

# lists - for each candidate
candidate = []
vote_count = []
percent_vote = []
total_vote = 0

# open CSV
with open(votes_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # remove header
    csvheader=next(csvfile)

    #go through row
    for row in csvreader:
        # add candidate
        if row[2] not in candidate:
            candidate.append(row[2])
            candidate_index = candidate.index(row[2])
            vote_count.append(1)
        else:
            candidate_index = candidate.index(row[2])
            vote_count[candidate_index] +=1

    # identify total votes
    for i in vote_count:
        total_vote = total_vote + int(i)
    
    # percent calc
    for x in vote_count:
        perc_vote = round((100*x / total_vote), 3)
        percent_vote.append(perc_vote)

        # identify max votes
    max_votes = max(vote_count)
    max_vote_index = vote_count.index(max_votes)
    winner = candidate[max_vote_index]

# print output
print(f"Election results")
print(f"----------------------------------------")
print(f"Total votes: {str(total_vote)}")
print(f"----------------------------------------")
for x in range(len(candidate)):
    print(f"{str(candidate[x])}: {str(percent_vote[x])}% ({str(vote_count[x])})")
print(f"----------------------------------------")
print(f"Winner: {winner}")
print(f"----------------------------------------")

# text output
with open(os.path.join("Analysis", "VoteAnalysis.txt"), "w") as f:
	f.write(f"Election Results\n")
	f.write(f"----------------------------------------\n")
	f.write(f"Total votes: {str(total_vote)}\n")
	f.write(f"----------------------------------------\n")

with open(os.path.join("Analysis", "VoteAnalysis.txt"), "a") as f:
    for x in range(len(candidate)):
        f.write(f"{str(candidate[x])}: {str(percent_vote[x])}% ({str(vote_count[x])})\n")

with open(os.path.join("Analysis", "VoteAnalysis.txt"), "a") as f:
    f.write(f"----------------------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"----------------------------------------\n")