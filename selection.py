import random
import time


def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

n = 10**7 # 10**3 , 10**4, 10**5
sorted_list = list(range(n))
descending_list = list(range(n, 0, -1))
half_sorted_list = list(range(1, n//2)) + random.sample(range(n//2+1, n+1), n//2)
random_list =[random.randint(1, n) for _ in range(n)]

start_time1 = time.time()
selectionSort(sorted_list)
end_time1 = time.time()
execution_time_sorted1 = end_time1 - start_time1
print(execution_time_sorted1)

start_time2 = time.time()
selectionSort(descending_list)
end_time2 = time.time()
execution_time_sorted2 = end_time2 - start_time2
print(execution_time_sorted2)

start_time3 = time.time()
selectionSort(half_sorted_list)
end_time3 = time.time()
execution_time_sorted3 = end_time3 - start_time3
print(execution_time_sorted3)

start_time4 = time.time()
selectionSort(random_list)
end_time4 = time.time()
execution_time_sorted4 = end_time4 - start_time4
print(execution_time_sorted4)