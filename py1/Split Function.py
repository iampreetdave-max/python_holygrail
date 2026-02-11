# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:02:04 2024

@author: student
"""

#TO make number of string in assign string
# Syntax : string.split(separator,maxsplit)
# By default space is used as separator
# Scenerios:
     # string.split()
     #string.split(',')
     #string.split(',',2)
a='Hello world'
b='Hello,World'
c='a,b,c,d'
print(a.split())
print(b.split(','))
print(c.split(',',4))
 