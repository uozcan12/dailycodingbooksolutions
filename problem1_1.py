A = [1, 2, 3, 4, 5]
N = len(A)
B = [1] * N
prev, next = 1, 1
for i in range(0, N):
    B[i] = prev
    prev = prev * A[i]
print(B)
for i in range(N-1, -1, -1):
    B[i] = B[i] * next
    next = next * A[i]
print(B)

import numpy as np
import time 

def make_prod_list(a):
    prod_list = []
    for i in range(len(a)):
        n=a[:]    
        n.remove(a[i])
        prod_list.append(np.prod(n))
    return prod_list

start = time.perf_counter()
returned_function = make_prod_list(A)
finish = time.perf_counter()
total_time = f"Total time is : {finish-start}"
print(total_time)
