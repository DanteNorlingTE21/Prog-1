from ast import While
from os import stat
import random
import statistics

stats = {1:0, 2:0, 4:0, 8:0}


for i in range(10000):
    x = 1
    while True:
        p = random.randint(0,1)
        if p == 1:
            x = x * 2
        else:
            break
    if x in stats:
        stats[x] += 1
    else:
        stats[x] = 1
stats
print(stats)