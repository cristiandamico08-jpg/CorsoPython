# Le liste possono contenere diversi tipi di dato all'interno di esse

listaDiProva = [1, 2.1, "Stringa", True]

print(len(listaDiProva))   # len() si usa per la dimensione della lista

print(type(listaDiProva))  # type() serve per far vedere di che tipo è una variabile (in questo caso sarà <class 'list'>)

print(listaDiProva[2])     # le liste funzionano come gli array statici in C, per indicare un singolo elemento si usa l'indice tra le []
print(listaDiProva[-1])    # gli indici negativi indicano gli elementi partendo dall'ultimo fino ad andare all'indietro
print(listaDiProva[1:3])   # si può indicare un range di indici da mostrare (ultimo non incluso) [uguale con gli indici negativi]
print(listaDiProva[:2])    # così si indica dal primo fino all'elemento indicato (non incluso)   [uguale con gli indici negativi]
print(listaDiProva[2:])    # così si indica dall'elemento indicato (compreso) fino alla fine     [uguale con gli indici negativi]


# per controllare se un elemento è presente in una lista si usa un if
if "Stringa" in listaDiProva:
    print("E' presente 'Stringa' nella lista")
else:
    print("Non c'e' 'Stringa' nella lista")


# gli elementi all'interno delle liste si possono cambiare in qualsiasi momento
listaCambiabile = ["mela", "arancia", "bastone di ferro", "banana"]
listaCambiabile[2] = "pera"
print(listaCambiabile[2])


# gli elementi si possono cambiare pure con il range
listaCambiabile2 = ["mela", "assi di legno", "bastone di ferro", "banana"]
listaCambiabile2[1:3] = ["arancia", "pera"]
print(listaCambiabile2[1:3])


# puoi cambiare un singolo elemento con 2 o più elementi (usare SEMPRE il range e le parentesi [])
listaCambiabile3 = ["mela", "arancia", "bastone di ferro", "banana"]
print("\nLista prima del cambiamento:", listaCambiabile3)
listaCambiabile3[2:3] = ["pera", "mango", "albicocca"]
print("Lista dopo il cambiamento:", listaCambiabile3,"\n")


# puoi cambiare più elementi con un singolo elemento (usare SEMPRE il range e le parentesi [])
listaCambiabile4 = ["mela", "assi di legno", "bastone di ferro", "banana"]
print("\nLista prima del cambiamento:", listaCambiabile4)
listaCambiabile4[1:3] = ["pera"]
print("Lista dopo il cambiamento:", listaCambiabile4,"\n")


# puoi inserire nuovi elementi alla lista in qualsiasi posizione
listaCambiabile5 = ["mela", "arancia", "pera", "banana"]
print("\nLista[5] prima del cambiamento:", listaCambiabile5)
listaCambiabile5.insert(2, "mango")  # <!> RICORDA <!> insert(indice, elemento) va sempre inserito l'indice
print("Lista[5] dopo il cambiamento:", listaCambiabile5,"\n")


# per inserire un elemento direttamente alla fine della lista si può usare il comando append()
listaCambiabile6 = ["mela", "arancia", "pera", "banana"]
print("\nLista[6] prima del cambiamento:", listaCambiabile6)
listaCambiabile6.append("mango")
print("Lista[6] dopo il cambiamento:", listaCambiabile6,"\n")


# per inserire una lista alla fine di un'altra lista si usa il comando extend()
listaBase = ["mela", "arancia"]
listaDaAggiungere = ["pera", "banana"]
print("\nLista base:", listaBase)
print("Lista da aggiungere:", listaDaAggiungere)
listaBase.extend(listaDaAggiungere)
print("Lista finale:", listaBase,"\n")


# puoi estendere qualsiasi variabile
listaBase1 = ["mela", "arancia"]
tuple = ("mango", "albicocca")
print("\nLista base:", listaBase1)
print("Tuple da aggiungere:", tuple)
listaBase1.extend(tuple)
print("Lista finale:", listaBase1,"\n")


# puoi rimuovere oggetti inserendo il 'nome' dell'oggetto
listaRimozione = [1, 2, 3, 4]
print("\nLista rimozione intera:", listaRimozione)
listaRimozione.remove(2)
listaRimozione.remove(3)
listaRimozione.remove(4)
print("Lista rimozione:", listaRimozione, "\n")


