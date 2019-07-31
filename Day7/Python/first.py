'''print "Hello World"

name = raw_input("please enter Your name:\n")
time = raw_input("What time is it?\n")
if time > 6 and time < 12:
    print "Hello", name,"It is", time,"In the Morning"
elif time > 12:

    print "Hello", name,"It is", time,"In the Afternoon"'''
num = raw_input("Enter a Number:")
num = int(num)
if type (num) != type (int()):
    print "Not an integer"
elif num < 1 or num > 10:
    print "Number is out of Range"
elif num % 2 == 0:
    if num == 2: 
        print "Your number is prime"
    else:
        print "Your number is not prime"
else:
    print "Enter another number between 1 and 10"

 