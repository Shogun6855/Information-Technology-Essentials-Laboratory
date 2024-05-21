lst=[]
while True:
    a=int(input("Enter a number: "))
    lst.append(a)
    ch=input("Add another data?(Y/N): ")
    if (ch=="N")|(ch=="n"):
        break
tup=tuple(lst)
dit={}
for i in tup:
    if i in dit:
        dit[i]+=1
    else:
        dit[i]=1
print(dit)
    
