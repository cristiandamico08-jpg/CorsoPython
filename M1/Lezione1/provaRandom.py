'''
from random import random, seed  #con il "seed" posso impostargli io la base su cui generare i numeri random, facendo si che ogni volta siano sempre gli stessi

seed(4)

for i in range(5):
    print(random()) # random di default genera numeri casuali tra 0(incluso) e 1(escluso)
'''

'''
import random

for i in range(100):
    # print(random.randrange(1,7))    # random tra 1(incluso) e 7(escluso)
    print(random.randint(1,7))      # random tra 1(incluso) e 7(incluso)
'''


import random

miaLista = [2, 6, 567, "pippo", "ciao"]
print(random.choice(miaLista)) # prende solo un elemento dalla lista

print(random.sample(miaLista, 3))  # prende n cose a caso dalla lista (n non può essere più grande del numero di elementi presenti nella lista)