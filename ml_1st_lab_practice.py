# #git add .
# #git commit -m "msg"
# #git push


# print("hello wordl")

# #varibales 
# name="umar"
# age=20
# mark=99
# gpa = float(3.52)

# print(name)
# print(age)
# print(mark)
# print(gpa)

# # Arithmetic operator
# add = 5+5
# sub = 50-30
# mul = 5*8
# div = 100/2
# floor_div = 15//2
# power = 2**3
# remainder = 10%3

# print("add :", add)
# print("sub :", sub)
# print("mul :", mul)
# print("div:", div)
# print(floor_div)
# print(power)
# print(remainder)

# #Comparison operators
# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# #Logical Operators 
# print("logical operators")
# salary = 1000

# print(salary>=1000 and salary<=2000 )
# print(salary<1000 or salary>2000)

# x=True
# print(not x)

# #Conditional Statements

# x = 50
# if x<=50:
#     print("number is less and equal")
# else:
#     print("number is greater")

# # if else with input
# age = int(input("enter your age "))

# if age>=18 and age<=50:
#     print("you are adult ")
# elif age>50:
#     print("you are old")
# else:
#     print("your are child")

# #nested if
# has_id = True

# if age>=18:
#     if has_id:
#         print("allow to vist")
#     else:
#         print("not allowed")
# else:
#     print("you are not eligible")

# #number indentifyer
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# #loops
# for i in range(3):
#    print(i)

# # range types maans controlling the stop and start 
# for i in range(2,10):
#     print(i)

# #range(start, stop, step)
# for i in range(5,40,5):
#     print(i)

# # WHILE LOOP
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

#user define function
def greet():
    print("Hello Umar")

greet()

def greetuser(name):
    print("Hello ",name)

greetuser("ali")

def add(a,b):
    print(a+b)

add(1,2)

def num(*args):
    print(sum(args))

num(10,20,30)

def sumOfAll(*args):
    return sum(args)

print(sumOfAll(1,2,3,4,5,6,7,8,9,))




    






