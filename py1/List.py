# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:18:23 2024

@author: student
"""

list=['a',1,2.2,3]
print(list)
print(len(list))
print(type(list))
#update in list ;
list[2]= 4
print("update:",list)
#Access ;
print("the number 2 is ",list[2])
#Delete ;
list.remove(1)
print(list)
#Range ;
print("Range is", list[2:4])
#Insert ;
list.insert(2,4)
print(list)
#ADD,( IN Last );
list.append(6)
print(list)
#Sort ;(only used when smae type of values are present in list (eg: integer))
list.sort()
print(list) # values not same type in list hence error