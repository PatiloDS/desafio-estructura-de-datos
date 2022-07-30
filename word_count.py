#Patricio Carrasco
import sys

with open ("lorem_ipsum.txt","r") as file:
    texto = file.read()
#cargamos el documento txt que contiene el texto por defecto lorem ipsum

numero_caracteres = len(set(texto)) #usamos len para contar los caracteres 
numero_palabras = len(set(texto.split(" ")))
print("el numero de caracteres distintos es: {}".format(str(numero_caracteres)))
print("el numero de palabras distintas es: {}".format(str(numero_palabras)))