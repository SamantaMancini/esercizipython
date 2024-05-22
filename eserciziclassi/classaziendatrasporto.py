class Veicolo:
    def __init__(self, targa, marca, modello, anno, tipo):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.tipo = tipo
    
    def informazioni(self):
        return f"{self.marca} {self.modello} ({self.anno}), Tipo: {self.tipo}"

class Flotta:
    def __init__(self):
        self.veicoli = []
    
    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)
    
    def rimuovi_veicolo(self, targa):
        for veicolo in self.veicoli:
            if veicolo.targa == targa:
                self.veicoli.remove(veicolo)
                break

    def elenco_veicoli(self):
        for veicolo in self.veicoli:
            print(veicolo.informazioni())

flotta = Flotta()

autobus1 = Veicolo("AB123CD", "Mercedes", "Tourismo", 2015, "Autobus")
camion1 = Veicolo("XY789ZA", "Scania", "R500", 2018, "Camion")
auto1 = Veicolo("EF456GH", "Toyota", "Corolla", 2020, "Auto")

flotta.aggiungi_veicolo(autobus1)
flotta.aggiungi_veicolo(camion1)
flotta.aggiungi_veicolo(auto1)

print("Elenco veicoli: ")
flotta.elenco_veicoli()

flotta.rimuovi_veicolo("XY789ZA")

print("Nuovo elenco veicoli: ")
flotta.elenco_veicoli()