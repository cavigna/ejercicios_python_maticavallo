#Escribir una función que borre un numero n de un listado y devuelva el 
# MISMO listado. NO CREAR UNO NUEVO 

def borrar_n(listado_de_la_funcion:list, numero_a_borrar:int)->list:
    """
    Borrar un numero n de un listado de int
    """
    for numero_actual in listado_de_la_funcion:
        if numero_actual == numero_a_borrar:
            listado_de_la_funcion.remove(numero_a_borrar)
    return listado_de_la_funcion



listado_n = [23, 31,6, 31, 95, 4, 31, 2, 33, 3, 31] 

# Borrar el 31

borrar_n(listado_n, 123)


#listado_n.remove(123)


print(listado_n)

