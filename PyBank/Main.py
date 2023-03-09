# This is the code for PyBank
#Import 
import os
import csv

# Path to collect data
bank_CSV = os.path.join("Resources", "budget_data.csv")
with open(bank_CSV, 'r') as f:
    reader =csv.reader(f,delimiter=",")
    header_row = next(f)

    for row in reader:
     