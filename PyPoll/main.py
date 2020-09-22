# PyPoll challenge main script
# import dependencies
# import modules
import os
import csv

# read csv
poll_file = os.path.join( 'Resources','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

# create row counter to count total votes
row_count= 0
# create results dictionary to store results for each candidate
results = {}
cands = []

with open(poll_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader, None)

    for row in csvreader:
        if row[2] not in cands:
            cands.append(row[2])
csvfile.close()  
    # add candidates to results dictionary
for i in cands:
        cand_dict = dict(name = i, vote_count = 0)
        results[i] = cand_dict
    #print(results)
    #print(results['Khan']['vote_count'])
    # count votes
with open(poll_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader, None)
    for row in csvreader:
        for i in results:
            if results[i]['name'] == row[2]:
                results[i]['vote_count'] += 1
    print(results)
        



        
