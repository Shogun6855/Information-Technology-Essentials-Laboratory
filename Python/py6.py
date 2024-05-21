f=open('result.txt','r')
a=f.readlines()
def result_analysis():
    Total=0
    Pass=0
    Fail=0
    for i in a:
        Total+=1
        for j in i.split():
            if j=='pass':
                Pass+=1
            if j=='fail':
                Fail+=1
    print("Total number of students: ",Total)
    print("No of students passed: ",Pass)
    print("No of students failed: ",Fail)
def disp_student(string):
    for i in a:
        for j in i.split():
            if j==string:
                print(i)
result_analysis()
string = input("Enter the name: ")
disp_student(string)

