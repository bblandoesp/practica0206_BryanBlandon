import os
n = int(input("Numero entre 1 y 10:"))
m = int(input("Numero entre 1 y 10:"))
def Linea_M(n ,m):
    """ Función para mostrar una linea del fichero.
    Parámetros:
        -n: Numero identificador para el fichero.
        -m: Linea del fichero que queremos.
    Salida:
        Muestra la Linea del fichero-
    """
    if os.path.isfile("tabla del " + str(n) + ".txt"):
        with open("tabla del " + str(n) + ".txt", "r") as tabla:
                f = tabla.readlines()
                s = f[m-1]
                print(s)

Linea_M(n, m)