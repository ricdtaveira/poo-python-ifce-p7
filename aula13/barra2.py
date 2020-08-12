
import matplotlib.pyplot as plt

# Definindo variáveis
x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

# Criando um gráfico
plt.bar(x, y, label='Alunos', color='b')
plt.bar(x2, y2, label='Alunas', color='r')
plt.legend()

plt.show()