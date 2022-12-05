import time


now = time.time()
time_delta = 0
while True:

    time_delta = time.time() - now
    now = time.time()
    print(time_delta)
