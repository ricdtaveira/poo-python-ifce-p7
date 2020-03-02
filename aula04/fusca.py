"""
Módulo fusca
Classe Fusca
"""
from aula04.veiculo import IVeiculo

class Fusca(IVeiculo):
    # mostrará uma mensagem que ligou o veiculo
    def liga (self):
        print("Ligou Fusca")
    # mostrará uma mensagem que virou a direita    	 
    def viraParaDireita(self):
        print("Fusca virou a Direita!)")
    # mostrará uma mensagem que virou a esquerda 
    def viraParaEsquerda(self):
        print("Fusca virou para a Direita")
    # mostrará uma mensagem que acelerou	 
    def acelera(self):  
        print("Fusca acelerou !")
    # mostrará uma mensagem que freiou
    def freia(self):
        print("Fusca freiou!")     
    # mostrará uma mensagem que desligou  
    def desliga(self):
        print("Fusca Desligou!")
    