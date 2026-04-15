from memory_profiler import memory_usage
import numpy as np
import matplotlib.pyplot as plt
import algorithms

N_TESTS = 2
START_LEN = 10
END_LEN = 20
TIME_MEMORY_INTERVAL = 0.5
array_lengths = list(range(START_LEN, END_LEN))

AVG_NUM_COUNT = 5

memories = np.empty((len(array_lengths), 6, N_TESTS))

for j in range(N_TESTS):
    for i, arrlen in enumerate(array_lengths):

        arr = np.random.randint(0, arrlen // AVG_NUM_COUNT, arrlen).tolist()

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.insertion_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, 0, j] = max(mem_after) - min(mem_before)

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.selection_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, 0, j] = max(mem_after) - min(mem_before)

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.merge_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, 0, j] = max(mem_after) - min(mem_before)

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.quick_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, 0, j] = max(mem_after) - min(mem_before)

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.counting_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, 0, j] = max(mem_after) - min(mem_before)

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.radix_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, 0, j] = max(mem_after) - min(mem_before)
        print('done for arlen', arrlen)

    print('done with 1')

memories_final = np.mean(memories, axis=2)

algos = [
    "insertion_sort",
    "selection_sort",
    "merge_sort",
    "quick_sort",
    "counting_sort",
    "radix_sort"
    ]
for k in range(6):
    plt.plot(memories_final[:, k], label=algos[k])
plt.legend()
plt.show()


