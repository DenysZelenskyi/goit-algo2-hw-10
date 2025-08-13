import time
import random
import numpy as np
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = arr.copy()
        start = time.time()
        sort_function(arr_copy)
        end = time.time()
        times.append(end - start)
    return np.mean(times)

sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    randomized_time = measure_time(randomized_quick_sort, arr)
    deterministic_time = measure_time(deterministic_quick_sort, arr)
    randomized_times.append(randomized_time)
    deterministic_times.append(deterministic_time)
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {randomized_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд")

plt.figure(figsize=(10, 5))
plt.plot(sizes, randomized_times, label='Рандомізований QuickSort', marker='o')
plt.plot(sizes, deterministic_times, label='Детермінований QuickSort', marker='s')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (сек)')
plt.title('Порівняння QuickSort')
plt.legend()
plt.grid()
plt.show()