"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""
from produto import Produto

class ItemNotaFiscal():
    
    _valor = 0.0
    _produto = Produto()
    
    def _init_(self, id, sequencial, quantidade, produto):
        self._id=id
        self._sequencial=sequencial
        self._quantidade=quantidade
        self._produto=produto
             
    def str(self):
        string="\nId={3} Sequencial={2} Quantidade={1} Produto={0}".format(self._produto.getDescricao(), self._quantidade, self._sequencial, self._id)
        return string
    
        
if __name__ == '__main__':
    produto=Produto(1,100,'Arroz', 5.5) 
    item=ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())
        
    

