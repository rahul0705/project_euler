'''
Page one of Project Euler
@author: rahul
'''

def p1(x = 3, y = 5, end = 1000):
    total = 0
    current = 0

    while current < end:
        total += current
        current += x
        if current % (x * y) == 0:
            total -= current
    current = 0

    while current < end:
        total += current
        current += y
    return total

def p2(max_value=4000000):
    fib_numbers = {0:0, 1:1}
    i = 1
    total = 0
    
    while fib_numbers[i] < max_value:
        i += 1
        fib_numbers[i] = fib_numbers[i-1] + fib_numbers[i-2]
        if fib_numbers[i] % 2 == 0:
            total += fib_numbers[i]
    return total

def p3(number=600851475143):
    largest_factor = 0
    d = 2
    while number > 1:
        while number % d == 0:
            largest_factor = max(largest_factor, d)
            number /= d
        d = d + 1
    return largest_factor

if __name__ == '__main__':
    print p1()
    print p2()
    print p3()