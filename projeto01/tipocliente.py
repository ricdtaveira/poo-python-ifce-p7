""" 
    Modulo tipocliente -
    Classe TipoCliente - Enumeration de Tipos de Cliente
"""

import enum
 
class TipoCliente(enum.Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2
     
    