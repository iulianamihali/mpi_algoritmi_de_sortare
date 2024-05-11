import random
import time


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


n = 10**7 # 10**3 , 10**4, 10**5
sorted_list = list(range(n))
descending_list = list(range(n, 0, -1))
half_sorted_list = list(range(1, n//2)) + random.sample(range(n//2+1, n+1), n//2)
random_list =[random.randint(1, n) for _ in range(n)]



start_time1 = time.time()
mergeSort(sorted_list)
end_time1 = time.time()
execution_time_sorted1 = end_time1 - start_time1
print(execution_time_sorted1)

start_time2 = time.time()
mergeSort(descending_list)
end_time2 = time.time()
execution_time_sorted2 = end_time2 - start_time2
print(execution_time_sorted2)

start_time3 = time.time()
mergeSort(half_sorted_list)
end_time3 = time.time()
execution_time_sorted3 = end_time3 - start_time3
print(execution_time_sorted3)

start_time4 = time.time()
mergeSort(random_list)
end_time4 = time.time()
execution_time_sorted4 = end_time4 - start_time4
print(execution_time_sorted4)