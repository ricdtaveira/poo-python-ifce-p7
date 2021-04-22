class Aluno:

# Método Construtor
# Instancia na memória um objeto da classe Aluno
    def __init__(self, matricula, nome, endereco):
        self.matricula = matricula
        self.nome = nome
        self.endereco = endereco
        self.disciplinas=[]

# Métodos Acessores
# Retorna por exemplo o valor de
# um atributo
    def get_matricula(self):
        return self.matricula
    
    def get_nome(self):
        return self.nome
    
    def get_endereco(self):
        return self.endereco
    
    def get_disciplinas(self):
        return self.disciplinas

# Metodos Modificadores
# Altera o valor de um atribuo de um Objeto

    def set_matricula(self, matricula):
        self.matricula = matricula
        
    def set_nome(self, nome):
        self.nome = nome
        
    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def toString(self):
        return (str(self.matricula) + " " + self.nome + " " + self.endereco)

    def printSelf(self):
        print("Valor de self=" + str(self))
        return
    
    
    
        
