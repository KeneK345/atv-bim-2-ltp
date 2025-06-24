from models.usuario import Usuario

usuarios = []
# controla os ids dos usuarios
usuarios_id = 0

# atualiza ids
def criar_id():
    global usuarios_id
    usuarios_id += 1
    return usuarios_id

# cria um usuário
# usa um array com dados para criar um objeto Usuário como parâmetros
def criar_usuario(dados):
    global usuarios
    # checando se já existe um usuário com o email em dados
    for u in usuarios:
        if u.email == dados["email"]:
            # mensagem de erro, ainda não implementado
            return None, "EMAIL_DUPLICADO"
    usuario = Usuario(criar_id(), dados["nome"], dados["email"], dados["senha"])
    usuarios.append(usuario)
    return usuario, None

# apresenta todos os usuários presentes no sistema
def listar_usuarios():
    lista = [u.to_dict() for u in usuarios]
    return lista

# procura por um usuário específico com o seu id
def buscar_usuario(id):
    for u in usuarios:
        if u.id == id:
            return u, None
    # mensagem de erro, ainda não implementado
    return None, "USUARIO_NAO_ENCONTRADO"

# muda os dados de um usuário
def atualizar_usuario(id, novos_dados):
    usuario, erro = buscar_usuario(id)
    # mensagens de erro ainda não implementadas
    if erro:
        return None, erro
    # checando se já existe um usuário com o email em novos_dados
    for u in usuarios:
        if u.email == novos_dados["email"]:
            # mensagem de erro, ainda não implementado
            return None, "EMAIL_DUPLICADO"
    # passando os novos dados para o usuário
    if usuario:
        usuario.nome = novos_dados.get("nome", usuario.nome)
        usuario.email = novos_dados.get("email", usuario.email)
        usuario.senha = novos_dados.get("senha", usuario.senha)
    return usuario

# exclui um usuário
def excluir_usuario(id):
    global usuarios
    usuario, erro = buscar_usuario(id)
    if not usuario:
        # mensagem de erro, ainda não implementado
        return False, erro
    usuarios.remove(usuario)
    return True, None