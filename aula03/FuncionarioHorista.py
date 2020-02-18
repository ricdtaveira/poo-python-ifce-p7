"""
Classe FuncionarioHorista herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioHorista também demonstra programação por diferença.
"""

import aula03.Funcionario

class FuncionarioHorista(aula03.Funcionario):
    
    _horasTrabalhadas = 0
    
    def __init__(self, primeiroNome, ultimoNome, salario):
        super().__init__(primeiroNome, ultimoNome, salario)
    
    def addHoras(self, horas):
        self._horasTrabalhadas += horas
        
    def inicializarHoras(self):
        self._horasTrabalhadas = 0
        