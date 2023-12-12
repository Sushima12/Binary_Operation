#Half Adder by Poh Boon Siong
#A Half Adder Program written in Python

#Truth Table For Half Adder
# A + B = Carry|Sum
# 0 + 0 = 00
# 0 + 1 = 01
# 1 + 0 = 01
# 1 + 1 = 10

#Carry = A and B
#Sum = A Xor B
def main():
    while(True):
        print('\n=========================================================================================\n')
        print('Binary Addition of 2 1-bit binary numbers')
        A = input('Enter a 1-bit binary number for A (1 or 0): ')
        B = input('Enter another 1-bit binary number for B (1 or 0): ')
        
        if isBinary(A) == 0:
            continue
        elif isBinary(B) == 0:
            continue
        else:
            if is_n_Bits(A, 1) == 0 or is_n_Bits(B, 1) == 0: 
                continue
            else: 
                #Run the Half Adder Function
                result = Half_Adder(A,B)
                C = result[0]
                S = result[1]
                print('Binary addition of ' + A + ' and ' + B + ' is ' + str(C) + str(S))
             
def Half_Adder(a, b):
    #Half Adder Truth Table
    #Can be simplified
    result = []
    Carry = int(a) * int(b)
    Sum = int(a) ^ int(b)
    result = [Carry, Sum]
    return result

def isBinary(binary):
    #Check if the value is a binary number
    #Checks if binary is 1 bit
    #Method: Multiply every number binary
    #If the result of the multiplication is 1 or 0, then it is binary.
    #Otherwise it is not binary
    mResult = 0
    binary_list = list(binary)
    for i in binary_list:
        if i == '1' or i == '0':
            continue
        else:
            print('ERROR: ' + binary + ' is not a binary number, please try again')
            return 0
    return 1    

def is_n_Bits(binary, expected_bits):
    #Check number of bits and return true or false
    if len(binary) != expected_bits:
        print('ERROR: ' + binary + ' has incorrect number of bits, please try again (Expected nummber of bits: ' + str(expected_bits) + ')')
        return 0
    else: 
        return 1
        
if __name__=="__main__":
    main()


