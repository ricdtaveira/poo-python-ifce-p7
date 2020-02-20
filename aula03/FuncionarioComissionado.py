"""
Módulo FuncionarioComissionado
Classe EmpregadoComissionado demonstra herança de atributos e métodos de Empregado.
EmpregadoComissionado também demonstra programação por diferença. Ou seja, a classe
filha herda de uma classe mãe(atributos e métodos) e adiciona apenas o código que
a torna diferente da classe mãe.
"""

from Funcionario import Funcionario

class FuncionarioComissionado(Funcionario):

    _comissao = 0.00
    _unidades = 0
    
    def __init__(self, primeiroNome, ultimoNome, salario, comissao):
        super().__init__(primeiroNome, ultimoNome, salario)
        self._comissao = comissao
        
    def calcularPagamento(self):
        return (self._salario + (self._comissao * self._unidades))
    
    def adicionarVendas(self, unidades):
        self._unidades += unidades
        
    def iniciarVendas(self):
        self._unidades = 0
        
        
        
        
        
            