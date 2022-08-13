# Swapping
num1 = 7
num2 = 8
temp = num1
num1 = num2
num2 = temp

num1 , num2 = num2, num1

# prime number:
2,3, 5, 7, 11
num = int(input())
count = 0
if num > 1:
    for i in range(1,num+1):
        if num%i == 0:
            count = count + 1
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not prime")
else:
    print("Number is not prime")

# Factoral of given number_by_iterative

num = 5
fact_value = 1
for i in range(1,num+1):
    fact_value = fact_value * i
    i = i - 1
print(fact_value)

# fibonacci_numbers:
a = 0, 1,1,2,3,5,8,13
n1 = 0
n2 = 1
print(n1)
print(n2)

# factorial of given number by recurrcive approach
num = int(input("Enter the number which you want to find factorial"))

def factorial(n):
    if n == 0 or n== 1:
        return 1
    elif n < 0:
        return "factorial does not exist"
    else:
        return n * factorial(n-1)
fact = factorial(num)
print("Factorial of given number is :", fact)
for i in range(2, 10):
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum

# Swap any element of the list
myList = [1, 4, 23 ,32, 34]  # index starts from 0
print("List before swapping: ", myList)
