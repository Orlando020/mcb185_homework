# 10demo.py by Orlando_Shi

#print('hello, again') # greeting
#print(1.52e-2)

#def is_even(x):
#    if x %2 == 0: return True
#    return False

#print(is_even(2))
#print(is_even(3))
#a = vars
#b = vars
#a = 3
#b = 3
#c = a == b
#print(c)
#print(type(c))

#def isinterger(a):
#    if (a%1) == 0: return 'yes'
#    else: return 'no'
    
#print(isinterger(2))
#print(isinterger(2.1))
#print(isinterger(201))


def isntp(a):
    if a == 'a': return 491.2
    if a == 'c': return 467.2
    if a == 'g': return 507.2
    if a == 'T': return 482.2
    
print(isntp('a'))
print(isntp('b'))
print(isntp('c'))

def bigthree(x,y,z):
    if x > y and x > z: return x
    if y > x and y > z: return y
    if z > y and z > x: return z
    
print(bigthree(12,40,40))
import math

def minishannon(a,pdenom):
    if a == 0: return 0
    else: return a*pdenom* math.log2(a*pdenom)
    
def shannon(a,c,g,t):
    pdenom = 1/(a+c+g+t)
    a2 = minishannon(a, pdenom)
    c2 = minishannon(c, pdenom)
    g2 = minishannon(g, pdenom)
    t2 = minishannon(t, pdenom)
    return -(a2+c2+g2+t2)
    
print (shannon(1,2,3,4))
# better if I made a function sepeeratly for if stattemnt and formula
# shannon with equal chances
def asciinumber(a):
    return ord(a)
print(asciinumber('A') , asciinumber('!') , asciinumber ('@'))