da=input("Enter a date:")
m=0
s=da.split()
for i in s:
    if s[0]=="January":
        m=1
    if s[0]=="February":
        m=2
    if s[0]=="March":
        m=3
    if s[0]=="April":
        m=4
    if s[0]=="May":
        m=5
    if s[0]=="June":
        m=6
    if s[0]=="July":
        m=7
    if s[0]=="August":
        m=8
    if s[0]=="September":
        m=9
    if s[0]=="October":
        m=10
    if s[0]=="November":
        m=11
    if s[0]=="December":
        m=12
print(("{:02d}".format(m)),"/",s[1],"/",s[2][2:])
