from models.atividade import Atividade

atividades = []
atividades_id = 0


def criar_id_atividade():
    global atividades_id
    atividades_id += 1
    return atividades_id


def criar_atividade(dados):
    campos_obrigatorios = ["tentativas", "erros", "dificuldade", "horario"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return None, "ATIVIDADE_INVALIDA"
    atividade = Atividade(
        id=criar_id_atividade(),
        tentativas=dados["tentativas"],
        erros=dados["erros"],
        dificuldade=dados["dificuldade"],
        horario=dados["horario"]
    )
    atividades.append(atividade)
    return atividade, None


def listar_atividades():
    return [a.to_dict() for a in atividades]


def buscar_atividade(id):
    for a in atividades:
        if a.id == id:
            return a, None
    return None, "ATIVIDADE_NAO_ENCONTRADA"


def atualizar_atividade(id, novos_dados):
    atividade, erro = buscar_atividade(id)
    if erro:
        return None, erro
    if atividade:
        atividade.tentativas = novos_dados.get("tentativas", atividade.tentativas)
        atividade.erros = novos_dados.get("erros", atividade.erros)
        atividade.dificuldade = novos_dados.get("dificuldade", atividade.dificuldade)
        atividade.horario = novos_dados.get("horario", atividade.horario)
    return atividade, None


def excluir_atividade(id):
    global atividades
    atividade, erro = buscar_atividade(id)
    if not atividade:
        return False, erro
    atividades.remove(atividade)
    return True, None