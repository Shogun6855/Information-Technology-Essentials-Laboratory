f=open('trial.txt','r')
f.read
c=0
for i in f:
    for j in i.split():
        if j[-1]=="e":
            c=c+1
print("No of words ending with 'e': ", c)
f.close()
