import numpy as np
import time
import matplotlib.pyplot as plt
import algorithms

N_TESTS = 5
NUM_ARRAYS_PER_TEST = 200
START_LEN = 100
END_LEN = 100000
array_lengths = np.unique(np.logspace(np.log10(START_LEN), np.log10(END_LEN), num=NUM_ARRAYS_PER_TEST, dtype=int))
AVG_NUM_COUNT = 5

times = np.empty((len(array_lengths), 4, N_TESTS))

for j in range(N_TESTS):
    for i, arrlen in enumerate(array_lengths):

        arr = np.random.randint(0, arrlen // AVG_NUM_COUNT, arrlen).tolist()

        t = time.time()
        algorithms.merge_sort(arr)
        times[i, 0, j] = time.time() - t

        t = time.time()
        algorithms.quick_sort(arr)
        times[i, 1, j] = time.time() - t

        t = time.time()
        algorithms.counting_sort(arr)
        times[i, 2, j] = time.time() - t

        t = time.time()
        algorithms.radix_sort(arr)
        times[i, 3, j] = time.time() - t

times_final = np.mean(times, axis=2)
algos = [
    "merge_sort",
    "quick_sort",
    "counting_sort",
    "radix_sort"
    ]
for k in range(4):
    plt.plot(times_final[:, k], label=algos[k])
plt.legend()
plt.show()

