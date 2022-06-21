# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = '/Users/clarerobbins/Desktop/bootcamp/Challenges/Election_Analysis_Folder/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save teh file to a path.
file_to_save = '/Users/clarerobbins/Desktop/bootcamp/Challenges/Election_Analysis_Folder/Election_Analysis/analysis/election_analysis.txt'

# 1. The total number of votes cast
# a. Inialize a total vote counter.
total_votes = 0 

# Candidate Options
candidate_options = []

# Candidate Votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0 

# open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #b. Add to the total vote coutn.
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) *100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Determine winning vote count and candidate
# Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count and winning_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # set the winning_candidate equal to teh candidate's name
                winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

