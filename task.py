import time
def task_1():
    resistors = int(input("Please enter the number of resistors: "))
    total_resistance = 0
    for x in range(resistors):
        total_resistance += float(input(f"Please enter the Ohms in resistor {x + 1}: "))
    return total_resistance

def task_2(cost):
    tip = float(input("Please enter a tip as a percentage: "))
    while tip == False:
        tip = float(input("Don't be rude. Please enter a tip as a percentage: "))
    tip = tip / 100
    tip = cost * tip
    cost = cost * 1.20
    cost = cost + tip
    #total_cost = cost * 1.20
    return cost

def task_3():
    result = []
    number = int(input("Please enter a number above 0: "))
    while not number > 0:
        number = int(input("ERROR: Number must be above 0. Try again: "))
    for x in range(1, number + 1):
        if x % 3 == 0 and not x % 5 == 0:
            result.append("Fizz")
        elif not x % 3 == 0 and x % 5 == 0:
            result.append("Buzz")
        elif x % 3 == 0 and x % 5 == 0:
            result.append("Fizz Buzz")
        else:
            result.append(x)
    return result

def task_4():
    result = []
    n = int(input("Please enter a number above 0: "))
    while not n > 0:
        n = int(input("ERROR: Number must be above 0. Try again: "))
    while not n == 1:
        result.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3
            n = n + 1
    result.append(n)
    return result

def task_5():
    height = None
    n = int(input("Please enter a number above 0: "))
    while not n > 0:
        n = int(input("ERROR: Number must be above 0. Try again: "))
    layer = 1
    height = 0
    while not n == 0:
        if (n - layer) >= 0:
            n = n - layer
            layer += 1
            height += 1
        else:
            break
    return height
