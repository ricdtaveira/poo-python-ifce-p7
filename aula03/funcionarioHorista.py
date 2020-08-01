"""
Módulo FuncionarioHorista
Classe FuncionarioHorista herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioHorista também demonstra programação por diferença.
"""

from funcionario import Funcionario

class FuncionarioHorista(Funcionario):
    
    _horasTrabalhadas = 0
    
    def __init__(self, primeiroNome, ultimoNome, salario):
        super().__init__(primeiroNome, ultimoNome, salario)
    
    def adicionarHoras(self, horas):
        self._horasTrabalhadas += horas
        
    def inicializarHoras(self):
        self._horasTrabalhadas = 0
        
    def calcularPagamento(self):
        return (self._salario * self._horasTrabalhadas)
        