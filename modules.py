import math
import random
import datetime

#num = int(input())
'''num = 91
print(int(math.sqrt(num)))
print(int(math.pow(2, 3)))
print(math.factorial(5))


print(random.randint(1, 100))


dt = datetime.datetime.now()

print(dt)

#creating user defined module

import calendar

year  = 2004
month = 12
print(calendar.month(year, month))'''

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def simple_interest(p, r, t):
    return (p * r * t) / 100

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"