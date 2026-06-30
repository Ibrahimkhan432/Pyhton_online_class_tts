# print("hello")

# install python
# python or python3 --version

# functions
# builten formula - uncontrolled 
# (Date - months(specific))
# pre defined code which is reusable
# controlled code
# advantage - reuse , maintain , controlled code ,readable

# def my_function():
#     print("hello function")

# my_function()
# my_function()
# my_function()

# def myFirstFunction():  #camelcase (drawmadory)
#  a = 4
# def calculate():
#     sum = a + 5
#     print(sum)

# calculate()

#  a = 6
# def calculate():
#     sum = a + 5
#     print(sum)
# calculate()

# def calculation(sum): # sum -parameter
#  return sum + 5

# print(calculation(7)) # 7 - argument

# def my_name(name):
#     print(name)

# my_name("abc") 

# def sum(number1,number2=0): #default parameter
#     print(number1 + number2)

# # sum(2,3)  
# sum(2)
 
# def sum(a,b):
#  print(a + b)
# sum(2,3)    

# print(sum())

# def message():
#   return ("hello message")
# newmessage = message()  
# print(newmessage)

# def multiply(a,b):
#     print( a * b)

# multiply(3,4)    


# def myfullname(firstname,lastname):
#     print("my first name is" firstname, " my " lastname)

# myfullname("ibrahim", "khan")

# git - software


#  topic - data and interactivity

# -- data

# sum = 3 # assign
# sum == 3 # equal
# "3" == 3 # equal with type

# string - "ibrahim" (a to z)
# integer - 2323 (0 t 9)
# float - 2342.34 (decimal) (0.1 to 9.9)
# boolean - true

# name = "ibrahim"
# print(type(name))

# age = 20
# print(type(age))

# height = 5.9
# print(type(height))

# isActive = bool()
# print(type(isActive))

# num1 = 3   #int
# num2 = "4" #float 
# # sum = 3 + 5.5 # temporary add
# sum = num1 - num2  # type coercion
# print(sum)

# -- interactivity 
# input()

# fname = input("enter your fname")
# print("your fname is", fname)
# lname = input("enter your lname")
# print("your lname is", lname)
# print("your fullname is", fname , lname)

# num1 = int(input("enter first number")) # "5"
# num2 = int(input("enter second number")) # "6"
# sum = num1 + num2
# # sum = "5 "+ "6" = 56 (concatenation)
# print("sum is =",sum)

# assignment 
# 1. input for age which should be in integer
# 2. multiply 2 numbers using input (int)
# 3. fullname (string)


 # -- list
# std1 = "asad"
# std2 = "kashan"
# std3 = "saif"
# std4 = "bilal"

#list rules
#1.[]
#2. , [,] -comma seperated
# index - start from zero (0)
#reserve keywords - int - float - str - bool
studentList = ["asad", "kashan","saif","saif","bilal"]
#  index          0        1        2     3        4
#.  index 4(start from zero)
#.  length 5 (total elements)
#print(type(studentList))
print(studentList)

# stdlist = ["ali","asad","bilal"]
# print(len(stdlist))
# print(stdlist[0])
# print(stdlist[1])
# print(stdlist[2])

# print(stdlist[-2])

stddata = ["ali",20,4.5,True]
# print(stddata)
# list cannot change order
# list can modify(add data, remove data)
#stddata[4] = "bilal" #js
# stddata.append("bilal")
# stddata.insert(2,"asad")
# print(stddata)

# list1 = ["a","e","c"]
# list2 = ["d","e","f"]
# # combined
# list1.extend(list2)
# print(list1)

# list3= [ "a","b","c"]
# list3.remove("b")
# print(list3)

# js - pop and push
# pop(remove from last)
# push(add in last)

list3= ["a","b","c"]
#list3.pop(1) # 1 is an index number
# list3.pop() - method
#del - keyword
# del list3[0]
list3.clear()
print(list3)

assignment 
use all list methods and keywords 
create an list and remove center value
create an list and combine with another list 
remove the list elements using index number not an element