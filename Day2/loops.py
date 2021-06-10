# i = 1
# while(i<10):
#     print(i)
#     i+=1  # i = i + 1


# i have to take numbers 10 times and output the result whether number is odd or even

# counter = 0
# while(counter<5):
#     n = int(input("Enter the number : "))
#     if n%2==0:
#         print("it is even")
#     else: 
#         print("it is odd")
#     counter+=1


# counter=0
# n=-1
# while(counter<100):
#     n+=2
#     print(n)
#     counter+=1


# counter = 0
# odd_num = 1
# while(counter<100):
#     print(odd_num)
#     odd_num += 2 
#     counter+=1

# i = 1
# n = int(input())
# while(i<=n):
#     print('*'*i)
#     i+=1


# i = 1
# while(i<=100):
#     print(i)
#     if i%3==0 and i%5==0:
#         break
#     i+=1


# i = 1
# while(i<=100):
#     i+=1
#     if i%2==0 and i%3==0:
#         continue
#     print(i)
    

# find whether the given number is prime or not

# isprime = True
# n = int(input())
# i=2
# while(i<n):
#     if n%i==0:
#         isprime = False
#         break
#     i+=1
# if isprime:
#     print("it is prime")
# else:
#     print("it is not prime")

# Q .print the pattern

# 1
# 12
# 123
# 1234
# 12345

# n = int(input())
# ln = 1 # line number
# while(ln<=n):
#     i = 1
#     while(i<=ln):
#         print(i, end="")
#         i+=1
#     print("")
#     ln+=1



# for i in range(50, 100+1, 2):
#     print(i)

# for i in range(1, 100, 2):
#     print(i)

# for i in range(1, 100):
#     if i%2 !=0:
#         print(i)

# lower = 2
# upper = 100

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)



# isprime = True
# n = int(input())
# for i in range(2, n):
#     if n%i==0:
#         isprime = False
#         break
#     i+=1
# if isprime:
#     print("it is prime")
# else:
#     print("it is not prime")

# m = int(input())
# for j in range(2, m+1):
#     isprime = True
#     n = j
#     for i in range(2, n):
#         if n%i==0:
#             isprime = False
#             break
#         i+=1
#     if isprime:
#         print(n, "it is prime")
#     else:
#         print(n, "it is not prime")


# n = int(input("Enter the number of rows"))  
 
# for i in range(0, n):  
#     for j in range(0, i + 1):  
#         print("* ", end="")       
#     print()
