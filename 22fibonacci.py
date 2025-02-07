curro = 0
prevo = 0
prev2 = 1
for i in range (10):
    print(curro)
    curro = prevo + prev2
    prev2 = prevo
    prevo = curro