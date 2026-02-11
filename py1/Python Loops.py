# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:11:00 2024

@author: student
"""

# Loops : Whlie & For 
#While loop ;
count=3
while(count<7):
    count=count+1
    print("Hii")
    #break : to stop the Loop
i=1
while(i<6):
    print(i)
    if(i==3):
     break
    i=i+1
    #Continue: Do not print a particular statement
i=0
while(i<6):
    i=i+1
    if(i==3):
        continue
    print(i)

#For Loop ; used for iteration
A=['F','R','U']
for i in A: #i is a new variable which converts the content of A to act as integer
    print(i)
for X in "Banana": #X is new variable here
    print(X)  # for printing in single line : print(X,end="")
    #Range function : iteration through a set of limit
    # range(start,stop,step)
for X in range(6):
    print(X) #print using start =0 and step =1
for X in range(2,6):
    print(X) #prints 2,3,4,5 using start = 2 and end =5 & step=1
for X in range (2,30,3):
    print(X) #prints 2,5,8... using start =2,end = 30 & step = 3