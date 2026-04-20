import myModule1   # I moduli sono dei file e per importarli uso l'import
import myModule2 # Se il modulo è già importato all'interno di un altro modulo, non verrà eseguito 2 volte


nome = "Napoli"
myModule1.saluto(nome)  # Uso della funzione creata in precedenza all'interno del modulo

# Questa parte di codice viene quasi sempre messo all'interno di moduli, spesso utilizzato come codice di test perchè i metodi non dovrebbero eseguirsi da soli
if (__name__  == "__main__"):
    print("\nSono stato richiamato dall'interno")
else:
    print("\nSono stato richiamato dall'esterno")


'''
In python non esistono variabili privati e non esistono costanti
__privato = 5   # Convenzione per creare una variabile privata
COSTANTE = 5      # Convenzione per creare una costante
'''
