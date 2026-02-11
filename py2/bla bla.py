#!/usr/bin/env python
# coding: utf-8

# # array implementation 1-d 

# In[5]:


from array import *

#i=int d=float

num=array('i',[1,2,3,4,5])

for z in num:
    print(z)
    
    

print(num)


#                             wap to print 10 elements of float

# In[7]:


from array import*

num=array('d',[1.6,3.5,5.4,54.,65,6.65,65,64.5,9,10])

for a in num:
    print(a)


#                                        APPEND
# 

# In[9]:


from array import *

num=array('i',[1,2,3,4])

num.append(5)

for a in num:
    print(a)


# In[15]:


from array import *

num=array('i',[1,2,3,4])
print("apend 5 and replace 3 with 100")
num.append(5)

num[2]=100

for a in num:
    print(a)
    
print("after using remove on 100")
num.remove(100)

for a in num:
    print(a)
    
print("using delete on num[1]")
del num[1]

for a in num:
    print(a)


#                              import array as arr 
#                            num=arr.array('i',[1,5,6])
#                         

#                           array initialization by taking input
# 

# In[26]:


from array import *
num=array('i',[])

x=int(input("enter size of array:"))

for i in range(0,x):
    z=int(input("enter input:"))
    num.append(z)
    
print(num)

print("reverse")

for i in range(x-1,-1,-1):
    print(num[i])
    
    
#slice function  
print(num[::-1])
    


#                             wap to find sum of array
#                             

# In[31]:


from array import *
num=array('i',[])
sum=0
x=int(input("enter size of array:"))

for i in range(0,x):
    z=int(input("enter input:"))
    num.append(z)
    
for i in num:
    sum=sum+i
    
    
print(sum)


# #                                     # HW
# 1=search if element present in array
# 2=find min
# 3=find max
# 4=find mising element in serires 

# In[40]:


from array import *
num=array('i',[])
sum=0
x=int(input("enter size of array:"))

for i in range(0,x):
    z=int(input("enter input:"))
    num.append(z)
    
n=int(input("enter element to check:"))
c=0
for i in num:
    if i==n:
        c=c+1
    
if c>0:
    print("present")


# In[44]:


from array import *
num=array('i',[])
sum=0
x=int(input("enter size of array:"))

for i in range(0,x):
    z=int(input("enter input:"))
    num.append(z)
    

max=0
for i in num:
    if i>max:
        max=i
        
print(max)
        


# In[46]:


from array import *
num=array('i',[])
sum=0
x=int(input("enter size of array:"))

for i in range(0,x):
    z=int(input("enter input:"))
    num.append(z)
    

min=num[0]
for i in num:
    if i<min:
        min=i
        
print(min)


# In[13]:


from array import *
num=array('i',[])
sum=0
x=int(input("enter size of array:"))

for i in range(0,x):
    z=int(input("enter input:"))
    num.append(z)
mis=0    
for z in range(0,x-1):
    if num[z+1]-num[z]!=1:
        mis=num[z]+1
        print(mis,"is the missing number ")
    


# #                                    2-D array 
#                                      with numpy

# In[24]:


import numpy as np

x=np.array([[1,2],[3,4],[0,0]])

print(x)
a=int(input("new element"))
b=int(input("new"))
x[2]=[a,b]

print("first row after replacementt",x[0])
print(x)


# # stack        
# last in first out-
# push,pop,empty,peek,clear
# 
# 
# 

# In[35]:


stack=[]

n=int(input("enter size"))

for i in range(0,n):
    a=input("enter a element")
    stack.append(a)        #push
    
stack.pop()
print(stack)
l=len(stack)
print("length of stack is:",l)
stack.clear()
if not stack:
    print("stack is cleared")

#print(stack)


# reverse of array with pop

# In[33]:


stack=[]

n=int(input("enter size"))

for i in range(0,n):
    a=input("enter a element")
    stack.append(a)     
    
    
    
