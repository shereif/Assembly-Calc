# Shereif Saleh
# calc.py
# Rutgers University Computer Architecture

"""

This program's objective is to create a 32-bit calculator
without using built-in's. This program is to be run in the cmd-line.
It is able to compute Hexidecimal,Octal,Decimal,Binary and preform
arithmatic operations. This program features the ability to compute
negative numbers.

"""
import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]


def binary_to_decimal(number):
    a = 0
    count = 0
    for i in number[::-1]:
        if i == ' ':
            return "ERROR malformed binary1 has space"
        elif i.isalpha() == True:
            return "ERROR malformed binary2 is alpha"
        elif i != '0' and i != '1':
            return "ERROR malformed binary not 0 or 1"
        else:
            a += int(i)*(2**count)
            count +=1
    return a

def decimal_to_decimal(number):
    hold = str(number)
    for i in hold:
        if i == ' ':
            return "ERROR malformed decimal has space"
        elif i.isalpha() == True:
            return "ERROR malformed decimal is alpha"

    return int(number)

def decimal_to_binary(number):
    hold = 0
    L= [ ]

    while number != 0:
        hold = int(number) % 2
        number = int(number)//2
        L.append(hold)
    L.reverse()
    change = "".join(str(x) for x in L)
    return int(change)

def octal_to_decimal(number):
    a = 0
    count = 0
    for i in number[::-1]:
        if int(i) >7:
            return "ERROR can not have a number greater than 7 in your octal"
        else:
            a += int(i)*(8**count)
        count+=1
    return a

def decimal_to_octal(number):
    hold = 0
    L = [ ]
    while number != 0:
        hold = int(number) % 8
        number = int(number)//8
        L.append(hold)
    L.reverse()
    change = "".join(str(x) for x in L)
    return int(change)

def equalDec(number):
    numbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(len(numbers)):
        if number == numbers[i]:
            return i

def hex_to_decimal(number):
    count = 0
    a = 0
    s = ''
    for i in number[::-1]:
        if i == '0':
            a+= int(0)*(16**count)
            count+=1
        elif i == '1':
            a+= int(i)*(16**count)
            count+=1
        elif i == '2':
            a+= int(i)*(16**count)
            count+=1
        elif i == '3':
            a+= int(i)*(16**count)
            count+=1
        elif i == '4':
            a+= int(i)*(16**count)
            count+=1
        elif i == '5':
            a+= int(i)*(16**count)
            count+=1
        elif i == '6':
            a+= int(i)*(16**count)
            count+=1
        elif i == '7':
            a+= int(i)*(16**count)
            count+=1
        elif i == '8':
            a+= int(i)*(16**count)
            count+=1
        elif i == '9':
            a+= int(i)*(16**count)
            count+=1
        elif i == 'A' or i == 'a':
            a+= int(10)*(16**count)
            count+=1
        elif i == 'B' or i == 'B':
            a+= int(11)*(16**count)
            count+=1
        elif i == 'C' or i == 'c':
            a+= int(12)*(16**count)
            count+=1
        elif i == 'D' or i == 'd':
            a+= int(13)*(16**count)
            count+=1
        elif i == 'E' or i == 'e':
            a+= int(14)*(16**count)
            count+=1
        elif i == 'F' or i == 'f':
            a+= int(15)*(16**count)
            count+=1
        else:
            return "ERROR not a possible hex"
    return a

def decimal_to_hex(number):
    B = ''
    L = []
    while (number != 0):

        B = int(number) % 16
        number = int(number)//16
        if B == 10:
            L.append('A')
        elif B == 11:
            L.append('B')
        elif B == 12:
            L.append('C')
        elif B == 13:
            L.append('D')
        elif B == 14:
            L.append('E')
        elif B == 15:
            L.append('F')
        elif B == 0:
            L.append(B)
        elif B == 1:
            L.append(B)
        elif B == 2:
            L.append(B)
        elif B == 3:
            L.append(B)
        elif B == 4:
            L.append(B)
        elif B == 5:
            L.append(B)
        elif B == 6:
            L.append(B)
        elif B == 7:
            L.append(B)
        elif B == 8:
            L.append(B)
        elif B == 9:
            L.append(B)

    L.reverse()
    change = "".join(str(x) for x in L)
    converter = str(change)
    return converter

