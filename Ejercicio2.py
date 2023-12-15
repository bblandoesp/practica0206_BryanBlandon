import os 
numero = int(input("Un numero entre 1 y 10:"))
def leer_fichero(numero):
    """ Funcion para leer un fichero.
    Parámetros:
        -Numero = numero entre el 1 y 10 
    Salida:
        Muestra el todo el fichero del numero que le pidimos y si no existe avisa de ello """
    if os.path.isfile("tabla del " + str(numero) + ".txt"):
        with open("tabla del " + str(numero) + ".txt", "r") as tabla:
            leer = tabla.read()
            print(leer)
    else:
        print("¡El fichero tabla del " + str(numero) + " no existe!")

leer_fichero(numero)