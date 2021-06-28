# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:01:56 2021

@author: Jose Alcivar Garcia
"""

horas= int(input("ingresa las horas trabajadas: "))
pago= float(("ingresa el pago por horas: "))
triples=0
dobles=0
sueldo=0
if horas > 40:
    triples=horas-40
    dobles=0
    sueldo=(40*pago)+(dobles*pago*2)+(triples*pago*3)
else:
    sueldo-horas*pago

print("el sueldo por las ", horas,"horas es: $", sueldo)
print("se pago", dobles, "horas al doble es: $", dobles*pago*2)
print("se pago", triples, "horas al triples es: $", triples*pago*3)