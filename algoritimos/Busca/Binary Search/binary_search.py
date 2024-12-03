def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11]
    elemento = 7
    resultado = binary_search(lista, elemento)
    print(f"Elemento {elemento} encontrado no índice: {resultado}")
