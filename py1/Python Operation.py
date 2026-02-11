#Arithmetic operation: 
    #+,-,*,%,/,**,//
a=5
b=2
print("+ =", a+b)
print("- =", a-b)
print("* =", a*b)
print("% =", a%b)
print("/ =", a/b)
print("** =", a**b)
print("// =", a//b)

#Assignmemts:
    # a=1 ; 1 assigned to a
    # b* = 3 ; b=b*3
    # a+ = 4 ; a=a+4
#Comparison:
     # == ; equal
     # >,< ; greater, smaller
     # ! ; not equal
     # > ; greater than equal to
     # < ; smaller than equal to
#Logical :
     # (1)AND ; both true
     # (2)OR ; any one true
print(a>b and a==b)
print(a>b or a==b)
print(a==b and a<b)
#Identity :
     #(1)IS ; 
     #(2)IS NOT ; 
print(a is b)
print(a is not b)
#Membership :
    #(1)IN ;
    #(2)NOT IN ;
a='Hello'
print('H' in a)
#Bitwise :
     # (1) & AND; each bit set '1' if both are '1'
     # (2) | OR ; each bit set to '1' if one or both are '1'
     # (3) ^ XOR; each bit set to '1' if only one bit is '1'
     # (4) ~ NOT; invert all bit
print(6&3)
print(6|3)
print(6^3)
print(~4)