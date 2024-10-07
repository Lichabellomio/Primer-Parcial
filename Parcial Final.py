def listaPrimos(n):
    def esPrimo(x):
        esPrimo = True
        for i in range(2,x-1):
            if x%i==0:
                esPrimo = False
                break
        return esPrimo

    lista = []
    b = 2
    while len(lista)!=n:
        if esPrimo(b):
            lista.append(b)
        b += 1
    return lista[n-1]
    

n = int(input("Ingrese un numero"))
print(f"El {n}° número primo es: {listaPrimos(n)}")
