def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a number : "))
if(n<0):
    print("Factorial for negative number does not exist.")
elif(n==0):
    print("The factorial of 0 is 1.")
else:
    print("The factorial of",n,"is",factorial(n))