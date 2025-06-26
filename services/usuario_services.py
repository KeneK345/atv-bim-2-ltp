from models.usuario import Usuario

usuarios = []

usuarios_id = 0


def criar_id_usuario():
    global usuarios_id
    usuarios_id += 1
    return usuarios_id


def criar_usuario(dados):
    global usuarios
    for u in usuarios:
        if u.email == dados["email"]:
            
            return None, "EMAIL_DUPLICADO"
    usuario = Usuario(criar_id_usuario(), dados["nome"], dados["idade"], dados["genero"], dados["email"], dados["senha"])
    usuarios.append(usuario)
    return usuario, None


def listar_usuarios():
    lista = [u.to_dict() for u in usuarios]
    return lista


def buscar_usuario(id):
    for u in usuarios:
        if u.id == id:
            return u, None
    
    return None, "USUARIO_NAO_ENCONTRADO"


def atualizar_usuario(id, novos_dados):
    usuario, erro = buscar_usuario(id)
    if erro:
        return None, erro
   
    for u in usuarios:
        if u.email == novos_dados["email"]:  
            return None, "EMAIL_DUPLICADO"
    
    if usuario:
        usuario.nome = novos_dados.get("nome", usuario.nome)
        usuario.email = novos_dados.get("email", usuario.email)
        usuario.senha = novos_dados.get("senha", usuario.senha)
        usuario.idade = novos_dados.get("idade", usuario.idade)
        usuario.genero = novos_dados.get("genero", usuario.genero)
    return usuario, None


def excluir_usuario(id):
    global usuarios
    usuario, erro = buscar_usuario(id)
    if not usuario:
        
        return False, erro
    usuarios.remove(usuario)
    return True, None