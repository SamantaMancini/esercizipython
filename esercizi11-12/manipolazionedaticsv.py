import csv

nome_file = "dati.csv"

with open(nome_file, "r") as file_csv:
    lettore_csv = csv.reader(file_csv)
    header = next(lettore_csv)
    print("Header:", header)

    riga = next(lettore_csv)
    print("Prossima riga:", riga)