import matplotlib.pyplot as plt

# Definindo variáveis
fatias = [6, 4, 10]
atividades = ['X', 'Y', 'Z']
colunas = ['r', 'm', 'y']

# Criando um gráfico
plt.pie(fatias, labels = atividades, colors = colunas, startangle = 90, shadow = True, explode = (0.1, 0, 0))

plt.show()