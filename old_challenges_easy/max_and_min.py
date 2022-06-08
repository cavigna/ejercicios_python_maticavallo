# Escribir una función que devuelva un int en función a:
# Encontrar el valor máximo de un listado de numeros. NO USAR max()
# Encontrar el valor mínimo de un listado de numeros. NO USAR min()


def mas_grande(listado:list)-> int:
    elemento_mayor = listado[0]
    for elemento_actual in listado:
       if elemento_actual > elemento_mayor:
            elemento_mayor = elemento_actual
         
            print(elemento_mayor)
    return elemento_mayor 
    
    


def mas_chico(listado:list)-> int:
    pass


maximo_minimo_lista = [7, 93, 2, 8, 425, 1099901, 9, 1101000193, 393934, 3]

print(mas_grande(maximo_minimo_lista)) # Expected ==> Máximo: 1101000193
print(mas_chico(maximo_minimo_lista)) # Expected ==> Mínimo: 2