stack2=[]
for i in range(0,n):
    p=stack.pop()
    stack2.append(p)
    
    
print(stack2)


# wap to ask user to push or pop

# In[42]:


stack=[]

n=int(input("enter size"))

for i in range(0,n):
    a=input("enter a element")
    stack.append(a)     
    
c=int(input("enter 1 to push a element \n 2 to pop a element"))

if c==1:
    x=input("enter element to push:")
    stack.append(x)
    
elif c==2:
    stack.pop()
    
else:
    print("invalid")
    
print(stack)


# In[3]:


#sorting array 
from array import *

num=array('i',[])


n=int(input("enter size of array"))

for i in range(0,n):
    p=int(input("enter a element"))
    num.append(p)
temp=0
for i in range(0,n):
    for j in range(0,n):
        if(num[i]<num[j]):
            temp=num[j]
            num[j]=num[i]
            num[i]=temp
            
            print(num)
            
        


# # BUBBLE SORT
#  compares neigbouring elements
#  

# In[ ]:


from array import * 
num=array('i',[])

n=int(input("enter size:"))

for i in range(0,n):
    x=int(input("enter val:"))
    num.append(x)
temp=0
sum=0
for j in range(0,n-1):
    for i in range(0,n-1):
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
            
        sum=sum+1
        print(num)
print(sum)
    


# # selection sort

# In[17]:


from array import *
num=array('i',[])

x=int(input("enter size:"))

for i in range(0,x):
    a=int(input("enter val:"))
    num.append(a)


for i in range(0,x):
    for j in range(i+1,x):
        if num[j]<num[i]:
            min=num[j]
            num[j]=num[i]
            num[i]=min
print(num)
            

        


# In[26]:


#alternate method with indexs
from array import *
num=array('i',[])

x=int(input("enter size:"))

for i in range(0,x):
    a=int(input("enter val:"))
    num.append(a)


for i in range(x):
    min=i
    for j in range(i+1,x):
        if num[j]<num[i]:
            min=j
            num[i],num[min]=num[min],num[i]
print(num)


# ## stack implementation using deque modle

# In[15]:


#demonstrate usage of deque module in stack implementation by taking ip from user
#store to left to right thai
#default pop right thi thai
from collections import deque
stack=deque()

n=int(input("enter size:"))

for i in range(0,n):
    p=input("element:")
    stack.appendleft(p)
    
stack.pop()
print(stack)
stack.popleft()
print(stack)


# # queue implimentation using deque module

# In[16]:


from collections import deque
queue=deque()

n=int(input("enter size:"))

for i in range(0,n):
    p=input("element:")
    queue.appendleft(p)
    
queue.pop()
print(queue)
queue.popleft()
print(queue)


# ## QUEUE IMPLEMENTATION  USING LIST METHOD 

# In[17]:


queue=[]
x=int(input("enter size"))

for i in range(0,x):
    z=int(input("element:"))
    queue.append(z)
    
print(queue)

queue.pop(0)
queue.pop(0)     #popleft
print(queue)


# # queue implimentation using queue module

# In[24]:


from queue import Queue
q=Queue(maxsize=5)
q.put(1)
q.put(20)
q.put(300)

q.get()
q.get()
#q.get()


print(list(q.queue))
print(q.empty())  #check if queue is empty or not


# In[30]:


#big ahh question to implement fifo struct implement queue with max size menue based program to show push pop and check if queue is empty or not 
from queue import Queue
q=Queue()

n=int(input("enter size:"))

for i in range(0,n):
    p=input("enter element:")
    q.put(p)
    
print(list(q.queue))
print("press 1 to add/push a element\npress 2 to remove/pop a element\npress 3 to check if queue is empty \n 4 to check size of queue")
c=int(input("enter your choice:"))

if c==1:
    a=input("enter new element:")
    q.put(a)
    print(list(q.queue))
elif c==2:
    q.get()
    print(list(q.queue))
    
elif c==3:
    print(q.empty())

