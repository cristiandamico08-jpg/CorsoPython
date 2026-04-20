import myModule2    # Posso importare altri moduli creati da me all'interno di un modulo creato da me

def saluto(nome):  # Funzione che potrò richiamare una volta importato il modulo
    print("\nCiao ", nome, "!", sep = "")

__contatore = 0

def somma(listaNumeri):
    global __contatore
    __contatore += 1
    somma = listaNumeri[0]
    for elemento in listaNumeri:
        somma += elemento
    return somma