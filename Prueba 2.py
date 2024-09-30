
nombre = input("Hola, ¿Cuál es tu nombre? ")
print("Mucho gusto,", nombre)

edad = input("Ingresa tu edad ")
edad = (int (edad))
print("Tu edad es: ", edad, "años.")

numero = int(input ("pone un numero: "))

while numero < 0: 
    print("bien hecho")


def esPrimo(x):
    esPrimo = True
    for i in range (2,x-1):
        if x%i==0:
            esPrimo = False
            break
    return esPrimo

def listaPrimos(a):
    lista = []
    b = 2
    while len(lista)!=a:
        if esPrimo(b):
            lista.append(b)
            b += 1
    return lista

n = int(input("ingrese un numero"))
lista_respuesta = listaPrimos (n)
print(f"los primeros {n} números primos son: {lista_respuesta}")