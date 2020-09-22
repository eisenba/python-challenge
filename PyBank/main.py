#PyBank challenge main script
# import modules
import os
import csv

# read csv

budget_data_file = os.path.join( 'Resources','02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(budget_data_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
