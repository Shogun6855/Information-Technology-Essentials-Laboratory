import math
n = int(input("Enter a number: "))
print("Prime numbers upto ", n)
for i in range(2, n+1):
    for j in range(2, (i//2)+1):
        if math.gcd(i,j)!=1:
            break
    else:
        print(i)

