# *********** Ejecicio 5 **************
#Dada una lista, imprimir la suma de los números pares e imapres.
#Consejo: Ver en el repo, el uso de break

listado_pares_e_impares= [22, 32, 42, 13, 35, 13, 6, 42, 13, 25, 28, 15, 14, 
30, 42, 32, 46, 0, 47, 46]

#Expected:
# Expected ==> Pares 382, 161
# Expected ==> Impares 161

even_list = []
odd_list = []

for number in listado_pares_e_impares:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
print(f'Pares {sum(even_list)}')
print(f'Impares {sum(odd_list)}')




