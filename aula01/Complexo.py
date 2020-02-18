'''
Classe Complexo
'''
class Complexo:
    # Método Construtor
    def __init__(self):
        self.r = 0.0
        self.i = 0.0
        
    # Método Modificador
    def set_i(self, i):
        self.i = i
        
    # Método Acessor
    def get_i(self):
        return self.i
    
    def set_r(self, r):
        self.r = r
        
    def get_r(self):
        return self.r
        
x = Complexo()
x.set_i(-2.0)
x.set_r(5.0)

print(x.get_r, x.get_i)