"""
Given an array of integers that are out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted. For example,
given [ 3 , 7 , 5 , 6 , 9] , you should return ( 1 , 3 ) .
"""

def window(array):
    left, right= None, None
    s = sorted(array)
    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i
    return left, right

def window2(array):
    left, right= None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")
    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, array[i])
            if array[i] > min_seen:
                left = i
    return left, right

def locate_smallest(A):
    B = sorted(A)
    left = 0
    while left < len(A) and B[left] == A[left] :
        left += 1
    right = len(A) - 1
    while right > 0 and B[right] == A[right]:
        right -= 1
    return left, right

start = time.perf_counter()
result_1 = window([ 3, 7, 5, 6, 9])
finish = time.perf_counter()
total_time_1 = f"Total time is : {finish-start}"

start = time.perf_counter()
result_2 = window2([ 3, 7, 5, 6, 9])
finish = time.perf_counter()
total_time_2 = f"Total time is : {finish-start}"

start = time.perf_counter()
result_3 = locate_smallest([ 3, 7, 5, 6, 9])
finish = time.perf_counter()
total_time_3 = f"Total time is : {finish-start}"

best_score = min(total_time_1, total_time_2, total_time_3)

#total_time_1 : 4.183300188742578e-05
#total_time_2 : 6.438699347199872e-05
#total_time_3 : 3.755999932764098e-05

#best_score => total_time_3
