for i in range(1,101,1):
    if i%3 == 0 and not(i%5 == 0): word = 'Fizz'
    elif i%5 == 0 and not(i%3 == 0): word = 'Buzz'
    elif i%3 == 0 and i%5 == 0: word = 'FizzBuzz'
    else: word = i
    print(word)