def calc(op, num1, num2, out):
    Operations = ['+','-','*']                #Possible operations
    Types = ['d','b','o','x','D','B','O','X'] #Possible datatypes
    Negative = 0
    Negative = False
    value1 = 0
    value2 = 0
    if op in Operations:
        try:
            if op == '+':   #Looks like we are adding
                if num1[0] in Types and num1[0] == 'd' or num1[0] == 'D':
                    value1 = decimal_to_decimal(num1[1:])
                elif num1[0] == '-' and num1[1] == 'd' or num1[1] == 'D':
                    #Negative calculations
                    Negative == True
                    negsign = '-'
                    hold = '-'+ num1[2:]
                   # print(hold)
                    value1 = decimal_to_decimal(hold)
                elif num1[0] in Types and num1[0] == 'o' or num1[0] == 'O':
                    value1 = octal_to_decimal(num1[1:])

                elif num1[0] in Types and num1[0] == 'x' or num1[0] == 'X':
                    value1 = hex_to_decimal(num1[1:])

                elif num1[0] in Types and num1[0] == 'b' or num1[0] == 'B':
                    value1 = binary_to_decimal(num1[1:])
                else:
                    return "ERROR not a valid num1 positive"

                #***************Checking for num2 ***************

                if num2[0] in Types and num2[0] == 'd' or num2[0] == 'D':
                    value2 = decimal_to_decimal(num2[1:])
                elif num2[0] == '-' and num2[1] == 'd' or num2[1] == 'D':
                    #Negative calculations
                    Negative == True
                    negsign = '-'
                    hold = '-'+ num2[2:]
                    value2 = decimal_to_decimal(hold)
                    total = (value1 + value2)
                elif num2[0] in Types and num2[0] == 'o' or num2[0] == 'O':
                    value2 = octal_to_decimal(num2[1:])
                elif num2[0] in Types and num2[0] == 'x' or num2[0] == 'x':
                    value2 = hex_to_decimal(num2[1:])
                elif num2[0] in Types and num2[0] == 'b' or num2[0] == 'B':
                    value2 = binary_to_decimal(num2[1:])
                else:
                    return "ERROR not a valid num2 positive"

                checkingForErrors1 = str(value1)
                checkingForErrors2 = str(value2)
                if checkingForErrors1[0] == 'E':
                    print("Value1's error :")
                    print(checkingForErrors1)
                    print("\n")
                if checkingForErrors2[0] == 'E':
                    print("Value2's error : ")
                    print(checkingForErrors2)

                total = value1+value2

                #Outputting!
                convertedTotal = str(total)
                if out in Types and out == 'd' or out == 'D':
                    sign = 'd' + str(convertedTotal)
                    return sign
                if out in Types and out == 'o' or out == 'O':
                    if convertedTotal[0] == '-':
                        return "ERROR you can not have a negative octal output"
                    else:
                        thomas = convertedTotal
                        thomas = decimal_to_octal(convertedTotal)#WORKS
                        sign = 'o' + str(thomas)
                        return sign
                if out in Types and out == 'x' or out == 'X':
                    if convertedTotal[0] == '-':
                        return "ERROR you can not have a negative hex output"
                    else:
                        thomas = convertedTotal
                        thomas = decimal_to_hex(convertedTotal)#WORKS
                        sign = 'x' + str(thomas)
                        return sign
                if out in Types and out == 'b' or out == 'B':
                    if convertedTotal[0] == '-':
                        return "ERROR you can not have a negative binary output"
                    else:

                        thomas = convertedTotal
                        thomas = decimal_to_binary(convertedTotal)#WORKS
                        sign = 'b' + str(thomas)
                        return sign
                if out not in Types:
                    return "ERROR not a possible output"


            if op == '-':   #Looks like we are subtracting
                if num1[0] in Types and num1[0] == 'd' or num1[0] == 'D':
                    value1 = decimal_to_decimal(num1[1:])
                elif num1[0] == '-' and num1[1] == 'd' or num1[1] == 'D':
                    hold = '-'+ num1[2:]
                    value1 = decimal_to_decimal(hold)

                elif num1[0] in Types and num1[0] == 'o' or num1[0] == 'O':
                    value1 = octal_to_decimal(num1[1:])
                elif num1[0] in Types and num1[0] == 'x' or num1[0] == 'X':
                    value1 = hex_to_decimal(num1[1:])
                elif num1[0] in Types and num1[0] == 'b' or num1[0] == 'B':
                    value1 = binary_to_decimal(num1[1:])
                else:
                    return "ERROR not a valid num1 sub"

                #***************Checking for num2 ***************

                if num2[0] in Types and num2[0] == 'd' or num2[0] == 'D':
                    value2 = decimal_to_decimal(num2[1:])
                elif num2[0] == '-' and num2[1] == 'd' or num2[1] == 'D':
                    Negative == True
                    negsign = '-'
                    hold = '-'+ num2[2:]
                    value2 = decimal_to_decimal(hold)
                    total = (value1 - value2)
                elif num2[0] in Types and num2[0] == 'o' or num2[0] == 'O':
                    value2 = octal_to_decimal(num2[1:])
                elif num2[0] in Types and num2[0] == 'x':
                    #hold = int(num2[1:])
                    value2 = hex_to_decimal(num2[1:])
                elif num2[0] in Types and num2[0] == 'b' or num2[0] == 'B':
                    value2 = binary_to_decimal(num2[1:])
                else:
                    return "ERROR not a valid num2 sub"

                #Shows you your errors
                checkingForErrors1 = str(value1)
                checkingForErrors2 = str(value2)
                if checkingForErrors1[0] == 'E':
                    print("Value1's error :")
                    print(checkingForErrors1)
                    print("\n")
                if checkingForErrors2[0] == 'E':
                    print("Value2's error : ")
                    print(checkingForErrors2)
                total = (value1 - value2)

                #Outputting!
                convertedTotal = str(total)
                #print("hit")
                if out in Types and out == 'd' or out == 'D':
                    if convertedTotal[0] == '-':
                        #print("I aM HIT LOL")
                        a = 'd' + convertedTotal
                        return a
                    else:
                        out == 'd'
                        sign = 'd' + str(convertedTotal)
                        return sign
                    return convertedtotal
                if out in Types and out == 'o' or out == 'O':
                    if convertedTotal[0] == '-':
                        return "ERROR you can not have a negative octal output"
                    else:
                        #print("hit at sub o")
                        thomas = convertedTotal
                        thomas = decimal_to_octal(convertedTotal)
                        sign = 'o' + str(thomas)
                        return sign
                if out in Types and out == 'x' or out == 'X':
                    if convertedTotal[0] == '-':
                        return "ERROR you can not have a negative hex output"
                    else:
                        #print("hit at sub x")
                        thomas = convertedTotal
                        thomas = decimal_to_hex(convertedTotal)
                        sign = 'x' + str(thomas)
                        return sign
                if out in Types and out == 'b' or out == 'B':
                    if convertedTotal[0] == '-':
                        return "ERROR you can not have a negative binary output"
                    else:
                       # print("hit at sub b")
                        thomas = convertedTotal
                        thomas = decimal_to_binary(convertedTotal)
                        sign = 'b' + str(thomas)
                        return sign
                if out not in Types:
                    return "ERROR not a possible output"

        except:
            print("********************************************************************\n")
            print("In order to run this program follow these examples")
            print("python calc.py + 'd100' 'd100' 'b'")
            print("python calc.py + 'xfFf' '-o4234523' 'd'\n")
            print("Little things to know : \n")
            print("1.Do not put letters in your inputs if its not a hex")
            print("2.Double check your inputs")
            print("3.You can not have a negative Octal, Hex, or Binary\n")
            print("I am just going to print None to signify ERROR for this case\n")

            return


if __name__ == "__main__":
    x = calc(a,b,c,d)
    print(x)
