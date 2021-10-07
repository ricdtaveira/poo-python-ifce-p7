"""
Módulo main.py - tem a função principal que executa as funcionalidades
                nas classes da hierarquia de Herança
"""

from funcionarioComissionado import FuncionarioComissionado
from funcionarioHorista      import FuncionarioHorista
from funcionarioMensalista   import FuncionarioMensalista

def main():
    c_emp = FuncionarioComissionado("José", "Almeida", 2000.00, 10.0)
    m_emp = FuncionarioMensalista("Maria", "Saraiva", 2000.00, 100.00)
    h_emp = FuncionarioHorista("Pedro", "Alcantara", 50.0)
    
    h_emp.adicionarHoras(160)
    m_emp.adicionarFaltas(10)
    c_emp.adicionarVendas(10)
    
    print ("Comissionado: " + str(c_emp.calcularPagamento()))
    print ("Mensalista: " + str(m_emp.calcularPagamento()))
    print ("Horista: " + str(h_emp.calcularPagamento()))

if __name__ == '__main__':
    main()