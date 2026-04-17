import math

'''
print(math.pi) 
print(math.sin(math.pi/2))
'''

# print(dir(math))  stampo la directory con tutte le sue entities

'''
miaLista = [1, 2, 3, "pippo"]

for elemento in dir(math):    # (foreach)
    print(elemento)
'''

'''
for elemento in range(0, 11, 2):  # (inizio(incluso), fine(escluso), ogni quanto(i++))
    print(elemento)
'''

'''
print("PiGreco base:", math.pi)
pi = 5   # 'pi' e 'math.pi' vengono trattate come 2 variabili diverse
print("Variabile pi:", pi)
print("PiGreco:", math.pi)
math.pi = 7     # è possibile modificare il pigreco perchè non esistono le costanti in py, tutto è sovrascrivibile
print("Variabile pi:", pi)
print("PiGreco modificato:", math.pi)
'''

'''
COSTANTE = 5   # convenzioni per dichiarare le "costanti"
_costante = 5
'''

'''
def saluto(x):    # come creare una funzione
    print("\n\nCiao", x, sep="--")  # sep="--" sostituisce gli spazi tra le stringhe con 2 -

saluto("Luca Ravasi")
'''