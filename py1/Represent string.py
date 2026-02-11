# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:16:58 2024

@author: student
"""

# (1) Using ','
# (2) Using '+"
# (3) Using format{}

#(1)
a='Hello'
b='World'
print(a,"",b)
print(a,b)
print("first and second",a,b)
#(2)
c=a+b
print(c)
print(a+""+b)
#(3)
age=12
name='Shiv'
order="My name is {} and age is {}"
print(order.format(name,age))

