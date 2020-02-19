
  
from . import FuncionarioComissionado  
from . import FuncionarioMensalista  
from . import FuncionarioHorista

c_emp = FuncionarioComissionado("José", "Almeida", 2000.00, 10.0)
m_emp = FuncionarioMensalista()
h_emp = FuncionarioHorista()

print (c_emp.calcularPagamento())