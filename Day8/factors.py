def Factors(num):
    num = abs(num)
    #Creates an emty list
    l = []
    for i in range (1,num+1):
        if num % i == 0:
            l.append(i)
    return l
def CountToN(num):
    # Num Will be assigned the absolute value of itself
    num = abs(num)
    for i in range(1,num+1):
        print i
n = raw_input ("Enter an in integer:\n")
n = int(n)


CountToN(n)
print Factors(n)
