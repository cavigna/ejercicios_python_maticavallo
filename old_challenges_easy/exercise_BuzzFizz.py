rango_numeros = range(1,101)
for n in rango_numeros:
    if (n % 3 == 0) and (n % 5 == 0):
        print(f'{n} FizzBuzz')     
    elif n % 5 == 0:
        print(f'{n} Buzz')
    elif n % 3 == 0:
        print(f'{n} Fizz')
    else:
        print(rango_numeros)