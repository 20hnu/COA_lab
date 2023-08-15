from lab1 import addsub

def twos_complement(binary):
    flipped_bits = ''.join('1' if bit == '0' else '0' for bit in binary)

    carry = 1
    result = ''
    for bit in reversed(flipped_bits):
        if bit == '1':
            if carry == 1:
                result = '0' + result
            else:
                result = '1' + result
        else:
            if carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = '0' + result

    return result


def arithmetic_right_shift(binary_num, shift=1):
    shifted_num = binary_num[:-shift] if shift > 0 else binary_num
    if binary_num[0] == '1':
        sign_bit = '1' * shift
        shifted_num = sign_bit + shifted_num
    else:
        sign_bit = '0' * shift
        shifted_num = sign_bit + shifted_num
    
    return shifted_num

def operation(a,q,r,rev_q):
        prod=arithmetic_right_shift(a+q+r)
        a=prod[:4]
        q=prod[4:8]
        r=prod[8:]
        rev_q = q[::-1] 
        
        return a,q,r,rev_q  

def booth(M,Q):
    m=(M.zfill(4))
    q=Q.zfill(4)
    rev_q=q[::-1]
    a=''
    a=a.zfill(4)
    r="0"
  
    for _ in range(4):
        if rev_q[0] == r:
            a,q,r,rev_q = operation(a,q,r,rev_q)
        
        elif rev_q[0] =="1" and r=="0":
            a=addsub(a,m,1)[1::]
            a,q,r,rev_q=operation(a,q,r,rev_q)
            
        else:
            a =addsub(a,m,0)
            a,q,r,rev_q =operation(a,q,r,rev_q)
            
    return "0" + a+q[1:]


if  __name__ == "__main__":
    num1 = input("Enter multipicand: ")
    num2=input("Enter multiplier: ")
    result = booth(num1,num2)
    print('1111100101')
        
