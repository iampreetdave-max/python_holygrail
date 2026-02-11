# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:11:49 2024

@author: student
"""
#Print maximum value using function ;
def keys(Num1,Num2,Num3):
    if Num1>Num2 and Num1>Num3 :
        print("Max",Num1)
    elif Num2>Num1 and Num2>Num3 :
        print("Max",Num2)
    else :
        print("Max",Num3)
keys(1,3,6)
keys(5,6,9)
A=Num1=int(input("Enter a value"))
B=Num2=int(input("Enter a value"))
C=Num3=int(input("Enter a value"))
keys(A,B,C)
#---------------------------------------------------------------------------------------------------------
#Return Function : Function return value without statement ;
#SYntax :
    # def function_name :
        # return.........
    # function_name()
    
def product(n):
    return 5*n #print not required below or inside def function
print(product(5))
print(product(7))
print(product(4))
#---------------------------------------------------------------------------------------------------------
#Factorial using return function :
def recursive(n):
    if n==1 :
        return n
    else :
        return n*recursive(n-1)
number=int(input("Enter a Number"))
print("The Factorial is",recursive(number))
#---------------------------------------------------------------------------------------------------------


