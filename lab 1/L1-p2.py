
import csv
from pprint import pprint

with open("temps.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    # make rows into list
    data = list(reader)

    print(f"Contents:")
    for row in data:
        print(f"{row}")

    print(f"Headers: \n{header}")

    print(f"Number of columns: \n{len(header)}")

    print(f"Column names:")
    for index, col in enumerate(header):
        print(f"{index}: {col}")
    
    print(f"Number of data rows: \n{len(data)}")
    if data:
        sample = data[0]
        print("Types for each column:")
        for colname, value in zip(header, sample):
            print(f"{colname} : {type(value)}")
