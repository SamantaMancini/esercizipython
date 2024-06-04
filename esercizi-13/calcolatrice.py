class Calcolatrice:
    def calcola(self, operazione, a, b):
        return operazione(a, b)
    
def main():
    calcolatrice = Calcolatrice()

    somma = lambda x, y: x + y
    risultato_somma = calcolatrice.calcola(somma, 5, 3)
    print("Risultato della somma:", risultato_somma)

    prodotto = lambda x, y: x * y
    risultato_prodotto = calcolatrice.calcola(prodotto, 4, 2)
    print("Risultato del prodotto:", risultato_prodotto)

if __name__ == "__main__":
    main()