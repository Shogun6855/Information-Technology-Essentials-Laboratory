A = []
B = []
C = []
p = int(input("Enter no of rows of matrix A: "))
q = int(input("Enter no of cols of matrix A: "))
r = int(input("Enter no of rows of matrix B: "))
s = int(input("Enter no of cols of matrix B: "))
if(q!=r):
    print("Matrix multiplication not possible: ")
else:
    for i in range(p):
        temp=[]
        for j in range(q):
            print("A[%d][%d]"%(i, j), end=": ")
            temp1 = int(input())
            temp.append(temp1)
        A.append(temp)
    for i in range(r):
        temp=[]
        for j in range(s):
            print("B[%d][%d]"%(i, j), end=": ")
            temp1 = int(input())
            temp.append(temp1)
        B.append(temp)
    print("Matrix C:")
    for i in range(p):
        temp = []
        for j in range(s):
            sum = 0
            for k in range(q):
                sum= sum + A[i][k]*B[k][j]
            temp.append(sum)
        C.append(temp)
    for i in range(p):
        print("[", end="\t")
        for j in range(s):
            print("%d"%(C[i][j]), end="\t")
        print("]")