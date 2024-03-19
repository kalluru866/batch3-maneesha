 #day7
'''
d1 = {'ten':10,'twenty':20,'thirty':30}
d2 = {'thirty':30,'fourty':40,'fifty':50}
d1.update(d2)
print(d1)


set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c=0
flag=0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==3:
        for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flag==0:
    print("disjoint")
else:
    print("joint")
    



list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3 = []
for val in range(len(list1)):
    ans=list1[val]+list2[val]
    l3.append(ans)
print(l3)


#using while loop
i=0
while i<len(list1):
     l3.append(list1[i]+list2[i])
     i+=1
print(l3)

#functions
#eg:1
def greet():
    print("moti down down! !")
greet()
greet()

#eg:2
#?function with parameter
def greeting(name):
    print("welcome",name)

for val in range(3):
    username = input("enter the name:")
    greeting(username)


def profile(*name,age):
    for val in name:
        print("my name is",val,"may age is",age)
profile("sid",'name2','name3',23)


def profile(age,*name):
    for val in name:
        print("my name is",val,"may age is",age)
profile(28,"sid",'name2','name3')

#*keyword variable length args
#kwargs--> which is used to provude the args in the form of key value pair
#eg:1
def price(**pricr_list):
    print(price_list)
price(shirt=1000,iphone=80000)


n=5
{1:1,2:4,3:9,4:16,5:25}

n=int(input("enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val] = val**2
print(d1)
##
def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val] = val**2
    print(d1)
dict1(5)

#!-->object oriented programming
#the paradigms of objects oriented programming are
#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation

# ! class is a blue of an object
l1 =[1,2,3,4,5,6,7]
#eg:1
class c1:
    name = "MOTI"
    print(name1)
#eg:2
class person:
  name="sidhu"
c=person()
print(c.name)

#eg:3
#create of a method
#when the function is created with a class is called as method

class person:
    def display(person):
        print("hello welocome to classel")
p=person()
p.displ
#eg:4
class person:
    def display(person,name,age):
        print(name,age)
p=person()
p.display("sid",43)

#?eg:5
class person:
    fname = "sid"
    lname = "k"
    def first_name(self):
        print(self.fname)
    def full_name(self):  
        print(self.fname+" "+self.lname)
p = person1()
p.first_name()
p.full_name()
'''
#?eg:6
#constuctor-->__init__()
#this is a special method which has the ability to execute iotself without
#calling it manullay through the process of instantiation
class profile:
    def__init__(self):
        print("oy")
p=profile()













          



