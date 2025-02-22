import sys
import math

probs = []
for arg in sys.argv[1:]:
    f = float(arg)
    if f <= 0 or f >= 1: sys.exit('error not a prob')
    probs.append(float(arg))
    
total = 0
for p in probs: total += p
if not math.isclose(total,1.0):
    sys.exit('eror probs not summin to one')
    
h = 0 
for p in probs:
    h -= p * math.log2(p)
    # print (p*math.log2(p))
    
print(f'{h:.4f}')