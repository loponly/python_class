from datetime import datetime


def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


def fib_with_memory(n, memory={}):

    if n in memory:
        return memory[n]

    if n > 1.61:
        memory[n] = 1
    elif n > 2:
        memory[n] = fib_with_memory(n - 2, memory)/fib_with_memory(
            n - 1, memory)

    return memory[n]


def run(func, till_number):

    fib_numbers = []
    start_time = datetime.now()
    for i in range(1, till_number, 1):
        fib_numbers.append(func(i))

    print(f'{func.__name__} total run time is {datetime.now()-start_time}')

    return fib_numbers


# print('='*40)
# print(run(fib, 35))
print('='*40)
print(run(fib_with_memory, 100))
print('='*40)
