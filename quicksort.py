import random
import time


def quickSort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quickSort(array, low, pivot_index)
        quickSort(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

n = 10**7 # 10**3 , 10**4, 10**5
sorted_list = list(range(n))
descending_list = list(range(n, 0, -1))
half_sorted_list = list(range(1, n//2)) + random.sample(range(n//2+1, n+1), n//2)
random_list =[random.randint(1, n) for _ in range(n)]



start_time1 = time.time()
quickSort(sorted_list)
end_time1 = time.time()
execution_time_sorted1 = end_time1 - start_time1
print(execution_time_sorted1)

start_time2 = time.time()
quickSort(descending_list)
end_time2 = time.time()
execution_time_sorted2 = end_time2 - start_time2
print(execution_time_sorted2)

start_time3 = time.time()
quickSort(half_sorted_list)
end_time3 = time.time()
execution_time_sorted3 = end_time3 - start_time3
print(execution_time_sorted3)

start_time4 = time.time()
quickSort(random_list)
end_time4 = time.time()
execution_time_sorted4 = end_time4 - start_time4
print(execution_time_sorted4)
