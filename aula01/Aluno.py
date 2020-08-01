class Aluno:
     
    def __init__(self, matricula, nome, endereco):
        self.matricula = matricula
        self.nome = nome
        self.endereco = endereco
        self.disciplinas=[]
       
    def get_matricula(self):
        return self.matricula
    
    def get_nome(self):
        return self.nome
    
    def get_endereco(self):
        return self.endereco
    
    def get_disciplinas(self):
        return self.disciplinas

    def set_matricula(self, matricula):
        self.matricula = matricula
        
    def set_nome(self, nome):
        self.nome = nome
        
    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def toString(self):         
        return (str(self.matricula) + " " + self.nome + " " + self.endereco)
    
    
    
        
