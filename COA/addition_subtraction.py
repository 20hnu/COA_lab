
def addsub(x,y,cin):
    a=x[::-1]
    b=y[::-1]
    sumval=[]
    for i in range(len(a)+1):
        if(i==0):    
            ci=cin
        else:    
            ci=carryGenerator(a,b,i-1,cin)
        
        if(i==len(a)):
            if(int(ci)!=cin):
                sumval.append(str(binadd(0, 0, int(ci))))
        else:
            sumval.append(str(binadd(int(a[i]), int(b[i])^cin, int(ci))))
        
    return "".join(sumval[::-1])


def binadd(a,b,c):
    return a^b^c

def carryGenerator(x,y,i,cin):
    gen=generate(x[i], int(y[i])^cin) 
    prop=propagate(x[i], int(y[i])^cin) * (cin if i == 0 else int(carryGenerator(x, y, i - 1, cin)))
    return(str(binadd(gen,prop,0)))

    

def generate(xi,yi):
    return int(xi)*int(yi)

def propagate(xi,yi):
    return binadd(int(xi),int(yi),0)


if __name__ == "__main__":
    while(True):
        choice=input("Do you want to add or subtract: ")
        if(choice.lower()=="add"):
                cin=0
                break
        elif(choice.lower()=="sub"):
                cin=1
                break
        else:
                print("Invalid choice. Try again !!!")

    num1 = input("Enter any binary numbers: ")
    num2=input("Enter next binary number: ")

    if(len(num1)>len(num2)):
        num2=("0"*(len(num1)-len(num2)))+num2
    elif(len(num2)>len(num1)):
        num1=("0"*(len(num2)-len(num1)))+num1
    
    sumval=addsub(num1,num2,cin)
    print(sumval)
