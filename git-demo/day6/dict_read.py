import csv

with open("data.csv", "r") as file:
    import csv

with open("data.csv", "r") as file:import csv

with open("data.csv", "r") as file:
    for row in reader:
        print(row["Name"], row["Age"], row["Department"])

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)              