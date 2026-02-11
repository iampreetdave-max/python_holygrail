

def prime(n):
  for x in range (2,n):
    if(num%x==0):
        return 0
    else:
        return 1
    
num=int(input("enter a number "))
print(prime(num))

if(prime(num)==0):
    print("not prime")
    
else:
    print("prime")