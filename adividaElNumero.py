from random import randint



numeroSecreto = randint(1 , 50)
intentos = 0
adivinar = None
intentosMaximo = 10

print('Adivina el numero entren el 1 y el 50')
while adivinar != numeroSecreto and intentos < intentosMaximo:
    adivinar = int(input('Cual numero es? '))
    #verificamos si el numero es igual o distinto
    if adivinar > numeroSecreto:
        print('el numero Secreto es menor')
    elif adivinar < numeroSecreto:
        print('el numero Secreto es Mayor')
    #incrementamos la variale de intentos
    intentos += 1

if intentos < intentosMaximo:
    print(f'felicidades ganaste en {intentos} intentos 😁')
else:
    print('LO SIENTO SUPERASTE EL IMITE DE INTENTOS 😒')