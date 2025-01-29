import math

def graph_dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
print (graph_dist(0,0,1,1))
print (graph_dist(-3,-4,0,0))

def valid_prob(prob):
    if prob <= 1 and prob >=0: return True
    return False
    
print(valid_prob(2))
print(valid_prob(0.004))

def biggest_of_four(a,b,c,d):
    if a >= b and a >= c and a >= d: return a
    if b >= a and b >= c and b >= d: return b
    if c >= b and c >= a and c >= d: return c
    if d >= b and d >= c and d >= a: return d
    
print(biggest_of_four(1,2,4,5))
print(biggest_of_four(4,4,2,1))

def position_to_orf(position):
    orf = position % 3
    if position <= 3: return position 
    return orf + 1
    

print(position_to_orf(13))
print(position_to_orf(3))