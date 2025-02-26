import random
import sys
#input python3 34birthday.py 10000 365 23
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def bdaygacha(days, people):
    calendar = []
    for i in range(days):
        calendar.append(0)
    for i in range(people):
        guy = random.randint(0,days)
        calendar[guy] += 1
        if calendar[guy] == 2: return True
    return False

matches = 0
for i in range(trials+1):
    result = bdaygacha(days,people)
    if result: matches += 1
print(matches/trials)