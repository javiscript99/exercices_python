# -*- coding: utf-8 -*-

passw = input()

numeros = 0
mayus = 0
minus = 0
espacio = 0

for carac in passw:
    if (carac.isdigit()):
        numeros+=1
    
    if (carac.isupper()):
        mayus+=1
    
    if (carac.islower()):
        minus+=1
        
    if (carac.isspace()):
        espacio+=1
    
if (len(passw)>=12 and numeros>=1 and mayus>=1 and minus>=1 and espacio == 0):
    print("Valida")
    
else:
    print("No valida; Revisa que no tenga espacios, que almenos contenga una minúscula, una mayúscula, un número y que contega 12 o más caracteres")



