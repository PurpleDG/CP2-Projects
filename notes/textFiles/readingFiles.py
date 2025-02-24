#Evan mcCabe Reading Files Notes

import csv

with open("notes/test.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes/userInfo.csv") as file:
    reader = csv.reader(file)
    next(reader) # (skip the first line)
    for row in reader:
        print(row)