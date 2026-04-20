import os

# Per creare una eccezione si usa il try ... except
try:
    print(x)   # In questo caso x non è dichiarata e quindi verrà eseguita l'eccezione
except:
    print("\n<!> Non hai dichiarato la variabile! <!>")


# Puoi creare diversi tipi di eccezioni usando a nomi di eccezioni (tutte le built-in exception qui: https://www.w3schools.com/python/python_ref_exceptions.asp)
try:
    print(x)
except NameError:
    print("\n<!> La variabile 'x' non e' dichiarata <!>")
except:
    print("\n<!> Errore <!>")


# Puoi usare il comando else per definire se non ci sono stati problemi
try:
    print("\nCiao!")
except:
    print("<!> Qualcosa e' andato storto <!>")
else:
    print("<!> E' tutto apposto <!>")


# Il comando finally va ad eseguire il codice al suo interno indipendentemente se ci siano errori o meno
try:
    print(x)
except:
    print("\n<!> La variabile 'x' non e' stata dichiarata <!>")
else:
    print("\n<!> E' tutto apposto <!>")
finally:
    print("Questa parte di codice viene sempre eseguita")


# Puoi usare anche il comando raise per mandare un'eccezione e far terminare il programma
x = "ciao"
print("\nInserisci un numero intero:", x)
if not type(x) is int:
    raise Exception("<!> Sono ammessi solo numeri interi <!>")
else:
    print("<!> Non ci sono problemi <!>")
    os._exit(0)