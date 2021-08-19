
from aluno import Aluno 

# Construindo dois objetos da classe Aluno
# com os seus atributos
a = Aluno(100, "Joana", "Av. 13 de Maio 2081")
b = Aluno(200, "João Pedro", "Av. João Pessoa 1200")
c = Aluno(300, "Rodrigo Bastos", "Av Luciano Carneiro 1000")
d = Aluno(400, "Pedro Bastos", "Av Luciano Carneiro 1000")

print("Matricula= " + str(a.get_matricula()))
print("Nome= " + str(a.get_nome()))

a.set_matricula(150)
a.set_nome("Maria Joana")

print("Matricula= " + str(a.get_matricula()))
print("Nome= " + str(a.get_nome()))

print(a)
print(b)
a.printSelf()
print(a.toString())
b.printSelf()
print(b.toString())


