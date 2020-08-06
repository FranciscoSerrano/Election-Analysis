import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "electiona_analysis.txt")
#Open the election results and read the file.
with open(file_to_load) as election_data:

    #TO DO: Perform Analyis

    print(election_data)

with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")

