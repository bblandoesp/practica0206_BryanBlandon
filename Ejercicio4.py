import urllib.request

Url = urllib.request.urlopen("http://textfiles.com/adventure/aencounter.txt")
r = Url.read() #Leemos el texto que hay en Url
p = r.split() #dividimos el texto que por defecto es en un espacio en blanco
print(len(p)) # Devolvemos el numero de caracteres y lo imprimimos