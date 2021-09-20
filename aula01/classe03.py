class Person:
  x = 10
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # O Parametro self é uma referencia para a instancia(objeto) corrente da classe,
  # é usado para acessar variaveis que pertencem a classe.
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print(p1.x)

p2 = Person("Maria", 21)
p2.myfunc()
print(p2.x)

p1.x = 20
p2.x = 25

p1.endereco = "Av. da Universidade 1900"

print(p1.x)
del p1.endereco
del p1
print(p2.x)
print(p1.x)




