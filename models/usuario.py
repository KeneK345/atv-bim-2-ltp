class Usuario:
    def __init__(self, id, nome, idade, genero, email, senha):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.email = email
        self.senha = senha
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "genero": self.genero,
            "email": self.email
        }