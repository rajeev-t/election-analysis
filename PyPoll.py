import csv
import os

#Data to retrieve 

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# intialize total vote accumulator
total_votes = 0

# create a list for candidates 
candidates = list()

# declare a dictionary for votes per candidate
candidate_votes = dict()

# declaring winner stats
winner = ""
winner_vote_count = 0
winner_vote_percent = 0

with open(file_to_load) as election_data:

# To do: perform analysis.
    file_reader = csv.reader(election_data)

    # read header row
    headers = next(file_reader)     

    # print each row in .csv file
    for row in file_reader:
        #print(row)

        # increment total votes
        total_votes += 1

        # add each candidate to the candidates[] list
        candidate = row[2]

        if candidate not in candidates:
            
            candidates.append(candidate)

            # instantiating candidate as a key with 0 votes (at the beginning)
            candidate_votes[candidate] = 0

        # increment candidate's vote count
        candidate_votes[candidate] += 1

# 1. Total # of votes cast

#print(total_votes)

# 2. Complete list of candidates who recieved votes

#print(candidates)

# 3. Total # of votes each candidate won

#print(candidate_votes)

# 4. % of votes each candidate won

for candidate in candidate_votes:
    
    # gather vote count per candidate
    indie_votes = candidate_votes[candidate]

    # calculate % of votes per candidate
    vote_percent = float(indie_votes) / float(total_votes) * 100

    #print(f"{candidate} received {vote_percent:.1f}% of the votes.")
    print(f"{candidate}: {vote_percent:.1f}% ({indie_votes:,})\n")

# 5. Winner of election based on popular vote

    if (indie_votes > winner_vote_count) and (vote_percent > winner_vote_percent):

        winner_vote_count = indie_votes
        winner_vote_percent = vote_percent
        winner = candidate

winner_summary = (
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winner_vote_count:,}\n"
    f"Winning Percentage: {winner_vote_percent:.1f}%\n"
    f"----------------------------\n"
)

print(winner_summary)

with open(file_to_save, "w") as txt_file:
    
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")