d={}
def add():
    while True:
        rn=int(input("Enter the roll number: "))
        na=input("Enter the name: ")
        d[rn]=na
        ch=input("Add another data?(Y/N): ")
        if ch=="N":
            break
def display():
    print("The dictionary is")
    print(d)
def delete():
    rn=int(input("Enter the roll number to delete:"))
    del d[rn]
    print("The dictionary after removing the data")
    print(d)
def modify():
    rn=int(input("Enter the roll number to modify:"))
    d[rn]=input("Enter new name: ")
    print("The dictionary after modifying\n",d)
while True:
    print("1.Add data\n2.Display\n3.Delete\n4.Modify\n5.Quit")
    a=int(input("Enter the choice: "))
    if a==1:
        add()
    if a==2:
        display()
    if a==3:
        delete()
    if a==4:
        modify()
    if a==5:
        break
    else:
        print("Enter a valid number: ")
      
