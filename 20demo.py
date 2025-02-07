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


def det_avg(repeats, function):
    total = 0
    for i in range (repeats+1):
        total = total + function()
    return total/repeats