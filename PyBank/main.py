#PyBank challenge main script
# import modules
import os
import csv

# read csv
budget_data_file = os.path.join( 'Resources','02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# create row counter to count total months
row_count= 0
# create net_change to track total net change
net_change= 0
# creatae changes to store mothly change
changes = []
# creates max_change to store month with greatest increase
max_change= ['',0]
# creates min_change to store month with greatest decrease
min_change= ['',0]

with open(budget_data_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader, None)

    for row in csvreader:
        # print(row)
        row_count += 1
        # print(row_count)
        net_change += int(row[1])
        # print(net_change)
        changes.append(row[1])
        # print(changes)
        if int(row[1]) > int(max_change[1]):
            max_change = row
        # comment
        elif int(row[1]) < int(min_change[1]):
            min_change = row
    print(max_change)
    print(min_change)
