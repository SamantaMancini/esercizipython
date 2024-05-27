import csv

dati = [
    [" Nome", "Cognome", "Età"],
    ["Mario", "Rossi", 25],
    ["Laura", "Verdi", 30]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(dati)