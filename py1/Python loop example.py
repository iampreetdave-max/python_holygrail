# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:53:34 2024

@author: student
"""

fruit=['A','B','C','D']
for X in fruit : #condition gets printed in this case (B)
    print(X)
    if (X=='B'):
        break
#----------------------------------------------------------------
for X in fruit : #condition doesnt gets printed in this case
    if (X=='B'):
       break
    print(X) 
#----------------------------------------------------------------
 #Nested for 2 dimensions 
for i in range(1,4):
     for j in range(1,4):
      print(i,j)
    
