import csv

with open("dati.csv", "r") as file:
    reader = csv.reader(file)

    for riga in reader:
        print(riga)