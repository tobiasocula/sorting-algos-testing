import numpy as np
import time
import matplotlib.pyplot as plt
import algorithms
from help_funcs import partially_sorted_array

N_TESTS = 10
NUM_ARRAYS_PER_TEST = 200
START_LEN = 100
END_LEN = 10000
array_lengths = np.unique(np.logspace(np.log10(START_LEN), np.log10(END_LEN), num=NUM_ARRAYS_PER_TEST, dtype=int))
AVG_NUM_COUNT = 5
unsorted_ratio = 0.2

times = np.empty((len(array_lengths), 6, N_TESTS))

for j in range(N_TESTS):
    for i, arrlen in enumerate(array_lengths):

        arr = partially_sorted_array(arrlen, unsorted_ratio)

        t = time.time()
        algorithms.insertion_sort(arr)
        times[i, 0, j] = time.time() - t

        t = time.time()
        algorithms.selection_sort(arr)
        times[i, 1, j] = time.time() - t

        t = time.time()
        algorithms.merge_sort(arr)
        times[i, 2, j] = time.time() - t

        t = time.time()
        algorithms.quick_sort(arr)
        times[i, 3, j] = time.time() - t

        t = time.time()
        algorithms.counting_sort(arr)
        times[i, 4, j] = time.time() - t

        t = time.time()
        algorithms.radix_sort(arr)
        times[i, 5, j] = time.time() - t

times_final = np.mean(times, axis=2)
algos = [
    "insertion_sort",
    "selection_sort",
    "merge_sort",
    "quick_sort",
    "counting_sort",
    "radix_sort"
    ]
for k in range(6):
    plt.plot(times_final[:, k], label=algos[k])
plt.legend()
plt.show()

