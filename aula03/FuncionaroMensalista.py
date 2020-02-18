"""
Classe FuncionarioMensalista herda Funcionario.
É uma SubClasse de Funcionario.
FuncionarioMensalista também demonstra programação por diferença.
"""

import aula03.Funcionario

class FuncionarioMensalista(aula03.Funcionario):
    
    _faltas = 0
    _valorFaltas = 0.0
    
    def __init__(self, primeiroNome, ultimoNome, salario):
        super().__init__(primeiroNome, ultimoNome, salario)
            
    
    