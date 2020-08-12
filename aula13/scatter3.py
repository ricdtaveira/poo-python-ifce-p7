
import matplotlib.pyplot as plt

# Definindo variáveis
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 5, 6, 8, 4, 8]

# Criando um gráfico
plt.scatter(x, y, label='Pontos', color='b', marker='*', s=100)
plt.legend()

plt.show()