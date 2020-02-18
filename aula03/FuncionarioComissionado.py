"""
Classe FuncionarioComissionado herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioComissionado também demonstra programação por diferença.
"""

import aula03.Funcionario

class FuncionarioComissionado(aula03.Funcionario):
    
    _faltas = 0
    _valorFaltas = 0.0
    
    def __init__(self, primeiroNome, ultimoNome, salario):
        super().__init__(primeiroNome, ultimoNome, salario)
            