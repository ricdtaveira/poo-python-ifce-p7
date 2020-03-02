"""
Módulo main
"""
from manobrista import Manobrista 
from fusca   import Fusca 
from jegue   import Jegue
from aviao   import Aviao
 
v1 = Fusca()
v2 = Aviao()
v3 = Jegue()
mano = Manobrista()
mano.estaciona(v1)
mano.estaciona(v2)
mano.estaciona(v3) 
    