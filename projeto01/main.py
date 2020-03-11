"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.   
"""
from produto        import Produto
from cliente        import Cliente
from notafiscal     import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from tipocliente    import TipoCliente


def main():
    p1=Produto(1, "arroz01", "Arroz de Goiás", 5.00)
    print(p1.str())

if __name__ == '__main__':
    main()
    

