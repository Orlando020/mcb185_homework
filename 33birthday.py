import random
import sys
#input python3 33birthday.py 10000 365 23
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#building list while comparing

def bdaygacha(days, people):
    bdaylist = []
    for i in range(people):
        guy = random.randint(0,364)
        if guy in bdaylist: return True
        bdaylist.append(guy)
    return False
    
#comparing preconstructed list 

# def bdaygachamat(days,people):
    # bdaylist = []
    # for i in range(people):
        # bdaylist.append(random.randint(0,364))
    # for i in range(len(bdaylist)):
        # for j in range(i + 1,len(bdaylist)):
            # if bdaylist[i] == bdaylist[j]: return True
    # return False

matches = 0
for i in range(trials+1):
    result = bdaygacha(days,people)
    if result: matches += 1
print(matches/trials)

# matchmat = 0
# for i in range(trials+1):
    # result = bdaygachamat(days,people)
    # if result: matchmat += 1
# print (matchmat/trials)