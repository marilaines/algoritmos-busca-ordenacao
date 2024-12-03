def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    def binary_search(arr, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    return binary_search(arr, i // 2, min(i, n - 1), target)

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11]
    elemento = 11
    resultado = exponential_search(lista, elemento)
    print(f"Elemento {elemento} encontrado no índice: {resultado}")
