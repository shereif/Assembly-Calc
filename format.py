import sys

a = sys.argv[1]

def formatnegative(number):
    """
    If leading bit is negative this will preform a negative two's complement
    """
    flippedInput = ''
    convertednums = ''
    for i in number[::-1]:
        flippedInput += i
    convertednums = flipper(flippedInput)
    a = 0
    count = 0
    for i in convertednums:
        a += int(i)*(2**count)
        count +=1
    add = a + 1
    changer = str(add)
    return ("-" + changer)

def formatregular(number):
    a = 0
    count = 0
    for i in number[::-1]:
        a += int(i)*(2**count)
        count +=1
    return a

def flipper(number):
    num = ''
    for i in number:
        if i == '1':
            num+= '0'
        elif i == '0':
            num+= '1'
    return num

def formater(number):
    L = ["0","1"]
    if len(number) < 32 or len(number) > 32:
        return "ERROR input either not long enough or too short"
    for i in number:
        if i not in L:
            return "ERROR can not have anything but 0 or 1"
    if number[0] == '1':
        answer = formatnegative(number)
    else:
        answer = formatregular(number)
    return int(answer)



if __name__ == "__main__":
    x = formater(a)
    print(x)

