# n! = n * (n-1)!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "does not exist"
    else:
        return n * factorial(n - 1)


n = int(input("Enter the number which factorial you want to find : "))
fact = factorial(n)
print("Factorial of the ", n, "is", fact)
