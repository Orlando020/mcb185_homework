import random

def deathsaves():
    success = 0
    critsuccess = 0
    failure = 0
    while True: 
        roll = random.randint(1,20)
        if roll == 20: critsuccess += 1
        elif roll >= 10: success += 1
        elif roll < 10: failure += 1
        if critsuccess == 1: return 'critical success!'
        elif success == 3: return 'stabilize'
        elif failure == 3: return 'die'
    
def simulator(repeat):
    totalcritsuccess = 0
    totalsuccess = 0
    totalfailure = 0
    for i in range(repeat):
        result = deathsaves()
        if result == 'critical success!': totalcritsuccess += 1
        elif result == 'stabilize': totalsuccess += 1
        elif result == 'die': totalfailure += 1
    return totalcritsuccess, totalsuccess, totalfailure
    
#one death save
print(deathsaves())

#result number of many death saves
print(simulator(1000))

#probabilities of many death saves, another instance of simulation
probrepeats = 1000
probcrit, probsucc, probfail = simulator(probrepeats)
print(probcrit/probrepeats, probsucc/probrepeats, probfail/probrepeats)