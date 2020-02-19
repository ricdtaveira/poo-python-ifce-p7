"""
Módulo main.py - tem a função principal que executa as funcionalidades
                nas classes da hierarquia de Herança
"""

from aula03.FuncionarioComissionado import FuncionarioComissionado
from aula03.FuncionarioHorista import FuncionarioHorista
from aula03.FuncionarioMensalista import FuncionarioMensalista


def main():
    c_emp = FuncionarioComissionado("José", "Almeida", 2000.00, 10)
    m_emp = FuncionarioMensalista("Maria", "Saraiva", 2000.00, 100.00)
    h_emp = FuncionarioHorista("Pedro", "Alcantara", 20.00)

    print("Comissionado: " + str(c_emp.calcularPagamento()))
    print("Mensalista: " + str(m_emp.calcularPagamento()))
    h_emp.adicionarHoras(160)
    print("Horista: " + str(h_emp.calcularPagamento()))

    print(c_emp.imprimirCheckPagamento())
    print(m_emp.imprimirCheckPagamento())
    print(h_emp.imprimirCheckPagamento())


if __name__ == '__main__':
    main()
