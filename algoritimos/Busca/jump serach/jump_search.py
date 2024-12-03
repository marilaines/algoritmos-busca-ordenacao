import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11]
    elemento = 9
    resultado = jump_search(lista, elemento)
    print(f"Elemento {elemento} encontrado no índice: {resultado}")
