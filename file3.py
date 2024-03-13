DAY:3
'''
# ! eg:3
length = int(input("enter a length:"))
breadth = int(input("enter a breadth:"))
if length==breadth:
    print("it is a square")
else:
    print("it is not a square")
# ! eg:4
n = int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
#eg:5
n=int(input("enter the price:"))
amount=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    amount=value*(15/100)
    print(value+amount)
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is:",total)

# !---> if elif else
#eg:1
a = 7
b = 9
c = 3
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
    
n=int(input("enter the mark"))
if mark>80 and mark<=100:
      print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=60 and mark<80:
     print("C")
elif mark>=50 and mark<60:
    print("D")
else:
    print("fail")

a=9
b=60
print("A") if a>b else print("B")

# code to check the given char is vowel or constant
char = input("enter the char:")
if char=="a" or char=='e' or char =='i' or char =='o' or char =='u':
    print("is a vowel")
else:
    print("its cinsonent")
    
# same
char= input("enter the char:")
str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonnt")

# shorthand if else
char=input("enter the char:")
str1="aeiouAEIOU"
print("vowel")if char in str1 else print("consonent")

# elif ladder using short hand if else
a=8
b=9
c=7
print("a is greater") if a>b and a>c  else print("b is greater") if b>a and b>c else print("C is greater")

# !----> looping
#looping can be implimented using
#for loop
#while loop
#---> for loop
#for loop is used for iteartion,ifwe know the number of times the loop have to run
# it is used to iterate the iterable eg(string,list,tuple,etc...)
#syntax for loop
# ! for syntax in python
#statement
#statement
#statement
#eg:1
# to print the value from 1 to 10 using for loop
for i in range(0,10):
    print(i)
    print("afrin")

#eg:2
for val in range(1,11,3): 
   print(val)
#3   
for val in range(1,15,3):
   print(val)
   
#?eg:3
#to decrement the value
for val in range(10,0,-2):
    print(val)

for val in range(10,0,-1):
    print(val)
    
# ? eg:4
# print the output of 7th multi[lication table from 21 to 43
for val in range(1,10+1):
    print('7','x',val,'=',val*7)
#method:2
ans="7 x {} = {}"
print(ans.format(val,val*7))
#methode:3
print(f"20f x {val}={val*20}")

#eg:1
#break
for val in range(1,10):
    print(val)
    if val ==6:
        break
#eg:2 
for val in range(1,10):
    if val ==6:
       print(val)
       break

#eg:3
for val in range(1,10):
    if val ==6:
        break
    print(val)

# ! continue
# eg:1
for val in range(1,10):
    if val ==6:
        continue
    print(val)

# practice problems
#print the even number b/w 20 to 40
for val in range(20,41,2):
    print(val)

#!-->while loop
#while is used when we do not know yhe number of times the loop have to r
# to iterate the non iterable elements while loop is used

#syntax
#initialisation
#while condition:
# statement#incre or decre

#eg:1
#to iterate number from 1 to 10
'''
i=o
while i<11:
    print(i)
    i=i+1
n=int(input("enter number:"))
sum=0
for val in range(1,n+1):
    sq=val*val
    if val%2!=0:
       sum=sum+sq
    else:
       sum=sum-sq
print(sum)



























































