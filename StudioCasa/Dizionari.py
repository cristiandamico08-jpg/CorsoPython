# I dizionari li possiamo considerare come le Struct del linguaggio C
# <!> RICORDA <!> I dizionari non accetta duplicati


# I dizionari si dichiarano in due modi diversi

# Con le parentesi {}
dizionarioGraffe = {
    "nome" : "Luca",
    "cognome" : "Napolitano",
    "eta" : 27
}

print("\nDizionario graffe:", dizionarioGraffe)

# Con il comando dict()
dizionarioDict = dict(nome = "Simone", cognome = "Ciraudo", eta = 17)

print("Dizionario \"dict()\":", dizionarioDict)


# Per andare a selezionare un oggetto all'interno del dizionario, andiamo a prendere il nome della variabile
dizionario = {
    "nome" : "Adriano",
    "cognome" : "Ravasi",
    "eta" : 24
}

print("\nIl nome della persona e':", dizionario["nome"])


# Per determinare quanti oggetti sono presenti all'interno di un dizionario si usa il comando len()
print("Il dizionario ha", len(dizionario), "oggetti all'interno di esso")


# Puoi inserire anche le liste all'interno dei dizionario
mela = {
    "possibiliColori" : ["rosso", "verde", "giallo"],
    "livelloDiAcidita" : ["basso", "medio", "alto"]
}

print("\nI possibili colori della mela sono:", end = " ")
for i in range(len(mela["possibiliColori"])):
    print(mela["possibiliColori"][i], end = " ")


# Per accedere a degli oggetti presenti all'interno di un dizionario puoi usare il comando get()
print("\n\nIl nome della persona e':", dizionarioGraffe.get("nome"))


# Per sapere quali sono i nomi delle variabili all'interno di un dizionario puoi usare il comando keys()
print("\nVariabili all'interno di 'mela':", mela.keys())


# Puoi aggiungere nuove variabili ad un dizionario in questo modo
auto = {
    "marca" : "Fiat",
    "modello" : "Panda",
    "anno" : 2026
}

print("\nDizionario prima del cambiamento:", auto)

auto["colore"] = "Bianco Panna"    # Modo per aggiungere una variabile

print("Dizionario dopo il cambiamento:", auto)


# Se vuoi stampare SOLO tutti i valori all'interno di un dizionario puoi usare il comando values()
print("\nValori presenti all'interno del dizionario 'auto':", auto.values())


# Se vuoi verificare se una variabile è presente in un dizionario puoi usare un ciclo if
if "marca" in auto:
    print("\nLa marca e' presente all'interno del dizionario")


