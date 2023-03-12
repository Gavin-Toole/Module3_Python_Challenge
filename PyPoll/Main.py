# This is the code for PyPoll
# import dependances
import os
import csv

# Path to collect and output data
pollcsv_path = os.path.join("Resources", "election_data.csv")
wpath =os.path.join("PyPoll_Analysis","election_results.txt")

# Define varibiles

tvotes = 0

# Candidates 
candidates = []
vcandidates = {}

wcandidate = ""
wcandidatev = 0

# Open Election Data file and skip header row
with open(pollcsv_path, 'r') as f:
    reader = csv.reader(f, delimiter=",")
        
    header_row = next(f)


# Read through file and calcuate total votes cast and Cadidate name

    for row in reader:
        
        tvotes = tvotes + 1
        ncandidates = row[2]
        

# Check and set Candidate list
        if ncandidates not in candidates:
            candidates.append(ncandidates)
            vcandidates[ncandidates] = 0
        
# Calcuate votes
        vcandidates[ncandidates] = vcandidates[ncandidates] + 1

# # Save to file
with open(wpath, "w") as output:
    Results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes : {tvotes}\n"
        f"----------------------\n"
     )

# Print Total Votes                
    print(Results)

# Save to file
    output.write(Results)
    

# Determine Winners
    for win in vcandidates:

        votes = vcandidates.get(win)
        votep = float(votes) / float(tvotes) * 100

        if (votes > wcandidatev):
            wcandidatev = votes
            wcandidates = win

        voteout = f"{win}: {votep:.3f}% ({votes})\n"    
# Print State Winners
        print(voteout)
#Save to file
        output.write(voteout)

    Winning_Cand = (
        f"-------------------------------\n"
        f"Winner: {wcandidates}\n"
        f"-------------------------------\n"
    )
    print(Winning_Cand)
    output.write(Winning_Cand)
