# Audit of Colorado Congressional Election Results with Python

## Overview of Election Audit

The following analysis is an election audit of the results from a recent local congressional election for employees of the Colorado Board of Elections. The election results was stored in a .csv file, and the employees wanted Python script to run through the dataset. 

The code needed to do the follow:

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Get a complete list of each county where votes were cast.
  4. Calculate the voter turnout for each candidate.
  5. Calculate the percentage of votes from each count out of the total count.
  6. Determine the county with the highest turnout.
  7. Calculate the total number of votes each candidate received.
  8. Calculate the percentage of votes each candidate won. 
  9. Determine the winner of the election based on the popular votes. 

## Data and Resources

Data source: election_results.csv<br/>
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
- 369,711 votes were cast in the election.

#### County Votes
- **Jefferson County** represented **10.5%** of the total vote with **38,855** votes cast.
- **Denver County** represented **82.8%** of the total vote with **306,055** votes cast.
- **Arapahoe County** represented **6.7%** of the total vote with **24,801** votes cast.

#### Largest County Turnout
- Denver County had the largest voter turnout. 

#### Candidate Results
- **Charles Casper Stockham** received **23.0%** of the vote with **85,213** number of votes.<br/>
- **Diana DeGette** received **73.8%** of the vote with **272,892** number of votes.<br/>
- **Raymon Anthony Doane** received **3.1%** of the vote with **11,606** number of votes.<br/>

#### Winner
- **Diana DeGette** won the election with **73.8%** of the vote and **272,892** votes.

#### Election Result Printed in Terminal
![Election results in terminal](https://user-images.githubusercontent.com/106405775/175406242-48aab74b-a13f-4de1-a73b-40bee0b79b72.png)


#### Election Results Saved to a Text File
![Election results Saved to a Text File](https://user-images.githubusercontent.com/106405775/175407213-e302b4a6-1142-4049-8e2d-c1ce751cd645.png)|


## Election Audit Summary


