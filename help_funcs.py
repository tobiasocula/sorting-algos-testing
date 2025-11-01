import numpy as np

def mostly_constant_array(length, avg_num_count, constant_ratio=0.9):
    const_val = np.random.randint(0, length // avg_num_count)
    num_constant = int(length * constant_ratio)
    arr = [const_val] * num_constant
    arr += list(np.random.randint(0, length // avg_num_count, length - num_constant))
    np.random.shuffle(arr)
    return arr

def partially_sorted_array(length, unsorted_ratio=0.1):
    arr = list(range(length))
    num_unsorted = int(length * unsorted_ratio)
    indices_to_shuffle = np.random.choice(length, num_unsorted, replace=False)
    for idx in indices_to_shuffle:
        swap_with = np.random.randint(0, length)
        arr[idx], arr[swap_with] = arr[swap_with], arr[idx]
    return arr
