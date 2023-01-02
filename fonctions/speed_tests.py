#tests
from time import perf_counter
time_p = []
time_j = []
for i in range(10000):
    fx = "dsa"
    start = perf_counter()
    fx += "=0"
    end = perf_counter()
    start2 = perf_counter()
    fx = fx.__add__("=0")
    end2 = perf_counter()
    time_p.append(start-end)
    time_j.append(start2-end2)

avr_p = sum(time_p)/len(time_p)
avr_j = sum(time_j)/len(time_j)

print("avr p :", avr_p)
print("avr j :", avr_j)
