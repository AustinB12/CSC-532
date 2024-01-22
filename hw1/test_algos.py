import time
from lists import get_ordered_list, get_unordered_list
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from max_subarray import max_subarray

sorted_list = get_ordered_list()
unsorted_list = get_unordered_list()

for x in range(250, 10250, 250):
    start = time.time()
    insertion_sort(sorted_list[0:x])
    print(round(time.time() - start, 3))

for x in range(250, 10250, 250):
    start = time.time()
    merge_sort(sorted_list[0:x])
    print(round(time.time() - start, 3))

for x in range(250, 10250, 250):
    start = time.time()
    max_subarray(sorted_list[0:x], 0, len(sorted_list))
    print(round(time.time() - start, 3))