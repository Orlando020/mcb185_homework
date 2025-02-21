#print(range(1,10,4))



#def triangular(n):
#    total = 0
#    for i in range(1, n+1):
#        total = total + i
#        print(total)
#    return total
    
#tn = triangular(100)
#print(tn)

#alphab = 'a', 'b', 'c'
#for i in alphab:
#    print(i)
    
#for i in range(len(alphab)):
#    print(alphab[i])
    
    
#import random

#for i in range(5):
#    r = random.random()
#    print(r)
    
#for i in range(5):
#    r = random.randint(1,6) #like dice
#    print(r)
    
#for i in range (3):
#    print(i)
    
def factorial(n):
    if n == 0: return 1 #outlier condition
    product = 1
    for i in range(1, n+1):
        product *= i
    return product
    
#print(factorial(5))

#Eulers number = 1+1/n!

def euler_est(n):
    e = 0
    for i in range (n):
        e+= 1/(factorial(i))
        print(e)
    return e
        
#print(euler_est(60))

#IDing prime number

#def is_prime(n):
#    if n <= 1: return 'bad search'
#    for i in range (2,n//2):
#        if n % i == 0: return False
#    return True
#print (is_prime(4)) # more degbugging it says its true
#print (is_prime(4))
#print (is_prime(9))
#print (is_prime(9))
#print (is_prime(17))
#print (is_prime(17))


#Monty python shotgun pi method
#import random
#intally = 0
#outtally = 0
#for i in range(100000):
#    x = random.random()
#    y = random.random()
#    incircle = (x**2 + y**2) ** (0.5) <= 1
#    if incircle: intally += 1
#    else: outtally += 1
#    print ((intally/(intally+outtally))*4)
# DND stat rolls #random.seed(5) to fix rolls
import random

def dice3D6():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def dice3D6r1():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    while(a==1):
        a = random.randint(1,6)
    while(b==1):
        b = random.randint(1,6)
    while (c==1):
        c = random.randint(1,6)
    return a+b+c
    
def dice3D6x2():
    sum = 0
    for i in range (4):
        a = random.randint(1,6)
        b = random.randint(1,6)
        if a > b: sum +a
        else: sum+b
    return sum

def dice4D6d1():
    
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    d = random.randint(1,6)
    if 3*a < b+c+d: a = 0
    if 3*b < a+c+d: b = 0
    if 3*c < b+a+d: c = 0
    if 3*d < b+c+a: d = 0
    return a+b+c+d
#descendign order means you donnt have to check repreats

def det_avg(repeats, function):
    total = 0
    for i in range (repeats+1):
        total = total + function()
    return total/repeats
    
tupletest = 1, 'a', 1.2
#print(tupletest)
integer, string, string = tupletest
#print(integer, string)
#took latest assignment

#basket = 1,2,3,4,5,'snake',2.3
#for i in basket:
#    print(i)
    
#for i in range (51,0,-1):
#    prime = True
#    for a in range(2,(i//2)+3):
#        if i % a == 0: prime = False
#    if i == 1: print(i) 
#    elif prime: print(i,'*')
#    elif not prime: print(i)

#def over2(number):
#    return number/2

#def over3(number):
#    return number/3
#s is overstringi make list, for item in list try make function 2 for loops
#overall want to be able to define different varibale different 

varstring = 'over1','over2'
print (type(varstring))
for i in range(1,51):
    a = 'over' + str(i)
    varstring = varstring + tuple(a)
print(varstring)
print(type(varstring))
toople = 1,2,3,4
print(type(toople))


#for i in range(50):
#    s = 'over'+str(i)
#    def s(number):
#        return number/i
#    print(s)

def cutonionweight(weight, func):
    return func(weight)
    
print(cutonionweight(5, over3))
print(cutonionweight(5, over2))
