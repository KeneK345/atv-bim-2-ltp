class Atividade:
    def __init__(self, id, tentativas, dificuldade, horario, erros):
        self.id = id
        self.tentativas = tentativas
        self.dificuldade = dificuldade
        self.horario = horario
        self.erros = erros
    
    def to_dict(self):
        return {
            "id": self.id,
            "tentativas": self.tentativas,
            "dificuldade": self.dificuldade,
            "horario": self.horario,
            "erros": self.erros
        }