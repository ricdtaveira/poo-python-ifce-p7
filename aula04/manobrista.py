"""
Módulo manobrista
Classe Manobrista
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
        
        
        

        
        
 