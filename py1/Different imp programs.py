# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:08:30 2024

@author: student
"""

# TO write a program to convert km into m,feet,inch,centimeter :
    # feet = km*3280.84
    #inch = km*39370.1
    
Value=int(input("Enter the Value in kilometer"))

print("Select conversion unit")
print("1. Feet")
print("2. meter")
print("3. inch")
print("4. centimeter")

choice=int(input("Enter choice (1,2,3,4):"))
if choice==1:
     result=Value*3280.84
     
elif choice==2:
    result=Value*1000
    
elif choice==3:
    result=Value*39370.1
    
elif choice==4:
    result=Value*100000
else :
    print("An error occured")
print("The answer is",result)
#---------------------------------------------------------------------------------------------------------
#Write a program to find first,second and third digit(alphabet)
  # 201 & ABC
  
Name=input("Enter a value")
print("first digit",Name[0])
print("Second value",Name[1])
print("Third Value",Name[2])
#---------------------------------------------------------------------------------------------------------

#Write a program to find sum of n digit :
    
n=int(input("Enter the value"))
sum=0
for i in str(n) :
    sum+=int(i)
print("The sum is",sum)
#---------------------------------------------------------------------------------------------------------

    