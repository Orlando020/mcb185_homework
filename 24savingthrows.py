import random

def savingthrow(DC):
    roll = random.randint(1,20)
    result = roll>=DC
    return result

def advsavingthrow(DC):
    a = savingthrow(DC)
    b = savingthrow(DC)
    if a or b: return True
    else: return False
    
def disadvsavingthrow(DC):
    a = savingthrow(DC)
    b = savingthrow(DC)
    if a and b: return True
    else: return False
    
def simulator(repeats,function,DC):
    success = 0
    total = 0
    for i in range(repeats):
        result = function(DC)
        if result: success += 1
        total += 1
    return(success/total)

print(simulator(100, savingthrow,10))
print(simulator(200,advsavingthrow,15))
print(simulator(50, disadvsavingthrow,15))