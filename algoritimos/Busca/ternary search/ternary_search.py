def ternary_search(arr, left, right, target):
  if right >= left:
      mid1 = left + (right - left) // 3
      mid2 = right - (right - left) // 3

      if arr[mid1] == target:
          return mid1
      if arr[mid2] == target:
          return mid2

      if target < arr[mid1]:
          return ternary_search(arr, left, mid1 - 1, target)
      elif target > arr[mid2]:
          return ternary_search(arr, mid2 + 1, right, target)
      else:
          return ternary_search(arr, mid1 + 1, mid2 - 1, target)
  return -1

if __name__ == "__main__":
  lista = [1, 3, 5, 7, 9, 11]
  elemento = 7
  resultado = ternary_search(lista, 0, len(lista) - 1, elemento)
  print(f"Elemento {elemento} encontrado no índice: {resultado}")