elif c==4:
    print(q.qsize())
    
else:
    print("invalid choice")


# ## wap to implement reverse of queue using deque module(you can utilise pop left and append left)and store the result in seperate queue

# In[5]:


from collections import deque
queue=deque()
queue2=deque()

n=int(input("enter size:"))

for i in range(0,n):
    p=input("element:")
    queue.append(p)
    
for i in range(0,n):
    b=queue.popleft()
    queue2.appendleft(b)
    
    
print(queue2)


# # object oriented programing 
# 

# defining class

# In[1]:


class person:
    def __init__(pas,name,height,weight):
        pas.name=name
        pas.height=height
        pas.weight=weight
        
    def dis(pas):
        print("name is:",pas.name,"height is:",pas.height,"ft","weight is",pas.weight)
        
        
        

p1=person('preet',7,100)
p1.dis()


# In[ ]:


class person:                                     #constructor
    def __init__(pas):
        pas.name=input("enter name:")
        pas.height=int(input("enter height:"))
        pas.weight=int(input("enter weight:"))
        
    def dis(pas):
        print("name is:",pas.name,"height is:",pas.height,"ft","weight is",pas.weight)
        
        
        

p1=person()          #driver code
p1.dis()


# wap to get marks using class and obj implementation

# In[5]:


class person:                                     #constructor
    def __init__(std):
        std.name=input("enter name:")
        std.math=int(input("enter marks of math:"))
        std.sci=int(input("enter marks of sci:"))
        std.eng=int(input("enter marks"))
        
    def dis(std):
        print("name is:",std.name,"\nmarks in math is:",std.math,"\nmarks in sci is:",std.sci,"\nmarks in eng is:",std.eng)
        print("\n=====================================================")
        


s1=person()
s2=person()
s3=person()         #driver code
s1.dis()
s2.dis()
s3.dis()


# In[7]:


class person:                                     #constructor
    def __init__(std):
        std.name=input("enter name:")
        std.math=int(input("enter marks of math:"))
        std.sci=int(input("enter marks of sci:"))
        std.eng=int(input("enter marks"))
        
    def dis(std):
        print("name is:",std.name,"\nmarks in math is:",std.math,"\nmarks in sci is:",std.sci,"\nmarks in eng is:",std.eng)
        print("\n Total marks obtained:",std.math+std.sci+std.eng)
        print("\n avg:",(std.math+std.sci+std.eng)/3)
        print("\n=====================================================")
        


s1=person()
s2=person()
s3=person()         #driver code
s1.dis()
s2.dis()
s3.dis()


# find area of circle for 7 diffrent radius
# 

# In[11]:


class circle:
    def __init__(cir):
        cir.radius=int(input("enter radius"))
        
    def dis(cir):
        area=cir.radius*cir.radius*3.14
        print("area of radis",cir.radius,"is",area)
        
r1=circle()
r2=circle()
r3=circle()
r4=circle()
r5=circle()
r6=circle()
r7=circle()

r1.dis()
r2.dis()
r3.dis()
r4.dis()
r5.dis()
r6.dis()
r7.dis()


        
    


# In[12]:


class swap:
    def __init__(sw):
        sw.a=int(input("enter num1:"))
        sw.b=int(input("enter num2:"))
        
    def dis(sw):
        print("values before swaping:",sw.a,sw.b)
        c=sw.a
        sw.a=sw.b                        #sw.a,sw.b=sw.b,sw.a
        sw.b=c
        print("values after swaping:",sw.a,sw.b)
        
        
s1=swap()
s1.dis()


# In[16]:


class table():
    def __init__(tab):
        tab.t1=int(input("enter value 1:"))
        
        
        
    def ans(tab):
        for i in range(1,11):
            print(tab.t1,"X",i,"=",i*tab.t1)
        print("========================================")
            
t1=table()
t2=table()
t3=table()
t1.ans()
t2.ans()
t3.ans()


# In[23]:


