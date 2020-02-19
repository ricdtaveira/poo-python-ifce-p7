"""
 Funcionario é uma classe abstrata (Abstract Base Class). Todos os empregados tem um 
 primeiro_nome,  ultimo_nome, e um salário. 
 Cada empregado pode calcular o seu salario. 
 Todavia, o mecanismo  para calcular o salário depende do tipo de empregado. 
 Assim, cada subtipo deve definir, o modo como calcular o seu salário.
"""
# Definição de uma Classe Abstrata - (Abstract Base Class).
import abc
class Funcionario(abc.ABC):
    # Método Construtor
    # Atributos Privados
    def __init__(self, primeiroNome, ultimoNome, salario):
        self._primeiroNome = primeiroNome
        self._ultimoNome = ultimoNome
        self._salario = salario
    
    # Método Acessor retorna _primeiroNome           
    def get_primeiroNome(self):
        return self._primeiroNome
    
    # Método Acessor retorna _ultimoNome 
    def get_ultimoNome(self):
        return self._ultimoNome
    
    # Método Acessor retorna _salario 
    def get_salario(self):
        return self._salario
    
    # Método Modificador altera  _primeiroNome    
    def set_primeiroNome(self, primeiroNome):
        self._primeiroNome=primeiroNome
    
    # Método Modificador altera  _ultimoNome   
    def set_ultimoNome(self, ultimoNome):
        self._ultimoNome=ultimoNome
        
    # Método Modificador altera  _salario    
    def set_salario(self, salario):
        self._salario=salario
        
        
    # Definição de um Método Abstrato.
    # O Método Abstrato será reescrito na SubClasse
    @abc.abstractmethod    
    def calcularPagamento(self):
        pass
    
    def imprimirCheckPagamento(self):
        nomeCompleto = self._ultimoNome + ", " + self._primeiroNome
        return ("Pagamento= " +  nomeCompleto + " R$ " + str(self.calcularPagamento()))