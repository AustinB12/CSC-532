import time
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from max_subarray import max_subarray
import random

# for x in range(250, 10250, 250):
#     start = time.time()
#     insertion_sort(sorted_list[0:x])
#     print(round(time.time() - start, 3))

# for x in range(250, 10250, 250):
#     start = time.time()
#     merge_sort(sorted_list[0:x])
#     print(round(time.time() - start, 3))

rand_list = []
for i in range(0, 10000):
    rand_list.append(random.randint(-1000, 1000))

for x in range(250, 10250, 250):
    start = time.time()
    answer = max_subarray(rand_list[0:x], 0, x - 1)
    print(f"Size: {x},\tResult: {answer},\tTime: {round(time.time() - start, 3)} seconds")