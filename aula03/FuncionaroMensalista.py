"""
Classe FuncionarioMensalista herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioMensalista também demonstra programação por diferença.
"""

import aula03.Funcionario

class FuncionarioMensalista(aula03.Funcionario):
    
    _faltas = 0
    _valorFalta = 0.0
    
    def __init__(self, primeiroNome, ultimoNome, salario, valorFalta):
        super().__init__(primeiroNome, ultimoNome, salario)
        self.valorFalta = valorFalta
    
    def calcularPagamento(self):
        return (self._salario - (self._faltas * self._valorFalta))
    
    def adicionafFaltas(self, faltas):
        self.faltas += faltas
        
    def inicializarFaltas(self):
        self.faltas=0
            
    
    