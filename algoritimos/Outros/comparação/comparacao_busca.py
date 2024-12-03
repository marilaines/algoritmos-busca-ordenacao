import matplotlib.pyplot as plt

algoritmos = ['Busca Binária', 'Busca por Interpolação', 'Jump Search', 'Exponential Search']
tempos = [0.002, 0.0018, 0.0025, 0.0015]
tamanhos = [10, 100, 1000, 10000]

plt.figure(figsize=(10, 6))
for i, algoritmo in enumerate(algoritmos):
    tempos_escala = [tempo * (tam / 1000) for tempo, tam in zip([tempos[i]] * len(tamanhos), tamanhos)]
    plt.plot(tamanhos, tempos_escala, marker='o', label=algoritmo)

plt.title('Comparação de Algoritmos de Busca')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (s)')
plt.legend()
plt.grid(True)
plt.show()
