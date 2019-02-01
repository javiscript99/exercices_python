# -*- coding: utf-8 -*-
import random
"""
Editor de Spyder

Este es un archivo temporal.
"""

print("Un numero del 1 al 100")
numero = int(input())
respuesta = random.randint(1,101)  
    
while numero < respuesta or numero>respuesta or numero==respuesta:
    if numero > respuesta:
        print("El numero es mayor que la respuesta")
        numero = int(input())
    if numero < respuesta:
        print ("El numero es menor que la respuesta")
        numero = int(input())
    if numero == respuesta:
        print("Correcto!!") 
        break