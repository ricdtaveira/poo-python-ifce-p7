"""
Módulo main.py - tem a função principal que executa as funcionalidades
                nas classes da hierarquia de Herança
"""

from aula03.funcionarioComissionado import FuncionarioComissionado
from aula03.funcionarioHorista import FuncionarioHorista
from aula03.funcionarioMensalista import FuncionarioMensalista

def main():
    c_emp = FuncionarioComissionado("José", "Almeida", 2000.00, 10.0)
    m_emp = FuncionarioMensalista("Maria", "Saraiva", 2000.00, 100.00)
    h_emp = FuncionarioHorista("Pedro", "Alcantara",  )

    print ("Comissionado: " + c_emp.calcularPagamento())
    print ("Mensalista: " + m_emp.calcularPagamento())
    print ("Horista: " + h_emp.calcularPagamento())
    
    
if __name__ == '__main__':
    main()