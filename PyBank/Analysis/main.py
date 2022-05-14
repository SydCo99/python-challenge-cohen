def budgetanalysis(): 
    #import dependencies
    import os
    import csv 
    import numpy as np 
    # path to collect data from resources folder 
    budgetdata_csv = os.path.join("PyBank/Resources/budget_data.csv")

    # Your task is to create a Python script that analyzes the records to calculate each of the following:

    # * The total number of months included in the dataset
    # * The net total amount of "Profit/Losses" over the entire period
    # * The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # * The greatest increase in profits (date and amount) over the entire period
    # * The greatest decrease in profits (date and amount) over the entire period

        

    # Read in the CSV file

    csvfile = open(budgetdata_csv, 'r') 

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header line 
    header = next(csvreader)

    #initialize variables 
    total_months_rows = []
    total_profitsandlosses = 0 
    period_revenue = []
    changes = 0 
    total_changes = 0
    average_changes = 0 
    changes_list = []
    changes_min = 0 
    changes_max = 0 
    changes_min_date = 0 
    changes_max_date = 0 

    # Loop through the data
    for row in csvreader:
        #find how many months 
        total_months_rows.append(row[0])
        total_months = len(total_months_rows)
        #find total profits and losses 
        total_profitsandlosses += int(row[1])
        #collect a list of revenues for each month 
        period_revenue.append(int(row[1]))
    #iterate through rows, starting at index 1 to include changes to first index value at 0 
    for i in range (1,len(total_months_rows)):
        #calculate month to month changes 
        changes = period_revenue[i] - period_revenue [i-1]
        changes_list.append(changes)
        total_changes += changes 
        #find the greatest increase and decrease in profits 
        if changes > changes_max:
            changes_max = changes
            changes_max_date = total_months_rows[i]
        if changes < changes_min: 
            changes_min = changes 
            changes_min_date = total_months_rows[i]


    #calculate average change over the period, after the for loop so the total changes list is complete 
    average_changes = total_changes/(len(total_months_rows)-1)

    #print statements - I included some that I used for debugging purposes so you could see the process 
    print("Thank you for choosing Sydney to run your budget analysis!")
    print("Analyzing....")
    print("------------------------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits/Losses is: ${total_profitsandlosses}")
    #print(f"Period Revenue List:  {period_revenue}")
    formatavgchanges = "{:.2f}".format(average_changes)
    print(f"Average Changes is: ${formatavgchanges}")
    #print(f"Minimun change is: {changes_min}")
    #print(f"Maximum change is: {changes_max}")
    #print(f"Changes max date: {changes_max_date}")
    #print(f"Changes min date: {changes_min_date}")
    print(f"Greatest Increase In Profits: {changes_max_date} (${changes_max})")
    print(f"Greatest Decrease In Profits: {changes_min_date} (${changes_min})")
    print("------------------------------------------------------------------")

budgetanalysis()

import sys

original_stdout = sys.stdout # Save a reference to the original standard output

with open('pybankoutput.txt', 'w') as pybankoutput:
    sys.stdout = pybankoutput # Change the standard output to the file we created.
    budgetanalysis()
    #print("Thank you for choosing Sydney to run your budget analysis!")
    #print("Analyzing....")
    #print("------------------------------------------------------------------")
    #print("Financial Analysis")
    #print("------------------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits/Losses is: ${total_profitsandlosses}")
    print(f"Average Changes is: ${formatavgchanges}")
    print(f"Greatest Increase In Profits: {changes_max_date} (${changes_max})")
    print(f"Greatest Decrease In Profits: {changes_min_date} (${changes_min})")
    sys.stdout = original_stdout # Reset the standard output to its original value