"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
from cliente        import Cliente
from itemnotafiscal import ItemNotaFiscal
from produto        import Produto

class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=Cliente()        
        self._itens=[]
        self._valorNota=0.0        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor =+ item.produto._valorUnitario
        self.valorNota=valor
        
    def imprimirNotaFiscal(self):
        pass
    
    
        
        