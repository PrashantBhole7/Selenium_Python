# Natural number > 1 because prime numbers are 2,3,5,7,11
# Number is prime if it has factures 1 and itself
# e.g. 19 it is prime as it has factures 1 and 19
# e.g 28 has factures 1, 2 , 4, 7, 14, 28, so it is not a prime number

num = int(input("Enter the number to be checked: "))
count = 0
if num > 1:
    for i in range(1, num+1):
        if (num%i) == 0:
            count = count + 1
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not a prime")
else:
    print("Number is not a prime")
