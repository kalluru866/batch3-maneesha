#day2:
'''
#swapping of variables
a=7
b=5
temp=a
a=b
b=temp
print(a,b)
#eg:2

a=a+b 
b=a-b
a=a-b
print(a,b)

a=a*b
b=a/b
a=a/b
print(int(a),int(b))

#id()--> used to find the memory address of the variables
a=6
b=5
print(id(a))
print(id(b))

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

#literals
#literals is the constant value assigned to a variable
#a variable is considers to be constant when it is defines
#in caps
#a=78 # a is variable
#A=78 # A is constant
n1 = 89+7j
print(hash(n1))
f1=[7,8,9]
print(hash(f1))


#arithmatic
a=8
b=7
c=8
print(a+b+c)
print(a-b-c)
n1 = input("enter the value:")
print(type(n1))
#floor devision
a=765433
b-19
print(a//b)
print(a/b)
print(4*16)
print(2*4)

a=8
a+=2
print(a)
a=30
a-=5
print(a)
#comparison
a=8
b=7
print(a>b)
a=9
b=5
print(a==b)
# ! bitwise operator
a=7
b=4
print(a&b)

# ! logical
# and,or,not
a=6
print(a>3 and a<10)
print(not(a>8 and a<10
 #! identity
# is not
# it is used to compere the memory location
a=8
b=8
print(a is b)
print(a==b)
a=[1,2,3]
b=[1,2,3]
print(a is not b)
# ! membership  0perator
# in ,not,in
l1=[3,11,15,20]
num=3
print(num in l1)

# conditional statement

a=6
if a:
   print("h
eg:3
a=6
if a>3:
    print("hey")
else:
    print("no")
eg:4
a=0
a=None
a=False
a=""
if a:
     print("yes")
else:
     print("no")
# a number is even or odd
n=int(input("enter the number"))
if n%2==0:
      print(n,"is even")
else:
     print(n,"is odd")
'''
# name,age,nationality
name = (input("enter a number:"))
age = int(input("enter a name:"))
nationality=(input("enter the nation:"))
if age>=18 and nationality=="indian":
    print("eligible")
else:
    print("not eligible")



























          
          

          
