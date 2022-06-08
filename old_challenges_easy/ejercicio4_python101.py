# *********** Ejecicio 4 **************
#Encontrar los calores repetidos en una lista y mostrarlos en una nueva lista

import re
from tkinter import N


repetidos = [12, 23, 4, 6, 22,99,37, 52, 12, 65, 99, 33, 37]

unicos = []

# Excpected ==> [12, 99, 37]

repo = []
for position in repetidos:
    if position not in repo:
        repo.append(position) 
    else:
        unicos.append(position)
print(unicos)
