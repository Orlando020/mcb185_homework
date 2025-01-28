import math

def char_to_prob(a):
    b = ord(a) - 33
    if b >= 0 and b <= 40:
        return pow(10,(-b/10))
    else: return None
    
def prob_to_char(a):
    if a >= 0 and a <= 1: 
        b = -10 * math.log10(a)
    else: return None
    c = round(b, ndigits=0)
    return chr(int(c+33))
    
    
print(char_to_prob('F'))
print(char_to_prob('!'))
print(char_to_prob('+'))

print(char_to_prob('a'))

print(prob_to_char(0.0001995))
print(prob_to_char(0.9999))
print(prob_to_char(0.1))

print(prob_to_char(1.000001))

#print(prob_to_char(-0.3))
#print(prob_to_char(0.09))
#print(prob_to_char(0.089))
#print(prob_to_char(0.083))