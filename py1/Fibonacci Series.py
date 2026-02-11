# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:44:37 2024

@author: student
"""

#two variables are fix : 0,1 & further values are sum of corresponding 2 values
# 0,1,1,2,3,5,8...
# 0,1,2,3,4,5,6     : index values
#for example index value 3 = [n-2]+[n-1]

#method 1 ;

X=int(input("highest Range(index value) of fibonacci series"))
n1,n2=0,1
print("Fibonnaci series is",n1,n2,"",end="")
for i in range (2,X):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()

#method 2 ;
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else :
        return fib(num-2)+fib(num-1)
n=int(input("Enter the index value"))
for i in range(0,n):
    print(fib(i))