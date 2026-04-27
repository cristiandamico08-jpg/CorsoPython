import math


# Puoi creare delle eccezioni a cascata
try:
    x = float(input("\nInserisci un numero: "))
    y = math.sqrt(x)

    print("La radice quadrata di [", x, "] e' uguale a [", y, "]")
except ValueError:
    print("\n<!> Valore inserito non numerico o negativo <!>")
except:
    print("\n<!> C'e' stato un errore <!>")


# Ci sono diversi tipi di eccezioni
try:
    x = float(input("\nInserisci il primo numero: "))
    y = float(input("Inserisci il secondo numero: "))
    z = x / y

    print("Il risultato e':", z)
except ZeroDivisionError:
    print("\n<!> Non puoi dividere per 0 <!>")
except:
    print("\n<!> C'e' stato un errore <!>")


# Si usa il comando assert durante la fase di testing per verificare degli errori
x = float(input("\nInserisci un numero: "))
assert x >= 0.0   # Se il numero è più piccolo di 0 allora il programma si chiude

y = math.sqrt(x)

print("La radice quadrata di [", x, "] e' uguale a [", y, "]")