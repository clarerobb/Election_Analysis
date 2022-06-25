# Audit of Colorado Congressional Election Results with Python

## Overview of Election Audit

The following analysis is an election audit of the results from a recent congressional election for the Colorado Board of Elections. The election results were gathered from three voting methods and stored in a .csv file. The Colorado Board of Elections wanted Python script to run through the dataset. 

The code needed to do the follow:

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Get a complete list of each county where votes were cast.
  4. Calculate the voter turnout for each county.
  5. Calculate the percentage of votes from each county.
  6. Determine the county with the highest turnout.
  7. Calculate the total number of votes each candidate received.
  8. Calculate the percentage of votes each candidate won. 
  9. Determine the winner of the election based on the popular votes. 

## Data and Resources

Data source: The dataset is 'election_results.csv' and is composed of three columns: Ballot ID, County, and Candidate.<br/>
Software: Python 3.7.6, Visual Studio Code 1.68.1

## Model

After setting several variables to hold and track the data, I used the code below to loop through the data to calculate the total vote, candidates in the election, candidate votes, counties in the election, and county votes. I then printed the results to a text file.


    for row in reader:
    
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

## Election Audit Results

#### Total Votes 
- **369,711** votes were cast in the election.

#### County Votes
- **Jefferson County** represented **10.5%** of the total vote with **38,855** votes cast.
- **Denver County** represented **82.8%** of the total vote with **306,055** votes cast.
- **Arapahoe County** represented **6.7%** of the total vote with **24,801** votes cast.

#### Largest County Turnout
- **Denver County** had the largest voter turnout. 

#### Candidate Results
- **Charles Casper Stockham** received **23.0%** of the vote with **85,213** number of votes.<br/>
- **Diana DeGette** received **73.8%** of the vote with **272,892** number of votes.<br/>
- **Raymon Anthony Doane** received **3.1%** of the vote with **11,606** number of votes.<br/>

#### Winner
- **Diana DeGette** won the election with **73.8%** of the vote and **272,892** votes.

#### Election Result Printed in Terminal
![Election results in terminal](https://user-images.githubusercontent.com/106405775/175406242-48aab74b-a13f-4de1-a73b-40bee0b79b72.png)


#### Election Results Saved to a Text File
![Election results Saved to a Text File](https://user-images.githubusercontent.com/106405775/175407213-e302b4a6-1142-4049-8e2d-c1ce751cd645.png)


## Election Audit Summary
The audit certified the results of the election for a Colorado congressional district by reviewing the dataset and providing detailed votes counts for each candidate and county. 

This script automates the vote counting process and provides a detailed report of the results. It can also be easily modified to audit future elections. For example, the code could be modified to analyze additional elections by:
- changing the path to a different dataset, and
- updating variables according to the new dataset.

Additionally, by adding a few lines of code in the initial loop, this script could also calculate each candidates votes per county. 
