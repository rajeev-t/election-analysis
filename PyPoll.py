import csv
import os

#Data to retrieve 

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

# To do: perform analysis.
    file_reader = csv.reader(election_data)

     #print each row in .csv file
    headers = next(file_reader)
    print(headers)

# 1. Total # of votes cast
# 2. Complete list of candidates who recieved votes
# 3. Total # of votes each candidate won
# 4. % of votes each candidate won
# 5. Winner of election based on popular vote

with open(file_to_save, "w") as txt_file:
    
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")