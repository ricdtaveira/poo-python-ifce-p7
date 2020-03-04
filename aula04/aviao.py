"""
Módulo aviao
Classe Aviao
"""
from veiculo import IVeiculo

class Aviao(IVeiculo):
    # mostrará uma mensagem que ligou o veiculo
    def liga (self):
        print("Ligou Aviao")
    # mostrará uma mensagem que virou a direita    	 
    def viraParaDireita(self):
        print("Aviao virou a Direita!")
    # mostrará uma mensagem que virou a esquerda 
    def viraParaEsquerda(self):
        print("Aviao virou para a Esquerda!")
    # mostrará uma mensagem que acelerou	 
    def acelera(self):  
        print("Aviao acelerou!")
    # mostrará uma mensagem que freiou
    def freia(self):
        print("Aviao freiou!")     
    # mostrará uma mensagem que desligou  
    def desliga(self):
        print("Aviao Desligou!\n")
    

