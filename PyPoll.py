#Add our dependencies
import csv
import os
#The data we need to retrieve
  # Assign a variable for the file to load and the path.
file_to_load = os.path.join("ResourcesPP", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Candidate Options
candidate_options = []

# Declare a total vote counter.
total_votes = 0

# Declare the empty dictionary (votes by candidate)
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Read the header row
    headers=next(file_reader)
    
    # # Print each row in the CSV file.
    for row in file_reader:
      # 2. Add to the total vote count.
        total_votes += 1
      # Print the candidate name from each row.
        candidate_name = row[2]
     
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
     
          # Add the candidate name to the candidate list.
          candidate_options.append(candidate_name)

          #Begin trackint that candidate's vote count
          candidate_votes[candidate_name]=0  
        
        #Add a vote to that specific candidate
        candidate_votes[candidate_name]+=1

# Print the candidate list. 
#{'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
#print(candidate_votes)

#Print the total votes (the total sum for the for iteration. Result:369711)
#print(total_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate_votes list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

 # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to the terminal (all in the dict)
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    # # Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

