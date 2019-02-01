# -*- coding: utf-8 -*-

salario = int(input())


if (0< salario <=12450):
    calculadoUno = (salario*19)/100
    print(calculadoUno, " IRPF aplicado del 19%")
    print("Salario final " ,salario-calculadoUno)

if (12451<= salario <=20200):
    calculadoDos = (salario*24)/100
    print(calculadoDos, " IRPF aplicado del 24%" )
    print("Salario final " ,salario-calculadoDos)

if (20201<= salario<= 35200):
    calculadoTres = (salario*30)/100
    print(calculadoTres, " IRPF aplicado del 30%")
    print("Salario final " ,salario-calculadoTres)
    
if (35201<= salario<= 60000):
    calculadoCuatro = (salario*37)/100
    print(calculadoCuatro, " IRPF aplicado del 37%")
    print("Salario final " ,salario-calculadoCuatro)
    
if (salario>60000):
    calculadoCinco = (salario*45)/100
    print(calculadoCinco, " IRPF aplicado del 45%")
    print("Salario final " ,salario-calculadoCinco)