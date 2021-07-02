# Leibniz Series. More info can be found at wikiHow.com
from math import trunc
import time

start_time = time.time()

def value_pi(digit):
    current = 4
    previous = 0
    number = 0
    add_up = 1
    while abs(round(current, digit + 1) - round(previous, digit + 1)):
        add_up += 2
        previous = current
        if number < 0:
            number = 4 / add_up
        else:
            number = -4/ add_up
        current += number
        #print(f'calculating: {abs(round(current, digit + 1) - round(previous, digit + 1))}')
        #current_time = time.time()
        #print(current_time - start_time)

        #print(f'{current}\t{previous}\t{add_up}\t{number}')
        #print(f'{round(current, digit+1)}\t{round(previous, digit+1)}')

    return trunc(current * 10 ** digit) / (10 ** digit)

while True:
    try:
        digit = int(input('decimal number? :'))
        print(f'pi is {value_pi(digit)}')
        print(f'calculation took {time.time() - start_time} seconds.')
        break
    except:
        continue