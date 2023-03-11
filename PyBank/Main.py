# This is the code for PyBank
#Import 
import os
import csv

# Path to collect and output data
bankcsv_path = os.path.join("Resources", "budget_data.csv")
wpath = os.path.join("PyBank_Analysis,Budget_Analysis.txt")

# Define varibles
tmonths = 0
prev_rev = 0
months = []
rev_chng_lt = []
grest_incr= ["", 0]
grest_decr =["", 99999999999999999]
trev = 0
# Open Bank Data file and ingore the header row
with open(bankcsv_path, 'r') as f:
    csv_reader =csv.reader(f,delimiter=",")
    header_row = next(f)
   
    for row in csv_reader:
# Calcualte totals 
        tmonths = tmonths + 1
        trev = trev + int(row[1])

# Revenue Change
        rev_chng = int(row[1]) - prev_rev
        prev_rev = int(row[1])
        rev_chng_lt = rev_chng_lt + [rev_chng]
       # months = months + int(row[0])
#  # Greatest increase
        if rev_chng > grest_incr[1]:
            grest_incr[0] = row[0]
            grest_incr[1] = rev_chng

#  # Greatest descress
        if rev_chng < grest_decr[1]:
            grest_decr[0] = row[0]
            grest_decr[1] = rev_chng     

# # Average Revenue Change
rev_avg = (sum(rev_chng_lt) / tmonths)

       
        
print("Financial Analysis")
print("---------------------")
print(f"Total months:  {tmonths} ")
print(f"Total: ${trev}")
print(f"Average Change: ${rev_avg}")
print(f"Greatest Increase in Profit: {grest_incr[0]} (${grest_incr[1]})")
print(f"Greatest Decrease in Profits: {grest_decr[0]} (${grest_decr[1]})")      

# write to file to folder
with open(wpath, "w") as output:

    output.write("Financial Analysis")
    output.write("---------------------")
    output.write(f"Total months:  {tmonths} ")
    output.write(f"Total: ${trev}")
    output.write(f"Average Change: ${rev_avg}")
    output.write(f"Greatest Increase in Profit: {grest_incr[0]} (${grest_incr[1]})")
    output.write(f"Greatest Decrease in Profits: {grest_decr[0]} (${grest_decr[1]})") 
