import time
import random
import prof_sub as sub

t0 = time.time()
result = sub.very_slow_random_generator()
t1 = time.time()
print(f'slow: time = {t1-t0:.2f} sec')

result = sub.slow_random_generator()
t2 = time.time()
print(f'slow: time = {t2-t1:.2f} sec')

result = sub.fast_random_generator()
t3 = time.time()
print(f'slow: time = {t3-t2:.2f} sec')

