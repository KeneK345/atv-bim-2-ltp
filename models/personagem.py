class Personagem:
    def __init__(self, id, sapato, roupa, corpo, cabelo, acessorios, usuario_id):
        self.id = id
        self.sapato = sapato
        self.roupa = roupa
        self.corpo = corpo
        self.cabelo = cabelo
        self.acessorios = acessorios
        self.usuario_id = usuario_id

    def to_dict(self):
        return {
            "id": self.id,
            "sapato": self.sapato,
            "roupa": self.roupa,
            "corpo": self.corpo,
            "cabelo": self.cabelo,
            "acessorios": self.acessorios,
            "usuario_id": self.usuario_id,
        }
