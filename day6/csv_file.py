import csv

# open the CSV file for reading
with open("data.csv", "r") as file:
    reader = csv.reader(file)

    #next(reader)
    # read and print each row in the CSV file

    for row in reader:
        print(row)