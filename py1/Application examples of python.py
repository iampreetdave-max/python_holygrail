# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:17:52 2024

@author: student
"""
#Tables
Num=int(input("Enter the number for table"))
i=Num
for j in range(1,11):
   print(i,"x",j,"=",i*j)
#------------------------------------------------------------------------------
#Sum of n number :
i=int(input("Enter a Number"))
sum=0 #empty variable taken which is necessary
for j in range(0,i+1):
    sum=sum+j
print(sum)
#------------------------------------------------------------------------------
 #converting celsius to fahrenheit and farenheit to celsius :
     # c=(f-32)*1.8  &  f=(c*1.8)+32
value=int(input("Enter a value"))
print("Select unit")
print("1. fahreinheit")
print("2. celsius")

choice=input("Enter Choice from 1,2")
if choice=='1':
    result= (value-32)*1.8
elif choice=='2':
    result= (1.8*value)+32
else :
    print("error occured")
print(result)
#------------------------------------------------------------------------------
 #to check even odd : (range)
n=int(input("Enter a number"))
u=int(input("Enter a number"))
for X in range(n,u+1):
    if X % 2 == 0 :
        print(X,"is even")
    else :
        print(X,"is odd")
 # to check even odd (number):
n=int(input("Enter a Number"))
if (n % 2 == 0):
    print(n,"is even")
else :
    print(n,"is odd")
#------------------------------------------------------------------------------
 #List printing first 4 elements,last 4 elements, 2-6 elements, 
 #print(8th,9th,2nd)element
List=[1,2,3,4,5,6,7,8,9,10]
print(List[0:4])


