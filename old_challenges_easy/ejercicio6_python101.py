# *********** Ejecicio 6 **************
# Encontrar si en un listado dos números hacen la sumatoria 42. Devolver todos los 
# Pares de números en una lista


listado_suma_42 = [3, 94, 20, 22, 33, 9, 33, 12, 5, 11, 31]

# Expected ==> [20, 22, 33, 9, 9, 33, 11, 31]

sum = 0
pair_number_sums42 = []

for number1 in listado_suma_42:
    for number2 in listado_suma_42:
        if number1 + number2  == 42:
            pair_number_sums42.append(number1)
      
print(pair_number_sums42)