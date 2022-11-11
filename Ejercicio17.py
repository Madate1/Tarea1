
#Ejercicio 17: Crear un script que encuentre la potencia de un número ingresado por el teclado.

x = int(input("Ingrese un valor:"))

def potencia(base, exponente):

    resultado = 1

    for x in range(exponente):
        resultado *= base

    return resultado

print(x**3)
