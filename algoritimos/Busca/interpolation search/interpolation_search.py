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
    lista = [1, 3, 5, 7, 9, 11]
    elemento = 5
    resultado = interpolation_search(lista, elemento)
    print(f"Elemento {elemento} encontrado no índice: {resultado}")
