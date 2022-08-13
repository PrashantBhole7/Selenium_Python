# n! = n * (n-1) * (n-2) * (n-3) .... * 1
num = int(input("Enter the number : "))
fact_value = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, num+1):
        fact_value = fact_value * i
    print("Factorial of", num, "is : ", fact_value)

