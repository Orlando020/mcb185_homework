import sys
import math

numbers = []
for arg in sys.argv[1:]:
    numbers.append(float(arg))
    print(numbers)
numbers.sort()

#value count
print('value count', len(numbers))

#minimum and maximum
maxi = mini = numbers[1]
for n in numbers:
    if maxi < n: maxi = n
    if mini > n: mini = n
print('maximum and minimum', maxi, mini)

#mean
total = 0
for n in numbers:
    total += n
print('mean', total/len(numbers))

#standard deviation
sdnumerator = 0
for n in numbers:
    sdnumerator += (n - (total/len(numbers) )) ** 2
print('standard deviation(pop)', math.sqrt(sdnumerator/len(numbers)))

#median
medilength = math.floor((len(numbers) / 2))
frombott = numbers[medilength - 1]
fromtop = numbers[-medilength]
print('median', (frombott+fromtop)/2)