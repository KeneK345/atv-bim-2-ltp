from models.personagem import Personagem

personagens = []
personagens_id = 0


def criar_id_personagem():
    global personagens_id
    personagens_id += 1
    return personagens_id


def criar_personagem(dados):
    
    campos_obrigatorios = ["sapato", "roupa", "corpo", "cabelo", "acessorios", "usuario_id"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return None, "PERSONAGEM_INVALIDO"
    personagem = Personagem(
        id=criar_id_personagem(),
        sapato=dados["sapato"],
        roupa=dados["roupa"],
        corpo=dados["corpo"],
        cabelo=dados["cabelo"],
        acessorios=dados["acessorios"],
        usuario_id=dados["usuario_id"]
    )
    personagens.append(personagem)
    return personagem, None


def listar_personagens():
    return [p.to_dict() for p in personagens]


def buscar_personagem(id):
    for p in personagens:
        if p.id == id:
            return p, None
    return None, "PERSONAGEM_NAO_ENCONTRADO"


def atualizar_personagem(id, novos_dados):
    personagem, erro = buscar_personagem(id)
    if erro:
        return None, erro
    if personagem:
        personagem.sapato = novos_dados.get("sapato", personagem.sapato)
        personagem.roupa = novos_dados.get("roupa", personagem.roupa)
        personagem.corpo = novos_dados.get("corpo", personagem.corpo)
        personagem.cabelo = novos_dados.get("cabelo", personagem.cabelo)
        personagem.acessorios = novos_dados.get("acessorios", personagem.acessorios)
    return personagem, None


def excluir_personagem(id):
    global personagens
    personagem, erro = buscar_personagem(id)
    if not personagem:
        return False, erro
    personagens.remove(personagem)
    return True, None
