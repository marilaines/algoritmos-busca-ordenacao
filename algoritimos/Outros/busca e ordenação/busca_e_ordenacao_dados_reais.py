def bucket_sort(arr):
  max_value = max(arr)
  size = max_value // len(arr) + 1
  buckets = [[] for _ in range(len(arr))]

  for num in arr:
      index = num // size
      buckets[index].append(num)

  for bucket in buckets:
      bucket.sort()

  sorted_arr = []
  for bucket in buckets:
      sorted_arr.extend(bucket)
  return sorted_arr

def interpolation_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high and arr[low] <= target <= arr[high]:
      if low == high:
          if arr[low] == target:
              return low
          return -1
      pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
      if arr[pos] == target:
          return pos
      elif arr[pos] < target:
          low = pos + 1
      else:
          high = pos - 1
  return -1

if __name__ == "__main__":
  notas = [85, 90, 45, 78, 92, 88, 76, 60, 95, 70]
  notas_ordenadas = bucket_sort(notas)
  print("Notas ordenadas:", notas_ordenadas)

  nota_procurada = 92
  indice = interpolation_search(notas_ordenadas, nota_procurada)
  if indice != -1:
      print(f"Nota {nota_procurada} encontrada no índice {indice}.")
  else:
      print(f"Nota {nota_procurada} não encontrada.")
