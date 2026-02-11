# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:21:43 2024

@author: student
"""

#example of armstrong number :
    # 153 = 1^3 + 5^3 + 3^3 
    #if both values are equal, it is an armstrong number 
    
def arm_strong(num):
    num_str=str(num)
    n=len(num_str)  # length
#calc digit :
    total=sum(int(digit)**n for digit in num_str)
#check equality ; 
    return total==num
num=int(input("Enter a value"))
if arm_strong(num):
    print(num,"yes")
else :
    print(num,"no")
