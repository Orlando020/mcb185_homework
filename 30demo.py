#print('quote','"quote"','she sell\'s seashells','\\\\', '')
s = 'The quick brown fox jumps over the lazy dog'

# print('len',len(s))
# print(s.count('o'))
# print(s.rstrip('og'))
# print(s.replace('dog','fox'))
# print(s.replace('dog','fox').replace('jump','eat'))
# print(s.upper())
# if True:
    # print('ababbaba'), print('assdasfsdf')
# print('a'+'b')
# print(chr(123))
# print(ord('b'))

import math

# print(f'{1e6 * math.pi:e}')
# print(f'{"hello world":.>20}')
# print(f'{20:<1000} {10}')
# print(f'{23**4/51}')

# toople = 'aba','dara'
# stroong = 'sadfsa'

# print(toople[1],stroong[1])

# seq = 'GAATTC'
# for nt in seq:
    # print(nt, end='')
#   print(nt)
#   print(nt)
#   print(nt)
# print('')
#for nt in seq:
#   print(nt, end='')
# for i in range(len(seq)):
    # print(i,seq[i])
    
# print('terrify', end='')
# print('terrify')
# print('terrigy')

alpa = 'abcdefgh'

#print(alpa[3:5])
#print(alpa[::-1])

bucket = 'cat','melon', 'gun'

#print(bucket)
#print(bucket[::-1])

#for i in range(len(alpa)):
#    print(i,alpa[i])
short = 'abc'
#for i, alpa in enumerate(alpa):
#    print(i,alpa)
#print(type(enumerate(alpa)))

# for i in range(len(bucket)):
    # print(short[i], bucket)

# for i, bucket in zip(short,bucket):
    # print(i,bucket)
    
# for i, bucket in zip(alpa,bucket):
    # print(i,bucket)
    
# for i, (nt, bucket) in enumerate(zip(short,bucket)):
    # print(i,nt,bucket)
    
# for i,nt in enumerate(alpa):
    # print(i,nt)
    
# listo = ['a','b','c','a']
# print(listo)
# listo[2] = 'd'
# print(listo)
# listo.append('m')
# print(listo)
# listo.pop()
# print(listo)
# listo.sort()
# print(listo)
# losto = listo.copy()
# print(losto)

# stringus = 'apple bottom jeans boots with the fur'
# print(stringus)
# listius = stringus.split()
# print(listius)

# print('and'.join(listius))
# print(listius)

#listeria = ['a','A','b','c','As']

# def findlistmax(lis):
    # maxi = ' '
    # for i, nt in enumerate(lis):
        # if maxi < nt: maxi = nt
        # print(nt, maxi)
    # return maxi

# print(findlistmax(listeria))

# import sys
# print(sys.argv)

# monty hall
# import random
# doors = [1,2,3]
# random.seed(153)
# def montysetup():
    # cardoor = random.randint(1,3)
    # if cardoor == 1: return cardoor, random.choice([2,3])
    # if cardoor == 2: return cardoor, random.choice([1,3])
    # if cardoor == 3: return cardoor, random.choice([1,2])
    
# def montyswapper(goatreveal):
    # pick = random.randint(1,3)
    # baddoor = [pick,goatreveal]
    # for i in range(2):
        # for j in range(3):
            # matchpresent = 0
            # if doors[j] == baddoor[i]: 
                # pick = doors[j]
                # matchpresent = True
            # if not matchpresent: pick = doors[j]
            # print(doors[j],baddoor[i])
    # return pick
    
# def montystayer(goatreveal):
    # pick = random.randint(1,3)
    # return pick
    
# def simulator(montyfunc, repeats):
    # win = 0
    # for i in range(repeats):
        # cardoor, goatreveal = montysetup()
        # pick = montyfunc(goatreveal)
        # if pick == cardoor: win += 1
    # return win/repeats

# print(simulator(montyswapper,1))
# print(simulator(montystayer,10))








#monty hall attempt 2 list subtraction i still need, can search the list but not eliminate bits, maybe .pop has targeting
# import random
# doors = [1,2,3]

# def montysetup():
    # cardoor = random.randint(1,3)
    # pick = random.randint(1,3)
    # potendoors = doors.copy()
    # goatreveal = False
    # if pick in potendoors: potendoors.pop(potendoors.index(pick))
    # if cardoor in potendoors: potendoors.pop(potendoors.index(cardoor))
    # if len(potendoors) == 2:
        # goatreveal = random.choice(potendoors)
    # else: goatreveal = potendoors[0]
    # return cardoor, pick, goatreveal
    
# def montyswapper(cardoor, pick, goatreveal):
    # wantdoor = doors.copy()
    # if pick in wantdoor: wantdoor.pop(wantdoor.index(pick))
    # if goatreveal in wantdoor: wantdoor.pop(wantdoor.index(goatreveal))
    # pick = wantdoor[0]
    # return pick, cardoor

# win = 0
# repeat = 1000
# for i in range(repeat):
    # a, b = montyswapper(*montysetup())
    # if a == b: win +=1
# print(win/repeat)





# print(type(range(20)))
# for i in enumerate('stringo'):
    # print (i)
# nts = ['ok','howsy','nihao']
# names = ['jeery','jebediah','timmy']
# for i, (nt, name) in enumerate(zip(nts, names)):
    # print(i, nt, name)
# for i in zip(nts,names):
    # print (i)
#in is used in in range
# print(type(enumerate(nts)))
# print(type(zip(nts)))

# if blank in blank is same as for loop
# checking each element, 'in' has more stuff it can do

#for i in range(1,3)
#if 'ok' in nts:


# print('-'.join(list('ABCDE'))[3:6])

#n50
import sys

numbers = []
for arg in sys.argv[1:]:
    numbers.append(int(arg))
print(numbers)

numbers.sort()
longness_tot = 0

for n in numbers:
    longness_tot += n

medpath = 0
totprogress = 0
for i in range(len(numbers)):
    totprogress += numbers[i]
    if longness_tot/2 < totprogress:
        medpath = i
        break
    
print('The N50: ', numbers[medpath])
