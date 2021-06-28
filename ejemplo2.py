# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:09:53 2021

@author: Jose Alcivar Garcia 
"""

sueldo= float(input("ingresa el sueldo: "))
a= float(input("ingresa la venta 1 "))
b= float(input("ingresa la venta 2 "))
c= float(input("ingresa la venta 3 "))

comision= (a+b+c)*.10
print("el sueldo del trabajador es: $", sueldo)
print("la comision del mes por las 3 ventas es: ", comision)
print("el sueldo total ya con la comision es: $", sueldo + comision)


