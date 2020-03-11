"""
    Módulo itemnotafiscal -
    Classe ItemNotaFiscal - 
     Atributos :
            id         - informado.
            sequencial - informado.
            quantidade - informado.
            valor      - calculado.            
"""

class ItemNotaFiscal():
    
    _valor = 0.0
    
    def _init_(self, id, sequencial, quantidade):
        self._id=id
        self._sequencial=sequencial
        self._quantidade=quantidade
        
    
if __name__ == '__main__':
    item=ItemNotaFiscal(1, "Jose Maria", 1200, "200.100.345-34", TipoCliente.PESSOA_FISICA)
    print(cliente.str())
        
    

