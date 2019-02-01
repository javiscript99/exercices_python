# -*- coding: utf-8 -*-
import math

print("Introduce el primer valor")
a = int(input())
print("Introduce el segundo valor")
b = int(input())
if (0<=a<=b):
    print("La raiza cuadrada del sumatorio de ", a , " a " , b , " es: ")
    i = sum(list(range(a, b + 1)))
    print (math.sqrt(i))