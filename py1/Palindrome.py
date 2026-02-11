# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:51:55 2024

@author: student
"""

#reverse should be equal to original value 
#eg: 121=121

#using slice function ;
num=input("Enter a value")
Rev=(num[::-1])
if Rev==num:
    print("true ; palindrome")
else :
    print("False ; not palindrome")
    
#using string function ;

def palin(s):
    rev= "" .join(reversed(s))
    if s==rev :
        return True
    else: 
        return False
s=input("Enter a value")
ans=palin(s)
if(ans):
    print("yes")
else :
    print("no")
    
#without using any function
    

x=input("enter a value")
w= ""
for i in x :
    w=i+w
if (x==w):
    print("yes")
else :
    print("no")
    