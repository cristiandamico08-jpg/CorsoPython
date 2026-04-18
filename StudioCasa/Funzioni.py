# <!> RICORDA <!>
# Il nome di una funziona deve iniziare o con una lettera o con un trattino basso "_"
# Il nome di una funzione può contenere solo lettere e trattini bassi "_"
# I nomi delle funzioni sono case-sensitive ("laMiaFunzione" e "LaMiaFunzione" sono 2 funzioni diverse)

def laMiaFunzione():   # Per creare una funzione si usa il "def"
    print("Questa e' una funzione!")

laMiaFunzione()


# Se ti dovesse serivere creare una funzione "vuota" puoi inserire il pass
def funzioneVuota():
    pass


# Puoi inserire dei parametri di default in caso non venga inserito nulla
def saluto(nome = "amico"):
    print("Ciao ", nome, "!", sep = "")

saluto()          # In questo caso, visto che non ho inserito nessun parametro, stamperà la frase "Ciao amico!"
saluto("Luca")    # Mentre in questo caso sta,perà "Ciao Luca!"


# Se specifichi il nome della variabile, puoi inserirle in modo casuale
def presentazione(nome, anni):
    print("Ciao sono ", nome, " ed ho ", anni, " anni", sep = "")

presentazione("Luca", 27)                      # Funzione "normale"
presentazione(anni = 17, nome = "Adriano")     # Funzione con dati in ordine casuale


# Puoi passare qualsiasi tipo di dato all'interno di una funzione

# Liste
def funzioneLista(lista):
    for elemento in lista:
        print(elemento, end = " ")

lista = [1, 2, 3, 4, 5]
funzioneLista(lista)

# Dizionari
def funzioneDizionario(dizionario):
    print("\nNome:", dizionario["nome"], "\nEta':", dizionario["eta"])

dizionario = {
    "nome" : "Luca",
    "eta" : 27
}

funzioneDizionario(dizionario)


# Se non sai quanti paramentri saranno passati nella funzione, aggiungi un "*" prima del nome del parametro
def somma(*numeri):
    somma = 0
    for numero in numeri:
        somma += numero
    
    return somma

print("La somma totale e':", somma(1, 2, 3, 4, 5))


# Puoi combinari parametri normali con paramatri con l'asterisco
def saluti(saluto, *nome):
    for nome in nome:
        print(saluto, nome)

saluti("Ciao", "Luca", "Antonio", "Pasquale")


# Le lambda sono funzioni "nascoste"
def moltiplicatore(x):
    return lambda a : a * x       # lambda   argomento : espressione

duplicatore = moltiplicatore(2)
print(duplicatore(5))


# Le funzioni posso richiamarsi all'interno di esse
def countdown(n):
    if n <= 0:
        print("Finito!")
    else:
        print(n, end = " ")
        countdown(n - 1)

countdown(10)