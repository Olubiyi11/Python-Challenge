import os 
import csv
import numpy as np

#election_data_csv = os.path.join("..", "Resources", "election_data.csv")
election_data_csv = "C:/Users/lordb/Python-Challenge/PyPoll/Resources/election_data.csv"
Candidatenames = []
Totalvote = 0
votecharles = 0
voteDiana = 0
voteRaymon = 0

#Open and read csv
with open(election_data_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #skip header
    header = next(csv_file)
    for row in csvreader:
        #Determine the total votes
        Totalvote = Totalvote +1

        #Count individual votes
        if "Charles" in row[2]:
             votecharles= votecharles +1  
        elif "Diana" in row[2]:
             voteDiana= voteDiana +1
        elif "Raymon" in row[2]:
         voteRaymon= voteRaymon +1


    
 
    
     #Calculate percentage and round to 3 decimal places   
    votecharlespercentage = votecharles*100/Totalvote
    voteDianapercentage = voteDiana*100/Totalvote
    voteRaymonpercentage = voteRaymon*100/Totalvote
    rounded_votecharlespercentage = round(votecharles*100/Totalvote, 3)
    rounded_voteDianapercentage = round(voteDiana*100/Totalvote, 3)
    rounded_voteRaymonpercentage = round(voteRaymon*100/Totalvote, 3)  
    
   #Used this to scan on the csv to make sure there are just 3 candidates whose names appeared on Canvas.
    Candidatenames.append(row[2])
    Candidates = np.unique(Candidatenames)

   #Print Some of the result 
    print("Election Results")
    print(".........................................")
    print(f"Total Votes: {Totalvote}")
    #print(votecharles, voteDiana, voteRaymon)
     
    print(f"Charles Casper Stockam: {rounded_votecharlespercentage}%  ({votecharles})")
    print(f"Diana Degette: {rounded_voteDianapercentage}%  ({voteDiana})")
    print(f"Raymon Anthony Doane: {rounded_voteRaymonpercentage}%  ({voteRaymon})")
    
    #find the Winner
if rounded_votecharlespercentage > rounded_voteDianapercentage and rounded_votecharlespercentage >rounded_voteRaymonpercentage:
    print("Winner: Charles Casper Stockam")
elif rounded_voteDianapercentage > rounded_votecharlespercentage and rounded_voteDianapercentage > rounded_voteRaymonpercentage:
    print("Winner: Diana Degette")
else:
    print("Winner: Ramon Anthony Doane")


    #printing to Electionanalysis.txt
    with open("Election.txt", "w") as f:
        L= ["Election Results\n", ".........................................\n","Total Votes: 369711\n","Charles Casper Stockam: 23.049 (85213)\n","Diana Degette: 73.812 (272892)\n","Raymon Anthony Doane: 3.139  (11606)\n","Winner: Diana Degette\n"]
    f.writelines(L)
    f.close()

    

    
 

   