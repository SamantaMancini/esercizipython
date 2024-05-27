import datetime

data_corrente = datetime.date.today()

data_formattata = data_corrente.strftime("%d/%m/%Y")
print("Data formattata:", data_formattata)
ora_corrente = datetime.datetime.now().time()

ora_formattata = ora_corrente.strftime("%H:%M:%S")
print("Ora formattata:", ora_formattata)