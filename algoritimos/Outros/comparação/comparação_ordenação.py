import matplotlib.pyplot as plt


algoritmos = ['Shell Sort', 'Merge Sort', 'Selection Sort', 'Quick Sort', 'Bucket Sort', 'Radix Sort']
tempos = [0.12, 0.08, 0.15, 0.09, 0.10, 0.07]

plt.figure(figsize=(10, 6))
plt.bar(algoritmos, tempos, color=['blue', 'green', 'orange', 'red', 'purple', 'cyan'])
plt.title('Comparação de Algoritmos de Ordenação')
plt.xlabel('Algoritmos')
plt.ylabel('Tempo de Execução (s)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
