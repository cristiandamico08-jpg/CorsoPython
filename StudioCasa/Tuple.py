# I tuple sono come gli array statici di Java

# I comandi sono uguali a quelli delle liste solo che, una volta creati, non possono essere modificati
# A differenza delle liste, i tuple si dichiarano con le parentesi tonde

# Per riconoscere se una variabile è tuple si può usare il comando type()
tuple1 = ("mela", "arancia", "banana")

print(type(tuple1))


# Se vuoi modificare degli elementi all'interno del ruple lo dovrai convertire in lista
tuple2 = (1, 2, 3, 4, 5)                            # Tuple base
print("\nTuple prima del cambiamento:", tuple2)
listaTuple = list(tuple2)                           # Conversione da TUPLE in LISTA
listaTuple[2] = "cambiamento"                       # Cambiamento del primo elemento
tuple2 = tuple(listaTuple)                          # Conversione da LISTA a TUPLE
print("Tuple dopo il cambiamento:", tuple2)


# La stessa cosa vale se si vogliono aggiungere o rimuovere oggetti

# AGGIUNTA
tuple3 = (1, 2, 3, 4)
print("\nTuple prima del cambiamento:", tuple3)
listaTuple = list(tuple3)
listaTuple.insert(3, "cambiamento")
tuple3 = tuple(listaTuple)
print("Tuple dopo il cambiamento:", tuple3)

# RIMOZIONE
tuple4 = (1, 2, 3, 4, "cambiamento")
print("\nTuple prima del cambiamento:", tuple4)
listaTuple = list(tuple4)
listaTuple.pop(-1)
tuple4 = tuple(listaTuple)
print("Tuple dopo il cambiamento:", tuple4)


# Quando si crea un tuple si dice che lo stiamo impacchettando, in python si può pure spaccattarlo assegnandolo a più variabili
pacchetto = ("arancia", "banana", "pera")
print("\nTuple:", pacchetto)
(arancione, giallo, verde) = pacchetto
print("Variabili assegnate:", arancione, giallo, verde)


