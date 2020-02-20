"""
Módulo FuncionarioMensalista.
Classe FuncionarioMensalista herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioMensalista também demonstra programação por diferença.
"""

from Funcionario import Funcionario

class FuncionarioMensalista(Funcionario):
    
    _faltas = 0
    _valorFalta = 0.0
    
    def __init__(self, primeiroNome, ultimoNome, salario, valorFalta):
        super().__init__(primeiroNome, ultimoNome, salario)
        self._valorFalta = valorFalta
    
    def calcularPagamento(self):
        return (self._salario - (self._faltas * self._valorFalta))
    
    def adicionarFaltas(self, faltas):
        self._faltas += faltas
        
    def inicializarFaltas(self):
        self._faltas=0
            
    
    