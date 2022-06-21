# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = '/Users/clarerobbins/Desktop/bootcamp/Challenges/Election_Analysis_Folder/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save teh file to a path.
file_to_save = '/Users/clarerobbins/Desktop/bootcamp/Challenges/Election_Analysis_Folder/Election_Analysis/analysis/election_analysis.txt'

# open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.