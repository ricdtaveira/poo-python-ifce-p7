"""
Módulo jegue
Classe Jegue
"""
from veiculo import IVeiculo

class Jegue(IVeiculo):
    # mostrará uma mensagem que ligou o veiculo
    def liga (self):
        print("Ligou Jegue")
    # mostrará uma mensagem que virou a direita    	 
    def viraParaDireita(self):
        print("Jegue virou a Direita!)")
    # mostrará uma mensagem que virou a esquerda 
    def viraParaEsquerda(self):
        print("Jegue virou para a Direita")
    # mostrará uma mensagem que acelerou	 
    def acelera(self):  
        print("Jegue acelerou !")
    # mostrará uma mensagem que freiou
    def freia(self):
        print("Jegue freiou!")     
    # mostrará uma mensagem que desligou  
    def desliga(self):
        print("Jegue Desligou!")
    