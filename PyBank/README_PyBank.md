# PyBank Challenge
This portion of the project analyzes the financial records of company and returns some summary statistics for the financial records. Below is a list of the values returned and a list of the included files.
**Caution: running main.py will overwrite the existing output. If you would like to keep the existing output, copy PyBank_output.txt to a new file location.**

## Inputs
**02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv :** 
  - This csv contains the monthly financial data for the company.
  - The first column contains the month in this format: "[three-letter month abbreviation]-YYYY".
  - The second column contains the monthly profit or loss.
  
## Outputs
**PyBank_output.txt :**
  - The following values are also returned in the terminal when main.py runs
  - Total Months: The total number of months included in the dataset
  - Total: The net total amount of "Profit/Losses" over the entire period 
  - Average Change: The average of the changes in "Profit/Losses" over the entire period
  - Greatest Increase in Profits: The greatest increase in profits (date and amount) over the entire period
  - Greatest Decrease in Profits: The greatest decrease in losses (date and amount) over the entire period
  
## Files and Directories
1. Main.py
   - Python script that completes analysis
2. Resources
   - Directory contains the input csv file. 
   - input csv must be in this directory and must be named 02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv
3. analysis
    - Directory contains the output txt file.
    - PyBank_output.txt contains the output values. This file is overwritten during each run of main.py
  
