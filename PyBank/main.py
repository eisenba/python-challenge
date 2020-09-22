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
        # counts the month
        row_count += 1
        # adds change to total
        net_change += int(row[1])
        # appends change to list of changes
        changes.append(int(row[1]))
        # checks for max increase
        if int(row[1]) > int(max_change[1]):
            max_change = row
        # checks for max descrease
        elif int(row[1]) < int(min_change[1]):
            min_change = row
    #print(max_change)
    csvfile.close()
# Calculate average change
avg_change = (changes[row_count - 1] - changes[0]) / (row_count -1)
print(max_change)
print(min_change)
#print(avg_change)
# print results to terminal
print(f"""Financial Analysis \n
        ------------------------- \n
        Total Months:   {row_count} \n 
        Total Change:   {net_change} \n 
        Average Change: {avg_change} \n 
        Greatest Increase in Profits: {max_change[0]} ({max_change[1]}) \n 
        Greatest Decrease in Profits: {min_change[0]} ({min_change[1]}) """)


# create text file
output_file = os.path.join("Analysis", 'PyBank_output.txt')

# write results to text file
with open(output_file, 'w') as txtfile:
    txtfile.write(f"""Financial Analysis \n
        ------------------------- \n
        Total Months:   {row_count} \n 
        Total Change:   {net_change} \n 
        Average Change: {avg_change} \n 
        Greatest Increase in Profits: {max_change[0]} ({max_change[1]}) \n 
        Greatest Decrease in Profits: {min_change[0]} ({min_change[1]}) """)
    txtfile.close()
print("Output saved as Analysis/PyBank_output.txt")