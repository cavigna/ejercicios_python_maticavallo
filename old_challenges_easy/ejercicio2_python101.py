# *********** Ejecicio 2 **************
# Encontrar el valor máximo de un listado de numeros. NO USAR max()
# Encontrar el valor mínimo de un listado de numeros. NO USAR min()

maximo_minimo = [7, 93, 2, 8, 425, 1099901, 9, 1101000193, 393934, 3]

max_num = 0

for n in maximo_minimo:
    if max_num < n:
        max_num = n
print(f'the maximun number is {max_num}')  

min_num = max_num

for n in maximo_minimo:
    if min_num > n:
        min_num = n
print(f'the minimum number is {min_num}')     



# Expected ==> Máximo: 1101000193
# Expected ==> Mínimo: 2