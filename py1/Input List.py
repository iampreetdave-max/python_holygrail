# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:06:18 2024

@author: student
"""
'''list=[] #empty list
n=int(input('Size of the list')) #length
for i in range(0,n):
    print("Entre input")
    item=int(input()) #To add the item in list
    list.append(item) #only at end
print("The list is",list)

#for any external task on list :
print("four element:",list[:4]) #example
#---------------------------------------------------------------------------------------------------------
#Imp Question for Exam: (1)length 8 print first 4
# (2): length 7, print last 4
# (3) : length 7 print last 4 using -ve index
# (4): length 18 , print reverse
# (5): length 7 , print 1st 3rd 5th 7th
# (6): length 10, print 2nd 4th 6th 8th 10th using slice


list=[] 
n=int(input('Size of the list')) 
for i in range(0,n):
    print("Entre input")
    item=int(input()) 
    list.append(item) 
print("The list is",list)
print("The first 4 elements are",list[:4])  #1
print("The last 4 elements are",list[3:8]) #2
print("The last 4 elements using negative index are",list[-4:]) #3
print("The list in reverse is",list[::-1])#4
print("The 1st,3rd,5th&7th term are",list[0:7:2]) #5
print("The 2nd,4th,6th,8th&10th term are",list[1:10:2]) #6'''

#---------------------------------------------------------------------------------------------------------
#printing star :
def star(n):
    for i in range (0,n):
        for j in range(0,i+1):
            print("*",end="") #end will print till the range ends
        print('\r') #\r is used to switch rows
x=int(input("Enter a value"))
star(x)
#printing values :
def star(n):
    for i in range (0,n):
        for j in range(0,i+1):
            print(j+1,end="") 
        print('\r') 
x=int(input("Enter a value"))
star(x)

def star(n):
    for i in range (0,n):
        for j in range(0,i+1):
            print(i+1,end="") 
        print('\r') 
x=int(input("Enter a value"))
star(x)
#mirror image of last function ;
def star(n):
    for i in range(1,1+n):
        for j in range(n,0,-1):
         if j>i:
            print(" ",end="")
         else :
            print(i,end="")
        print('\r')
x=int(input("ENter a Value"))
star(x)

def star(n):
    for i in range (n,0,-1):
        for j in range(0,i):
            print(i,end="") 
        print('\r') 
x=int(input("Enter a value"))
star(x)

n=int(input("Enter value"))
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        print(j,end="")
        j=j+1
    print()
    i=i+1
    
n=int(input("Enter a value"))
for i in range(n+1,1,-1):
    for j in range(1,n-i+2):
        if(i%2==0):
            print('1',end="")
        else :
            print('0',end="")
    print()
    
m=int(input("Enter a value"))
for i in range(m+1,1,-1):
    for j in range(0,m-i+2):
        if(i%2==0):
            print('0',end="")
        else :
            print('1',end="")
    print()
    
#--------------------------------------------------------------------------------------------------------

def star(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(i+65),end="")
        print('\r')
x=int(input("Enter a value"))
star(x)