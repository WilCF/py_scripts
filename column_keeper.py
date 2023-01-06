# Prompts a user for a csv and outputs a csv with only the columns whose headers are: content_urn, content_crowdli_url, media_urn, is_gold_topic, gold_definition_version, sample_date_range, content_date. 
# Written by ChatGPT & Wil Stevens

# Libraries
import csv
import subprocess

# Set the columns to keep
columns_to_keep = ['content_urn', 'content_crowdli_url', 'media_urn', 'is_gold_topic', 'gold_definition_version', 'sample_date_range', 'content_date']

# Show a message to the user
print("Hey there friend! Let's crunch some headers!")

# Prompt the user for the input file name
input_file_name = input("Enter the name of the input CSV file: ")

# Prompt the user for the output file name
output_file_name = input("Enter the name of the output CSV file: ")

# Add the .csv extension to the input and output file names if they're not already there
if not input_file_name.endswith('.csv'):
  input_file_name += '.csv'
if not output_file_name.endswith('.csv'):
  output_file_name += '.csv'

# Open the input and output files
with open(input_file_name, 'r', newline='') as input_file, open(output_file_name, 'w', newline='') as output_file:
  # Create CSV readers and writers
  reader = csv.DictReader(input_file)
  writer = csv.DictWriter(output_file, fieldnames=columns_to_keep)
  
  # Write the header row to the output file
  writer.writeheader()
  
  # Iterate through the rows in the input file
  for row in reader:
    # Create a new row dictionary with only the columns we want to keep
    new_row = {key: value for key, value in row.items() if key in columns_to_keep}
    
    # Write the new row to the output file
    writer.writerow(new_row)

# Print the output file name
print("Output file:", output_file_name)

# Ask the user if they want to open the file
open_file = input("Do you want to open the file? [y/n] ")

# Open the file if the user says yes
if open_file.lower() == 'y':
  subprocess.call(['open', output_file_name])

# Show a message
print("You are amazing! Have a great day!")
