"""
DictWriter - creates a writer object for writing using dictionaries
fieldnames - kwarg for the dictwriter specifying headers
writeheader - method on a writer to write header row
writerow-method on a writer to write a row based on a dictionary
"""
from csv import DictWriter
with open("Reading_CSV_files/cats.csv", "w") as file:
    headers = ["name","breed", "age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "name": "garfield",
        "breed": "orange tabby",
        "age": 10
    })