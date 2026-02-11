# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:07:16 2024

@author: student
"""
#Functions ;;
#---------------------------------------------------------------------------------------------------------
def my_function():
    print("Hii")
my_function()
# def function_name (n) :
#                 parameter
#   print("hii",n,)
#function_name()
#          argument

def my_function(n):
    print(n*n)
my_function(3)
#parameter will be considered as argument , hence number of argument should be equal to parameter
#---------------------------------------------------------------------------------------------------------
#using multiple argument ;

def my_function(fname,lname):
    print('python says',fname,lname)
my_function("Hello","World")


def my_function(lname,fname):
    print('python says',fname,lname)
my_function("Hello","World")
#fname is considered as world in case 2 while fname is considered as hello in case 1,
# hence parameter and argument are selected using index value
my_function("Good","Morning")
my_function("ABC","XYZ")
my_function("AXY","BCZ")
#---------------------------------------------------------------------------------------------------------

#Even odd function : 
    
def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd(2)
even_odd(3)
even_odd(5)
even_odd(6)
#---------------------------------------------------------------------------------------------------------
#Arbitary argument ;
#Number of argument and parameter are not same but index value is selected for output

def my_function(*n):
    print("The print is",n[2])
my_function('A','B','C','D')

def key_word(A,B,C):
    print("the name is ",A)
key_word(A='HI',B='HELLO',C='WORLD')

#Arbitary Keyword Argument :
def key_word(**name): 
#dictionary has two values (key,value) hence two hashtach are used
#while for integer, single hashtach is used 
    print("Name",name['lame'])
key_word(fname='A',lame='B')
#---------------------------------------------------------------------------------------------------------
#Default Argument
def my_function(country="India"):
   print("I am from:",country)
my_function("Sweden")
my_function("Brazil")
my_function()
 #no argument is given in last so, parameter is printed as default argument & if parameter is not given,
 #error is given

