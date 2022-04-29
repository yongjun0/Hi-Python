import time
import random

def very_slow_random_generator():
    time.sleep(5)
    arr = [random.randint(1,100) for i in range(1000)]

    return sum(arr) / len(arr)

def slow_random_generator():
    time.sleep(2)
    arr = [random.randint(1,100) for i in range(1000)]
    return sum(arr) / len(arr)

def fast_random_generator():
    time.sleep(1)
    arr = [random.randint(1,100) for i in range(1000)]
    return sum(arr) / len(arr)


def main_func():
    result = fast_random_generator()
    print(result)

    result = slow_random_generator()
    print(result)

    result = very_slow_random_generator()
    print(result)

t0 = time.time()
result = very_slow_random_generator()
t1 = time.time()
print(f'slow: time = {t1-t0:.2f} sec')

result = slow_random_generator()
t2 = time.time()
print(f'slow: time = {t2-t1:.2f} sec')

result = fast_random_generator()
t3 = time.time()
print(f'slow: time = {t3-t2:.2f} sec')





