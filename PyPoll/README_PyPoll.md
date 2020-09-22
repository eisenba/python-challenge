# PyPoll Challenge
This portion of the project analyzes the votes in an election, returns the vote totals for each candidate, and identifies the winner. Below is a list of the values returned and a list of the included files.
**Caution: running main.py will overwrite the existing output. If you would like to keep the existing output, copy PyBank_output.txt to a new file location.**

## Inputs
**02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv :** 
  - This csv contains vote for each voter who participated in the election.
  - The first column contains the voter ID for the voter who cast the vote.
  - The second column contains the county of the voter.
  - The third column contains the last name of the Candidate that the voter voted for.
  
## Outputs
**PyPoll_output.txt :**
  - The following values are also returned in the terminal when main.py runs
  - Total Votes: The total number of votes cast
  - A complete list of candidates who received votes
  - The percentage of votes each candidate received
  - The total number of votes each candidate received
  - The winner of the election based on popular vote.
  
## Files and Directories
1. Main.py
   - Python script that completes analysis
2. Resources
   - Directory contains the input csv file. 
   - input csv must be in this directory and must be named 02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv
3. analysis
    - Directory contains the output txt file.
    - PyPoll_output.txt contains the output values. This file is overwritten during each run of main.py
