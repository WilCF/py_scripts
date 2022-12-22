#Split a CSV by a user defined chunk of rows and give the CSVs a user-defined name and keep the headers
#Written mostly by ChatGPT, Ayelita Ray & Wil Stevens

# Libraries
import csv
import os

# Define the current folder, this is also where the CSV chunks shall be saved.
dest_folder = os.path.dirname(os.path.realpath(__file__))

# Prompt the user for the input and output filenames
input_filename = input("Your CSV, Please: ")
output_filename = input("Enter the base name for the output CSV files: ")

# Prompt the user for the number of lines to split by
split_by = int(input("How many lines would you like it to split by? "))

# Open the input CSV file
with open(input_filename, 'r') as source:
        reader = csv.reader(source)
# Get the headers from the input file
        headers = next(reader)

# Define the file counter
        file_idx = 0
        records_exist = True

# Do the Splitting Work & Write to CSVs
        while records_exist:

            i = 0
            target_filename = f'{output_filename}_{file_idx}.csv'
            target_filepath = os.path.join(dest_folder, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < split_by:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except StopIteration:
                        records_exist = False
                        break

            if i == 0:
# we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_idx += 1

        else:
            print("Finished splitting the csv file into chunks! You're a great person and I am so proud of you!")
