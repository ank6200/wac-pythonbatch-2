# def isodd(n):
#     if n%2==0:
#         return False
#     return True

# print(isodd(5))



# def factorial(n=2):
#     result = 1
#     for i in range(1, n+1):
#         result*=i
#     return result

# print(factorial(5))

# def area(breadth, length=8):
#     return length*breadth

# print(area(8, 9))



# def prime(n):
#     isprime = True
#     for i in range(2, n):
#         if n%i==0:
#             isprime = False
#             break
#         i+=1
#     return isprime

# n = int(input())
# for i in range(2, n+1):
#     if prime(i):
#         print("it is prime", i)
#     else:
#         print("it is not prime", i)



# student1 = "neeraj"
# student2 = "aadhya"
# student3 = "ankit"

# student_list = ['neeraj', 'aadhya', 'ankit']
# print(student_list[0])


# lis = ['neeraj', 8, [19, 8, ['ankit', 9], 7]]
# print(lis[2][2][1])

# lis = [4,5,6,8]
# print(lis)
# lis.append(89)
# lis[1]=54
# del lis[1]
# print(lis)


# list slicing

lis = [1,2,3,4,5,6,7,8,9]
# print(lis[2:8:2])
print(min(lis))

print(abs(-8))