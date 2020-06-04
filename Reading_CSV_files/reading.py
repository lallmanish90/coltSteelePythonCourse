"""
**Reading CSV files
-csv files are common file format for tabular data
-we can read CSV files just like other text files
-python has built-in CSV module to read/write CSVs more easily

**CSV module
-two ways to read CSV
reader- lets you interate over rows of the CSV as lists
DictReader- lets you iterate over rows of the CSV as OrderedDicts
"""

#reader
# from csv import reader 
# with open("Reading_CSV_files/figher.csv") as file:
#     csv_reader = reader(file)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")

from csv import DictReader 
with open("Reading_CSV_files/figher.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row["Name"])
        print(row["Country"])