# This is the code for PyPoll
# import dependances
import os
import csv

# Path to read csv
poll_csv = os.path.join("Resources", "election_data.csv")

# Read csv
with open(poll_csv, 'r') as f:
    reader = csv.reader(f, delimiter=",")
    header_row = next(f)
    
    for row in reader:
        print(row)
