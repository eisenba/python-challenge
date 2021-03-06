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

 # count votes
with open(poll_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader, None)
    for row in csvreader:
        for i in results:
            if results[i]['name'] == row[2]:
                results[i]['vote_count'] += 1
                row_count += 1    
csvfile.close()

# find winner
winner = ''
winner_count = 0
for i in results:
    if results[i]['vote_count'] > winner_count:
        winner = results[i]['name']
        winner_count = results[i]['vote_count']
    elif results[i]['vote_count'] == winner_count:
        winner = "There is a tie"
        winner_count = results[i]['vote_count']

# Print results to terminal
print(f"""Election Results \n 
-------------------------- \n 
Total Votes: {row_count} \n 
-------------------------- \n """)

for i in results:
    print(f"{results[i]['name']} : {(results[i]['vote_count']/row_count)*100}% ({results[i]['vote_count']})")

print(f"""-------------------------- \n 
Winner: {winner}""")

# create text file
output_file = os.path.join("Analysis", 'PyPoll_output.txt')

# write results to text file
with open(output_file, 'w') as txtfile:
    txtfile.write(f"""Election Results \n 
-------------------------- \n 
Total Votes: {row_count} \n 
-------------------------- \n """)
txtfile.close()

with open(output_file, 'a') as txtfile:
    for i in results:
        txtfile.write(f"{results[i]['name']} : {(results[i]['vote_count']/row_count)*100}% ({results[i]['vote_count']}) \n")

    txtfile.write(f"""-------------------------- \n 
Winner: {winner}""")
    txtfile.close()
print("Output saved as Analysis/PyPoll_output.txt")