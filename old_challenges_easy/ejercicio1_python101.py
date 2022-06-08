# *********** Ejecicio 1 **************
# Borrar todos los números 31 de un listado


treinta_uno = [23, 31,6, 31, 95, 4, 31, 2, 33, 3, 31] 
# Expected : [23, 6, 95, 4, 2, 33, 3]

valor_a_remover = 31
for n in treinta_uno:
    if n == 31:
        treinta_uno.remove(n)

print(treinta_uno)
