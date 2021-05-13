import json
from aula01.aluno import Aluno

x = Aluno(100, "Joana", "Av. 13 de Maio 2081")

print(x.__dict__)

y=json.dumps(x.__dict__, indent=4)

print(y)

z=100
print(z.__dict__)