# puoi rimuovere oggetti usando anche l'indice dell'oggetto
listaRimozione1 = [1, 2, 3, 4, 5]
print("\nLista rimozione intera:", listaRimozione1)
listaRimozione1.pop(2)
listaRimozione1.pop(3)
print("Lista rimozione (con pop):", listaRimozione1, "\n")
# oppure
listaRimozione1 = [1, 2, 3, 4, 5]
print("\nLista rimozione intera:", listaRimozione1)
del listaRimozione1[2]
del listaRimozione1[3]
print("Lista rimozione (con del):", listaRimozione1, "\n")


# puoi rimuovere tutti gli elementi di una lista con il comando clear()
listaVuota = [1, 2, 3, 4, 5]
print("\nLista vuota prima:", listaVuota)
listaVuota.clear()
print("Lista vuota dopo:", listaVuota, "\n")


# puoi riordinare una lista con il comando sort()

# ORDINE ALFABETICO (case-sensitive, metterà sempre le parole con le maiuscole prima di quelle con le minuscole)
listaAlfabetica = ["c", "e", "a", "d", "b"]
print("\nLista alfabetica non ordinata:", listaAlfabetica)
listaAlfabetica.sort()
print("Lista alfabetica ordinata:", listaAlfabetica, "\n")
# ORDINE ALFABETICO AL CONTRARIO (case-sensitive, metterà sempre le parole con le maiuscole prima di quelle con le minuscole)
listaAlfabetica = ["c", "e", "a", "d", "b"]
print("\nLista alfabetica non ordinata:", listaAlfabetica)
listaAlfabetica.sort(reverse = True)
print("Lista alfabetica ordinata:", listaAlfabetica, "\n")

# ORDINE NUMERICO 
listaNumerica = [3, 0, 1, 4, 5, 2]
print("\nLista numerica non ordinata:", listaNumerica)
listaNumerica.sort()
print("Lista numerica ordinata:", listaNumerica, "\n")
# ORDINE NUMERICO AL CONTRARIO
listaNumerica = [3, 0, 1, 4, 5, 2]
print("\nLista numerica non ordinata:", listaNumerica)
listaNumerica.sort(reverse = True)
print("Lista numerica ordinata:", listaNumerica, "\n")


# puoi riordinare una lista anche con delle funzioni usando il comando 'key = funzione'

# Numeri più vicini al 50
def vicino50(n):
    return abs(n - 50)    # abs() serve per trovare il valore assoluto (es. il valore assoluto di -25 è 25)

lista50 = [100, 50, 65, 82, 23]
print("\nLista numerica non ordinata:", lista50)
lista50.sort(key = vicino50)
print("Lista numerica ordinata:", lista50, "\n")

# ORDINE ALFABETICO (case-insensitive, non importa se la parola inizia con la lettara maiuscola o minuscola)
listaAlfabetica = ["C", "e", "a", "D", "b"]
print("\nLista alfabetica non ordinata:", listaAlfabetica)
listaAlfabetica.sort(key = str.lower)
print("Lista alfabetica ordinata:", listaAlfabetica, "\n")
# ORDINE ALFABETICO AL CONTRARIO (case-insensitive, non importa se la parola inizia con la lettara maiuscola o minuscola)
listaAlfabetica = ["C", "e", "a", "D", "b"]
print("\nLista alfabetica non ordinata:", listaAlfabetica)
listaAlfabetica.sort(key = str.lower, reverse = True)
print("Lista alfabetica ordinata:", listaAlfabetica, "\n")


# puoi invertire l'ordine di una lista
listaInvertita = ["ciao", "come", "stai"]
print("Lista normale:", listaInvertita)
listaInvertita.reverse()
print("Lista invertita:", listaInvertita, "\n")


# puoi copiare una lista in 3 modi
listaDaCopiare = [1, 2, 3, 4]

# 1 - metodo copy()
lista1 = listaDaCopiare.copy()

# 2 - metodo list()
lista2 = list(listaDaCopiare)

# 3 - metodo slice [:]
lista3 = listaDaCopiare[:]


# puoi unire più liste in 3 modi
lista1 = ["ciao"]
lista2 = ["come"]
lista3 = ["stai"]
lista4 = ["tutto", "bene"]
lista5 = ["sono", "a", "casa"]

# 1 - metodo '+'
listaVuota = lista1 + lista2 + lista3
print("Lista unita [+]:", listaVuota)

# 2 - metodo append()
listaVuota.clear()
for elemento in lista4:
    listaVuota.append(elemento)

for elemento in lista5:
    listaVuota.append(elemento)

print("Lista unita [append()]:", listaVuota)

# 3 - metodo extend()
lista4.extend(lista5)
print("listaunita [extend()]:", lista4)