class table():
    def __init__(tab):
        tab.t1=int(input("enter value 1:"))
        
        
        
    def ans(tab):
        sum=1
        for i in range(tab.t1,0,-1):
    
            sum=i*sum
        print(sum)
        print("========================================")
            
t1=table()
t2=table()
t3=table()
t1.ans()
t2.ans()
t3.ans()


# In[25]:


class fact():
    def __init__(fac):
        fac.f1=int(input("enter a number:"))
    
    def ans(fac):
        for i in range(1,fac.f1+1):
            if fac.f1%i==0:
                print(i,"is factorial of",fac.f1)
                
f1=fact()
f1.ans()
        
    
        


# In[26]:


class check():
    def __init__(c):
        c.num=int(input("enter a number to check:"))
        
    def che(c):
        if c.num%2==0:
            print("number is even")
        else:
            print("number is odd")
            
v1=check()
v1.che()


# In[28]:


class length():
    def __init__(le):
        le.length=input("enter a string:")
        
    def ans(le):
        print("length:",len(le.length))

        
l1=length()
l1.ans()


# In[35]:


class length():
    def __init__(le):
        le.length=input("enter a string:")
        
    def ans(le):
        c=0
        for i in le.length:
            c=c+1
        print("length:",c)
        
v1=length()
v1.ans()


# In[37]:


class mul():
    def __init__(ch):
        ch.num=int(input("enter a number:"))
        
    def ans(ch):
        if ch.num%7==0:
            print(ch.num,"is a mulltiple of 7")
            
        else:
            print(ch.num,"is not a multiple of 7")
            
            
v1=mul()
v1.ans()


# In[2]:



class table():
    count=0
    def __init__(tab):
        
        table.count+=1
        tab.t1=int(input("enter value 1:"))
        
        
        
    def ans(tab):
        sum=1
        for i in range(tab.t1,0,-1):
            sum=i*sum
        print(sum)
        print("========================================")

t1=table()
t2=table()
t3=table()
t1.ans()
t2.ans()
t3.ans()

print(table.count)


# In[4]:


class check():
    def __init__(a):
        a.num=int(input("enter a number:"))
        
        
    def dig(a):
        l=a.num%10
        if l%2==0:
            print("even")
            
        else:
            print("odd")
            
            
            
n1=check()
n1.dig()


# In[15]:


class check():
    def __init__(a):
        a.num=int(input("enter a number:"))
        
        
    def dig(a):
        l=a.num%10
        m=(a.num//10)%10
        f=a.num//100
        t=l+m+f
        
        print(t)
            
            
n1=check()
n1.dig()


# In[21]:


class fact():
    def __init__(f):
        f.num=int(input("enter a number:"))
        
    def check(f):
        count=0
        for i in range(1,f.num+1):
            if f.num%i==0:
                count=count+1
                print(i,"is a factor of",f.num)
        print("number has ",count,"factors")

n1=fact()
n1.check()


# In[24]:


class fact():
    def __init__(f):
        f.num=int(input("enter a number:"))
        
    def check(f):
        count=0
        for i in range(1,f.num+1):
            if f.num%i==0:
                count=count+1
                
        if count>2:
            print("number is not prime")
                
        else:
            print("number is prime")

n1=fact()
n1.check()


# In[27]:


class arm():
    def __init__(a):
        a.num=int(input("enter a number"))
        
    def arms(a):
        l=a.num%10
        m=(a.num//10)%10
        f=a.num//100
        if (l*l*l)+(m*m*m)+(f*f*f)==a.num:
            print("number is armstrong")
            
        else:
            print("number is not armstrong")
        
n1=arm()
n1.arms()


# In[28]:


class string():
    def __init__(a):
        a.s=input("enter a string")
        
    def fun(a):
        v=0
        c=0
        for i in a.s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                v=v+1
                
            else:
                c=c+1
        print("vowels:",v)
        print("cons:",c)

        
s1=string()
s1.fun()


# In[ ]:




