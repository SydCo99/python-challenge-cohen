def polanalysis(): 
    #import dependences 
    import os
    import csv 
    import numpy as np 


    election_data_csv = os.path.join("PyPoll/Resources/election_data.csv")

    # Read in the CSV file

    csvfile = open(election_data_csv, 'r') 

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header line 
    header = next(csvreader)

    #initialize variables 
    total_votes_rows = []
    candidate_list = []
    candidate_vote_totals = {}
    votes_for_percentages = []
    winner = "none"

    # Loop through the data
    for row in csvreader:
        # The total number of votes cast
        total_votes_rows.append(row[0])
        total_votes = len(total_votes_rows)
        #A complete list of candidates who received votes
        #The total number of votes each candidate won
        if row[2] not in candidate_list: 
            candidate_list.append(row[2])
            candidate_vote_totals.update({row[2]: 1})
        else: 
            candidate_vote_totals[row[2]] += 1

    # * The percentage of votes each candidate won
    for key in candidate_vote_totals.keys(): 
        votes_for_percentages.append(candidate_vote_totals[key])
    percents = []
    for votes in votes_for_percentages:
        percents.append((votes/total_votes)*100)
    completed_dict = {candidate_list[0]: [votes_for_percentages[0], percents[0]],
                    candidate_list[1]: [votes_for_percentages[1], percents[1]],
                    candidate_list[2]: [votes_for_percentages[2], percents[2]]
                    }
    #The winner of the election based on popular vote.
    for percent in percents:
        if percents[0] > percents[1] and percents[2]:
            winner = "Charles Casper Stockham"
            #print("Charles Casper Stockham is the winner!")
        elif percents[1] > percents[0] and percents[2]:
            #print("Diana DeGette is the winner!")
            winner = "Diana DeGette"
        elif percents[2] > percents[0] and percents[1]:
            #print("Raymon Anthony Doane is the winner!")
            winner = "Raymon Anthony Doane"
            
        

    print(f"Thank you for choosing Sydney to run your polling analysis!")
    print(f"--------------------------------------------------------------")
    print(f"Election Results")
    print(f"--------------------------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------------------------------------------------")
    print(f"Charles Casper Stockham: {completed_dict[candidate_list[0]]}")
    print(f"Diana DeGette: {completed_dict[candidate_list[1]]}")
    print(f"Raymon Anthony Doane: {completed_dict[candidate_list[2]]}")
    print(f"--------------------------------------------------------------")
    print(f"Winner: {winner}")
    print(f"--------------------------------------------------------------")

polanalysis()

import sys

original_stdout = sys.stdout # Save a reference to the original standard output

with open('pypolloutput.txt', 'w') as pypolloutput:
    sys.stdout = pypolloutput # Change the standard output to the file we created.
    polanalysis()
    #print(f"Thank you for choosing Sydney to run your polling analysis!")
    #print(f"--------------------------------------------------------------")
    #print(f"Election Results")
    #print(f"--------------------------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------------------------------------------------")
    print(f"Charles Casper Stockham: {completed_dict[candidate_list[0]]}")
    print(f"Diana DeGette: {completed_dict[candidate_list[1]]}")
    print(f"Raymon Anthony Doane: {completed_dict[candidate_list[2]]}")
    print(f"--------------------------------------------------------------")
    print(f"Winner: {winner}")
    print(f"--------------------------------------------------------------")   
    sys.stdout = original_stdout # Reset the standard output to its original value