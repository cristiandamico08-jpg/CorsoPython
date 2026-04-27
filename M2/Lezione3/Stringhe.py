
# Per vedere se una frase o un carattere è presente in una stringa usa il conado in (restituisce true/false)
alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alfabeto)

# Le stringhe sono immutabili, per modificarle riassegno la variabile
print("\nPrima della modifica:", alfabeto)
alfabeto = alfabeto[5:]
print("Dopo la modifica:", alfabeto)


# Per modificare una singola lettera si riassegna la variabile
stringaFunzione = "abcdef"
print("\nPrima della modifica:", stringaFunzione)
indiceLetteraDaSostituire = stringaFunzione.index("d")
stringaFunzione = stringaFunzione[: indiceLetteraDaSostituire] + "D" + stringaFunzione[indiceLetteraDaSostituire+1 :]
print("Dopo la modifica:", stringaFunzione)


# Puoi contare quante volte si ripete un carattere o un insieme di caratteri puoi usare il comando count()
stringaConteggio = "abcaabc"
print("\nStringa:", stringaConteggio, "  Conteggio [bc]:", stringaConteggio.count("bc"))


# Puoi centrare una stringa con il comando center()
stringaInMezzo = "Stringa Centrata"
stringaInMezzo = "[" + stringaInMezzo.center(30) + "]"
print("\n", stringaInMezzo, sep = "")