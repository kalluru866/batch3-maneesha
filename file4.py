#day:4
'''
for row in range(8):
    for col in range(8):
        print("*",end=" ")
    print()

#
for row in range(5):
    for col in range(5):
        sum= sum+1
        print(sum, end=" ")
    print()

#to print stars in right angled triangle
    
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

for row in range(6,0,-1):
    for col in range(0,row):
        print("*",end=" ")
    print()
           
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

for row in range(5):
    for col in range(5):
        if ((row==0 and col==3) or (row ==1 and (col>=2 and col<4) or
                                  (row==2 and (col>=1 and col<=5)))):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




for row in range(5):
    for col in range(5):
        if ((row==0 and col==1) or (row ==2 and (col>=3 and col<5) or
                                  (row==4 and (col>=5 and col<=6)))):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# ! datatypes
#primary
#number int,float complex
#string
#boolean
#none

#collection
#list
#tuple
#set
#dictionary


# ?list

#1.) if the collection of elements are sorounded by square brakets,it id considered
# to be list
# eg:1
  #l1=[4,7,9,9.89,"hello",[8,9,0]]


#characteristics of list
#1.)list have to be sorrounded by[]
#2.)it is mutable (the elements in the list are changable)
#3.)every element inside list is indexed
#4.)the elements inside list will be ordered formate
#5.)it can hold duplo=icate values
#6.)its heterogenous

#to access the element in list
l1 = [1,4,1,7.89.7,7,5,"p","I"]
print(l1)

#indexing
in the collection datatyoes like list,tuple,string,the elements will be alloted
with pre-defined unique value called index value
we have 2 types if indexing
1positive indexing--> starts with 0 from left hand side
2negative indexing-->starts with -1 from right hand side

#positive indexing
l1 = [1,4,1,7.89.7,7,5,"p","I"]
print(lst1[0])
print(lst1[4])
print(lst1[20])-->error

#negative indexing
l1 = [1,4,1,7.89.7,7,5,"p","I"]
print(lst1[-1])
print(lst[-5])

#?slicing
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "I"]
#lst1[start index:end index]
print(lst1[0: 4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])
print(lst1[0:7:1]

print(lst1[-4:-1])
print(lst1[-1:-4])
print(lst1[-7:-1])
print(lst1[-7:-1:2])
'''
#!to insert ot add element inside list
append()
l1 = [9, 8, 0, 6]
l1.append("car")
print(l1)



































    
