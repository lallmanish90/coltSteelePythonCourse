"""
***writing CSV files
writer - creates a writer object for writing to csv
writerow - method on a writer to write a row in the CSV
"""
from csv import writer,reader 
with open("Reading_CSV_files/figher.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]

with open("Reading_CSV_files/screaming_fighters.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)