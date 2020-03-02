"""
Módulo veiculo
Classe IVeiculo
"""
import abc

class IVeiculo(abc.ABC):
	@abc.abstractmethod
	def liga (self):pass # mostrará uma mensagem que ligou o veiculo
	@abc.abstractmethod
	def viraParaDireita(self):pass # mostrará uma mensagem que virou a direita 
	@abc.abstractmethod
	def viraParaEsquerda(self):pass # mostrará uma mensagem que virou a esquerda
	@abc.abstractmethod
	def acelera(self):pass # mostrará uma mensagem que acelerou 
    @abc.abstractmethod 
    def freia(self):pass # mostrará uma mensagem que freiou
    @abc.abstractmethod
    def desliga(self):pass # mostrará uma mensagem que desligou 

