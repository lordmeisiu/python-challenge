import os
import csv
from unicodedata import name

#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
csvfile = path + "\\Resources\\election_data.csv"
csvfile_1 = path + "\\analysis\\analysis.txt"

with open(csvfile_1,'w') as analysis_output:
    with open(csvfile, encoding = 'utf') as election_csv: #assign variable to csv file
        csvreader = csv.reader(election_csv, delimiter=",")

        header = next(csvreader)
        #print(header)

        vote_count = 0
        charles_vote_count = 0
        diana_vote_count = 0
        raymon_vote_count = 0

        for row in (csvreader):
            vote_count +=1
        
            for x in row:
                if x == 'Charles Casper Stockham':
                    charles_vote_count +=1
                elif x == 'Diana DeGette':
                    diana_vote_count +=1
                elif x == 'Raymon Anthony Doane':
                    raymon_vote_count +=1

                Winner = max(charles_vote_count,diana_vote_count,raymon_vote_count)
        
        charles_percentage = round((charles_vote_count/vote_count)*100,3)
        diana_percentage = round((diana_vote_count/vote_count)*100,3)
        raymon_percentage = round((raymon_vote_count/vote_count)*100,3)
            
        print("Election Results")
        print("------------------")
        print("Total votes: " + str(vote_count))
        print("------------------")
        print("Charles Casper Stockham: " + str(charles_percentage) + "% " + "(" + str(charles_vote_count) + ")")
        print("Diana DeGette: " + str(diana_percentage) + "% " + "(" + str(diana_vote_count) + ")")
        print("Ramon Anthony Doane: " + str(raymon_percentage) + "% " + "(" + str(raymon_vote_count) + ")")
        print("------------------")
        if Winner == charles_vote_count:
            print("Winner: " + "Charles Casper Stockham")
        elif Winner == diana_vote_count:
            print("Winner: " + "Diana DeGette")
        elif Winner == raymon_vote_count:
            print("Winner: " + "Ramon Anthony Doane")
        print("------------------")

    out_1 = f'\nElection Results\n\n------------------------------\n\nTotal votes: {vote_count}\n\n------------------------------\n'
    out_2 = f'\nCharles Casper Stockholm: {charles_percentage}% ({charles_vote_count})\n'
    out_3 = f'\nDiana DeGette: {diana_percentage}% ({diana_vote_count})\n'
    out_4 = f'\nRaymon Anthony Doane: {raymon_percentage}% ({raymon_vote_count})\n'
    out_5 = f'\n------------------------------\n\nWinner: {Winner}\n\n------------------------------'
    analysis_output.write(out_1)
    analysis_output.write(out_2)
    analysis_output.write(out_3)
    analysis_output.write(out_4)
    analysis_output.write(out_5)
analysis_output.close()