def calcola_media(lista_numeri):
    somma = sum(lista_numeri)
    media = somma / len(lista_numeri)
    return media

def trova_parole_comuni(testo1, testo2):
    parole1 = set(testo1.split())
    parole2 = set(testo2.split())
    parole_comuni = parole1.intersection(parole2)
    return parole_comuni

lista_numeri = [10, 20, 30, 40, 50]
media = calcola_media(lista_numeri)
print(f"La media dei numeri nella lista {lista_numeri} è: {media}")
testo1 = "Questo è un esempio di testo."
testo2 = "Questo è un altro esempio di testo."
parole_comuni = trova_parole_comuni(testo1, testo2)
print(f"Le parole comuni tra i due testi sono: {parole_comuni}")