# Per creare una classe si usa il comando class
class ClasseVuota:
    def __init__(self):     # Così vado a creare il costruttore della classe
        print("Hello class!")

oggetto = ClasseVuota()  # Così vado ad instanziare un oggetto con la classe


pilaArray = []

# Inserimento/Lettura/Cancellazione
pilaArray.append(4)
print(pilaArray[-1])
del pilaArray[-1]


# Creazione classe pila
class ClassePila:
    def __init__(self):
        self.pilaLista = []

    def push(self, val):
        self.pilaLista.append(val)
    
    def pop(self):
        val = self.pilaLista[-1]
        del self.pilaLista[-1]
        return val
    
    def getLunghezza(self):
        return len(self.pilaLista)

pila = ClassePila()


# Per creare una sottoclasse metto la classe madre tra parentesi
class PilaAvanzata(ClassePila):
    def __init__(self):
        ClassePila.__init__(self)      # Come se fosse il super() di java

    def getSomma(self):
        somma = 0
        for elemento in self.pilaLista:
            somma += elemento
        return somma
    
pilaAvanzata = PilaAvanzata()
pilaAvanzata.push(6)
pilaAvanzata.push(7)
print("Somma:", pilaAvanzata.getSomma())

