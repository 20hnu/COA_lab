

A='0000'
Q=input("Enter Multiplier: ")
M=input("Enter Multiplicand: ")

Q=Q.zfill(4)
M=M.zfill(4)

def rshift(A,Q):
    B=A+Q
    B=B[:-1]
    B='0'+B
    A=B[:4]
    Q=B[4:]
    return B

def add(A,M):
    x=A[::-1]
    y=M[::-1]
    z=0
    i=0
    res=[]
    while(i<4):
        s=str(int(x[i])^int(y[i])^z)
        res.append(s)
        z=int(x[i])*int(y[i])|int(x[i])*z|int(y[i])*z
        i=i+1
    A = "".join(res[::-1])
    return A

def mul(A,Q,M):
    i=0
    while(i<4):
        if(Q[-1]=='1'):
            A=add(A,M)
        C=rshift(A,Q)
        A=C[:4]
        Q=C[4:]
        i=i+1
    return A+Q

    
r=mul(A,Q,M)
print("The result is: "+r)
