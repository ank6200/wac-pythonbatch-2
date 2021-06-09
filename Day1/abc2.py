# print("hello world", end="\n\n")
# this line is showing simple print way
# print("hello world", "it's me", sep = ",", end="")

# print("hello")
# print("world")

# x = input()
# print("value of x is", x)

# data types

# int integer 4, 5, -5
# float decimal point numbers 5.6, 6.4, 8.8
# str strings "my name is ", "Neeraj ", "8998*((*", 'sdfs', '''jkjhjkdsf'''
# bool true false


# "kasdfk"
# 'jsdfkjsdl'

# 'he said, "she is mad"'

# a = '''he is a boy.
# he is 8 year old.'''
# print(a)

# a = 5
# b = 6

# c = a // b
# c = b % a
# print(c)

# type casting
# a = input()
# b = float(a) # string -> int
# print(type(b))


# print(5%6)


principle = int(input("Please enter principle amount : "))
rate = float(input("Please enter interest rate : "))
time = int(input("please enter time for loan : "))

si = principle * rate * time / 100

print(principle, rate, time, "SI for the given is :", si, sep='\n')
print()


# n = int(input())

# if(n%2==0):
#     print('the number is even')
# else:
#     print("the number is odd")


# length = int(input("enter length : "))
# breadth = int(input("enter breadth : "))

# if length == breadth :
#     print("it is a square")
# else:
#     print("it is a rectangle")


# next question :
# a company decided to give bonus of 5% to employee if his year of service is 
# more than 5 year. ask user for their salary and year of experience and print 
# the net bonus amount


# salary = int(input("enter your salary : "))
# time = int(input("enter your working period : "))

# if time>5:
#     bonus = (5/100)*salary
#     print(bonus)
# else:
#     print("no bonus for you")

# next question : take two integer and print greatest among them

# a = int(input())
# b = int(input())

# if(a>b):
#     print("a is greater")
# else:
#     print("b is greater")


# a, b, c greatest among them

# a = int(input())
# b = int(input())
# c = int(input())

# if a>b:
#     if(a>c):
#         print("a is greatest")
#     else:
#         print("c is greatest")
# elif(b>a):
#     if(b>c):
#         print("b is greatest")
#     else:
#         print("c is greatest")
# else:
#     if(b>c):
#         print("a and b is greatest")
#     else:
#         print("c is greatest")
    

# and or

# a = int(input())
# b = int(input())
# c = int(input())


# if(a>b and a>c):
#     print("a is greatest")
# elif(b>a and b>c):
#     print("b is greatest")
# else:
#     print("c is greatest")


# i = 1
# while(i<=1000):
#     print(2*i)
#     i=i+1 # ---> increment condition


# kdsflkndsa
# sjdnfkasdf
# jsdfkjasd


'''single line comment

multi line comment'''

# a, b, c

# line = input().split()

# a = line[0]
# b = line[1]
# c = line[2]

# print("hello", "world", sep="\n")