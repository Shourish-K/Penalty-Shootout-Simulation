import csv

# Input and output file names
input_file = "D:\\USCB CSCI\\SEM 7\\Systems Modeling & Simulation\\Final Project\\Data\\male_players.csv"
output_file = "D:\\USCB CSCI\\SEM 7\\Systems Modeling & Simulation\\Final Project\\Data\\goalkeepers.csv"

with open(input_file, mode='r', newline='', encoding='utf-8-sig') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        # Create CSV reader and writer objects
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write the header to the output file
        writer.writeheader()
        
        # Iterate over each row and check if Position is GK
        for row in reader:
            if row.get("Position") == "GK":
                writer.writerow(row)
        
        print(f"Goalkeeper records have been written to '{output_file}'")