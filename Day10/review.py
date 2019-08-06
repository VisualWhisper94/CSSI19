#How to create a function Review   
'''Start by typing the keyword
def followed by the name of the 
function and then parentheses 
with a list of commas. Last you 
add a colon after the closed 
parenthesis and indent the next
line for the body of the function'''

def f(x):
    return 2* x + 3

'''The function above us named f.
It takes one parameter which should
be a number. The function returns twice
the parameter plus 3'''

'''Once a function is defined, yoou can use
it by calling it. To call a function, you must
use the function's name followed by parentheses
with the arguments of the function enlosed in them.
Arguments are literals, objects, expressions or return-value
function calls that takes the place the parameters in the function 
definition. The arguments are associated with the parameter in the 
same position as them in''' 

#Function call with a literal
'''print f(2)

#
print f(3 + 4 * 6)

#
print f(f(6))

v = 89
print f(v)

x = 4
y = 10
def p(x , y):
    if x > y:
        return x 
    else:
        return y
x = int(raw_input("Enter your x value:\n"))
y = int(raw_input("Enter your y value:\n"))

print p (x ,y)

def string():
    x = raw_input("Enter a string:\n")
    return x + x
print string()

def plus_p(x,y,z):
    v = x * y * z + 3
    print v
plus_p(1,2,3)'''

#List
'''A list us an ordered collection of objects'''
'''You can access the elements of a list with an inndex'''
''' -n to n -1'''
#creating a list 
'''l = []

k = list ()
j = [1,2,3,4,5,6,7,8,9,10]
print "l =",l
print "k =",k
print "j =",j
# how you empty the list
k.append('a')
k.append('t')
j.append('k')

print"\nThe list after incert"
print "l =",l
print "k =",k
print "j =",j

k.incert('a')
k.incert('t')
j.incert('k')'''

#Loops
#While loop
'''counting to 20'''
i = 1
while i <= 20:
    print i
    i += 1

while i <= 20:
    if i % 2 == 1:
        print i
    i +=1

#v = ""
#while v != "Hello":
   # v = raw_input("Enter a string:")

#For Loop
#traversing sequenses
'''
for i in range (1,11):
    print i

for i in range (1,21):
    print

for i in range (2,21,2):
    print i

for i in range (1,21):
    if i % 2 == 0:
        print i

for i in range (1,21):
    if i % 2 == 1:
        print i

for i in 'This is a string':
    print i
    

h = []
for i in range (20):
    h.append (0)
print h
len(h)
#fibanachi numbers
for i in range (2,20):
    h[i] = h[i-1] + h[i-2]

print how
'''
# dictionary
'''an unordered collection/list of key-value pairs'''
#Creating a dictionary

d = {}
b = dict()
a = {1:2, 2:1, 3:3, 4:5, 5:4} #permunant
c = {12:"John Smith", 89:"Jane Doe"}
print a[1]
print c[89]

#Adding element to a dictionary

c[72] = "Joe Brown"

print call

# Object
'''An instance of a class'''

class Area51:
    def__init__(self,name,):
        self.alien = 0
        self.type = name
    def no_of_alien (self):
        self.alien += 1

# Create objects
t = Area51 ("Naruto Runners") #Create a Person object

print t.name, t.alien


