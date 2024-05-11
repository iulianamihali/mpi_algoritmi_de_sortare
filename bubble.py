import time
import random
sorted_data = list(range(1000))

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

n = 10**7 # 10**3 , 10**4, 10**5
sorted_list = list(range(n))
descending_list = list(range(n, 0, -1))
half_sorted_list = list(range(1, n//2)) + random.sample(range(n//2+1, n+1), n//2)
random_list =[random.randint(1, n) for _ in range(n)]



start_time1 = time.time()
bubbleSort(sorted_list)
end_time1 = time.time()
execution_time_sorted1 = end_time1 - start_time1
print(execution_time_sorted1)

start_time2 = time.time()
bubbleSort(descending_list)
end_time2 = time.time()
execution_time_sorted2 = end_time2 - start_time2
print(execution_time_sorted2)

start_time3 = time.time()
bubbleSort(half_sorted_list)
end_time3 = time.time()
execution_time_sorted3 = end_time3 - start_time3
print(execution_time_sorted3)

start_time4 = time.time()
bubbleSort(random_list)
end_time4 = time.time()
execution_time_sorted4 = end_time4 - start_time4
print(execution_time_sorted4)