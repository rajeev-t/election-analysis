import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# intialize total vote accumulator
total_votes = 0

# create a list for candidates/counties
candidates = list()
counties = list()

# declare a dictionary for votes per candidate/county
candidate_votes = dict()
county_votes = dict()

# declaring winner stats
winner = ""
winner_vote_count = 0
winner_vote_percent = 0

winner_county = ""
winner_c_vote_count = 0
winner_c_vote_percent = 0

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

        # add each county to the counties[] list
        county = row[1]

        if county not in counties:
            
            counties.append(county)

            # instantiating county as a key with 0 votes (at the beginning)
            county_votes[county] = 0

        # increment county's vote count
        county_votes[county] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n"
    )

    print(election_results, end="")
    txt_file.write(election_results)

    for candidate in candidate_votes:
        
        # gather vote count per candidate
        indie_votes = candidate_votes[candidate]

        # calculate % of votes per candidate
        vote_percent = float(indie_votes) / float(total_votes) * 100

        candidate_results = (f"{candidate}: {vote_percent:.1f}% ({indie_votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

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
    txt_file.write(winner_summary)

    for county in county_votes:
        
        # gather vote count per county
        each_county_votes = county_votes[county]

        # calculate % of votes per candidate
        county_vote_percent = float(each_county_votes) / float(total_votes) * 100

        county_results = (f"{county}: {county_vote_percent:.1f}% ({each_county_votes:,})\n")

        print(county_results)
        txt_file.write(county_results)

        if (each_county_votes > winner_c_vote_count) and (county_vote_percent > winner_c_vote_percent):

            winner_c_vote_count = each_county_votes
            winner_c_vote_percent = county_vote_percent
            winner_county = county

    winner_c_summary = (
        f"----------------------------\n"
        f"County with Highest Turnout: {winner_county}\n"
        f"Highest Vote Count: {winner_c_vote_count:,}\n"
        f"Highest Vote Percentage: {winner_c_vote_percent:.1f}%\n"
        f"----------------------------"
    )

    print(winner_c_summary)
    txt_file.write(winner_c_summary)