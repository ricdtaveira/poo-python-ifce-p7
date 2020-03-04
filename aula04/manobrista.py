"""
Módulo manobrista
Classe Manobrista
       No método estaciona há um exemplo de polimorfismo. É recebido como parametro uma 
       implementação de um Veiculo que é manobrado pelos métodos da implementação de 
       sua interface.
"""

from veiculo import IVeiculo

class Manobrista():    
    def estaciona(self, v):         
        v.liga()
        v.acelera()
        v.viraParaDireita()
        v.viraParaEsquerda()
        v.freia()
        v.desliga()
        