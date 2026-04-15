from memory_profiler import memory_usage
import numpy as np
import matplotlib.pyplot as plt
import algorithms

N_TESTS = 2
START_LEN = 10000
END_LEN = 10200
TIME_MEMORY_INTERVAL = 0.1
array_lengths = list(range(START_LEN, END_LEN))

AVG_NUM_COUNT = 5

memories = np.empty((len(array_lengths), N_TESTS))

for j in range(N_TESTS):
    for i, arrlen in enumerate(array_lengths):

        arr = np.random.randint(0, arrlen // AVG_NUM_COUNT, arrlen).tolist()

        mem_before = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        algorithms.radix_sort(arr)
        mem_after = memory_usage(-1, interval=TIME_MEMORY_INTERVAL, timeout=1)
        memories[i, j] = max(mem_after) - min(mem_before)
        print('done for arlen', arrlen)

    print('done with 1')

memories_final = np.mean(memories, axis=1)
plt.plot(memories_final)
plt.legend()
plt.show()


