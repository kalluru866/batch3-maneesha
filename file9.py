'''
#DAY9
#find the uncommon words from 2 strings
s1="hello how are you"
s2="hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

#write a code print the 8th fibanochi number
0,1,1,2,3,5,
num=8
n1=0
n2=1
for val in range(num):
    ans=n1+n2
    print(ans)
    n1=n2
    n2=ans

# ! constructors
#eg:2
class profile:
  def __init__(self):
      print("hello world")
obj = profile()
obj.__init__()

# ? eg:3
# parametarised constuctor
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
obj = profile(1,"sid",29)
# ? eg:4
class c1:
    email = "abhay@gmail.com"
    def m1(self):
        name = "abhay"
        place = "abc"
        print(name,place)
        print(self.email)
object = c1()
object.m1()

# ? eg:5

class c1:
    def m1(self):
        name = "abhay"
        age = 23
        return name,age
    def display(self):
       #! print(name,age)
       #! print(self.name,self.age)
        print(self.m1())
object = c1()
object.display()

# ? eg:6

class c1ass1:
    def __init__(self):
       self.name = "abhay"
       self.email = "abhay@gmail.com"
    def display(self):
        print(self.name,self.email)
c1 = class1()
c1.display

        
        
#!---->inheritance
# the process of utilising the methods and attributes of parent class
#throught the object of child class it is called as inheritance
#5 types of inheritance
#single inheritance
#multilevel inheritance
#multiple inheritance
#hybrid inherutance
#heirarichal inheritance

#*single inheritance
#it has only one parent class aad only child class
#eg:1
class parent:
    def m1(self):
        print("iam parent class")
class child(parent):
    def m2(self):
        print("iam child class")
obj = child()
obj.m1()

#eg:2
class c1:
    def __init__(self):
        print("i am constructor from parent class")
class child(c1):
    pass
obj = child()

#eg:3
class parent:
    name = "sid"
class child(parent):
    name = "name1"
    def display(self):
        print(self.name)
d = child()
d.display()

#! multilevel inheritance


class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")


'''
#multiple inheritance
#it has multiple parent and 1 child
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)
#!hy brid inheritance
#the combination of above 4 inheritance is called hybrid inheritance
class c1:
    def m1(self):
        print("class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("class3")
class c4:
    def m1(self):
        print("class4")
class c5:
    def m2(self):
        print("class5")
class c6:
    def m3(self):
        print("class6")


#ploymorphism in builtin functions
#len()-->which is used to find the length of list,tuple,tc
#index()
#max()
#min()
#count()
#pop()
#and more...
    
#ploymorphism in operators
#+
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
def f1(*args):
l1=[1,2,3,4]
print(l1*10)















        








