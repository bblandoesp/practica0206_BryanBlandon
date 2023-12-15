numero = int (input ("Numero entre el 1-10:"))
def tabla_multiplicar(numero):
    """Función para realizar una tabla de multiplicar.

    Parámetros:
    - Numero: Un numero entero.

    Salida:
    tabla de multiplicar del numero solicitado.
    """
    if numero <= 10 and numero > 0:
        with open("tabla del " + str(numero) + ".txt", 'w') as tabla:
            for i in range(1,11):
                tabla.write(str(numero) + "x" + str(i) + "=" + str(numero * i) + "\n")

    else:
        print("Tiene que ser un numero entre 1 y 10")

tabla_multiplicar(numero)