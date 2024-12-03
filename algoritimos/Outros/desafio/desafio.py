def programa_interativo():
  print("Escolha uma ação:")
  print("1. Binary Search")
  print("2. Merge Sort")
  print("3. Quick Sort")
  escolha = int(input("Digite o número da opção: "))

  if escolha == 1:
      from busca.binary_search import binary_search
      arr = list(map(int, input("Digite uma lista ordenada de números: ").split()))
      target = int(input("Digite o número a ser encontrado: "))
      print("Resultado:", binary_search(arr, target))
  elif escolha == 2:
      from ordenacao.merge_sort import merge_sort
      arr = list(map(int, input("Digite uma lista de números: ").split()))
      merge_sort(arr)
      print("Lista ordenada:", arr)
  elif escolha == 3:
      from ordenacao.quick_sort import quick_sort
      arr = list(map(int, input("Digite uma lista de números: ").split()))
      print("Lista ordenada:", quick_sort(arr))
  else:
      print("Opção inválida.")

if __name__ == "__main__":
  programa_interativo()
