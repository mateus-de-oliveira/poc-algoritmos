import time

aux_list = list(range(1, 500000001))

def binary_search(list, item):
  low = 0
  high = len(list) - 1
  
  while low <= high:
    mid = (low+high) // 2
    guess = list[mid]
    
    if guess == item:
      return mid
    if guess > item:
       high = mid - 1
    else:
      low = mid + 1
    
  return None


start_time = time.time()
binary_search(aux_list, 537)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Binary search execution time (item in the middle of the list): {elapsed_time:.10f} seconds")


start_time = time.time()
binary_search(aux_list, 1000)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Binary search execution time (item at the end of the list): {elapsed_time:.10f} seconds")


start_time = time.time()
binary_search(aux_list, 2)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Binary search execution time (item at the beginning of the list): {elapsed_time:.10f} seconds")

print("==============================================================================")

def linear_search(list, item):
  for index, num in enumerate(list):
    if item == num:
      return index

  return None

start_time = time.time()
linear_search(aux_list, 537)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Linear search execution time (item in the middle of the list): {elapsed_time:.10f} seconds")


start_time = time.time()
linear_search(aux_list, 1000)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Linear search execution time (item at the end of the list): {elapsed_time:.10f} seconds")


start_time = time.time()
linear_search(aux_list, 2)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Linear search execution time (item at the beginning of the list): {elapsed_time:.10f} seconds")
print("==============================================================================")