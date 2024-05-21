a=int(input("Enter a number: "))
b=a
d=0
while a:
    r=a%10
    d=d+(r**3)
    a=a//10
if d==b:
    print("The number is an armstrong")
else:
    print("The number not an armstrong")
