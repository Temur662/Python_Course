import csv
data = [
    {"Name" : "Alice" , "Age": 24, "Major": "Computer Science"},
    {"Name": "Bob", "Age": 22, "Major": "Mathematics"},
    {"Name": "Charlie", "Age": 23, "Major": "Physics"}
]
with open("Students.csv", "w", newline="") as file:
    headers = ["Name", "Age", "Major"]
    csv_dict_writer = csv.DictWriter(file, fieldnames=headers)
    csv_dict_writer.writeheader()
    for row in data:
        csv_dict_writer.writerow(row)

with open("Students.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(dict(row))

newData = {
    "Name": "Temur", "Age" : 19, "Major": "Computer Science"
}

with open("Students.csv", "a") as file:
    csv_dict_writer = csv.DictWriter(file, fieldnames=newData)
    csv_dict_writer.writerow(newData)

with open("Students.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(dict(row))
