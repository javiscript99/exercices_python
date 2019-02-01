# -*- coding: utf-8 -*-

year=int(input())
print("Introduce un año para saber si es bisiesto")
if(year % 4 == 0 or year % 400 == 0 and year % 100 != 0):
 print("Si es bisiesto ")
else:
 print("No es bisiesto")