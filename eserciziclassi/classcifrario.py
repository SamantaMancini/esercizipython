class Cifrario:

    chiave_predefinita = "qwertyuiopasdfghjklzxcvbnm"

    def __init__(self, chiave=None):

        if chiave is not None:
            self._chiave = chiave
        else:
            self._chiave = Cifrario.chiave_predefinita
        self.__alfabeto = "abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def imposta_chiave_predefinita(cls, nuova_chiave):
        cls.chiave_predefinita = nuova_chiave

    @staticmethod
    def __applica_sostituzione(carattere, chiave):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        if carattere in alfabeto:
            indice = alfabeto.index(carattere)
            carattere_cifrato = chiave[indice]
            return carattere_cifrato
        else:
            return carattere

    def crittografa(self, messaggio):
        messaggio_cifrato = ""
        for carattere in messaggio:
            carattere_cifrato = self.__applica_sostituzione(carattere.lower(), self._chiave)
            messaggio_cifrato += carattere_cifrato
        return messaggio_cifrato

    def decrittografa(self, messaggio_cifrato):
        messaggio_originale = ""
        for carattere in messaggio_cifrato:
            carattere_originale = self.__applica_sostituzione(carattere.lower(), self._chiave)
            messaggio_originale += carattere_originale
        return messaggio_originale


def main():
    # Creazione di un'istanza del cifrario con una chiave specifica
    cifrario = Cifrario("qwertyuiopasdfghjklzxcvbnm")

    # Crittografa un messaggio
    messaggio = "ciao, come stai?"
    messaggio_cifrato = cifrario.crittografa(messaggio)
    print("Messaggio cifrato:", messaggio_cifrato)  # Stampa: "ompm, yodk fyop?"

    # Decrittografa il messaggio cifrato
    messaggio_decifrato = cifrario.decrittografa(messaggio_cifrato)
    print("Messaggio decifrato:", messaggio_decifrato)  # Stampa: "ciao, come stai?"

    # Imposta una nuova chiave predefinita per tutti gli oggetti Cifrario
    Cifrario.imposta_chiave_predefinita("zyxwvutsrqponmlkjihgfedcba")

    # Crea un nuovo oggetto Cifrario senza specificare la chiave
    nuovo_cifrario = Cifrario()

    # Crittografa un messaggio utilizzando la nuova chiave predefinita
    messaggio_cifrato_nuovo_cifrario = nuovo_cifrario.crittografa(messaggio)
    print("Messaggio cifrato (nuovo cifrario):", messaggio_cifrato_nuovo_cifrario)


if __name__ == "__main__":
    main()