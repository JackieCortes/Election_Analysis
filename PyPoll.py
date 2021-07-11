#Add our dependencies
import csv
import os
#The data we need to retrieve
  # Assign a variable for the file to load and the path.
file_to_load = os.path.join("ResourcesPP", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# with open(file_to_save, "w") as txt_file:
# # Write three counties to the file.
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("_________________________\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")


# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print the header row
    headers=next(file_reader)
    print(headers)
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)




#1. The total number of votes cast.
#2. A complete list of candidates who received votes
#3. The % of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election bases on popular vote.
# Close the file.
#election_data.close()