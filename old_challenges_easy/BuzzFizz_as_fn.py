# Crear una función que reciba un rango de numeros e imprima lo siguiente:
# Si el número es divisible por 3: imprimir Fizz
# Si el número es divisible por 5: imprir Buzz
# Si el número es divisible por 3 y por 5: imprimr FizzBuzz
def fizz_buzz(inicio:int, fin:int)->None:
    range_num = range(inicio,fin)
    for n in range_num:
        if (n % 3 == 0) and (n % 5 == 0):
            print(f'{n} FizzBuzz')     
        elif n % 5 == 0:
            print(f'{n} Buzz')
        elif n % 3 == 0:
            print(f'{n} Fizz')

fizz_buzz(-3265659656598,54545454545453)