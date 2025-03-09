a=int(input("\nEnter first number : "))
b=int(input("\nEnter second number : "))
c=int(input("\nEnter third number : "))

if(a>b and a>c):
    print("\nFrom the above entered numbers,",a,"is the highest.")
elif(b>a and b>c):
    print("\nFrom the above entered numbers,",b,"is the highest.")
else:
    print("\nFrom the above entered numbers,",c,"is the highest.")