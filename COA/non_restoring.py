from lab1 import addsub

def left_shift(bin_num):
    bin_num = bin_num[1:] + "0" 
    return bin_num

def non_restoring_division(dividend,divisor):
    n_bits =  len(dividend)
    register = "".zfill(n_bits + 1)
    divisor = divisor.zfill(n_bits + 1)
    for _ in range(n_bits):
        shift = left_shift(register+dividend)
        register = shift[:(n_bits + 1)]
        dividend = shift[(n_bits + 1):]
        if register[0] == "1":
            register = addsub(register, divisor,0)[1:]
            if register[0] == "0":
                dividend =dividend[:-1] + "1"
             
        else:
            register = addsub(register, divisor,1)[1:]
            if register[0] == "0":
                    dividend =dividend[:-1] + "0"
            
    if register[0] == "1":
        register = addsub(register,divisor,0)[1:]  
              
    return register,dividend

if __name__ == "__main__":
    num1 = input("Enter dividend: ")
    num2=input("Enter divisor: ")
    remainder,quotient = non_restoring_division(num1,num2)
    print("quotient:",quotient)
    print("remainder:",remainder)
    