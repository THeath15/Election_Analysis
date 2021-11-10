# # Add our dependencies.
# import csv
# import os

# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
#     with open(file_to_load) as election_data:

# # To do: read and analyze the data here:
# The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote


# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

#------------------------Read data from file
# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#  # To do: perform analysis.
#      print(election_data)

# # Close the file.
# election_data.close()

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # # Create a filename variable to a direct or indirect path to the file.
# # file_to_save = os.path.join("analysis", "election_analysis.txt")
# # # Using the open() function with the "w" mode we will write data to the file.
# # open(file_to_save, "w")


# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#    # txt_file.write("Hello World!") 
#      # Write three counties to the file.
#      #txt_file.write("Arapahoe, ")
#     #  txt_file.write("Denver, ")
#     #  txt_file.write("Jefferson, ") 
     
#     # Write three counties to the file.
#        txt_file.write("\nCounties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # To do: read and analyze the data here.


# # Close th filPypo
#     outfile.closee()

 # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)