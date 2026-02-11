# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:58:53 2024

@author: student
"""

# Swaping without third variable 
#a & b 
# a,b = b,a
# print(b,a)

# Swaping with third variable 
# a & b 
# c=a , a=b, b=c
# print(a,b,)
    
# Without Third Variable
Num_1=int(input("Enter a Number"))
Num_2=int(input("Enter a Number"))
Num_1,Num_2=Num_2,Num_1
print(Num_2,Num_1)

# With using Third Variable
Num_3=Num_1
Num_1=Num_2
Num_2=Num_3
print(Num_1,Num_2)