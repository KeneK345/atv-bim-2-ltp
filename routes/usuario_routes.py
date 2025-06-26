from flask import Blueprint, request, jsonify
from services.usuario_services import *
from utils.mensagens_erro import ERROS

# registrando rota no blueprint
usuarios_bp = Blueprint("usuarios", __name__)

# criar_usuario(dados) de serviços
@usuarios_bp.route("/usuarios", methods=["POST"])
def create_user():
    dados = request.json
    usuario, erro = criar_usuario(dados)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(usuario.to_dict()), 201

# listar_usuarios() de serviços
@usuarios_bp.route("/usuarios", methods=["GET"])
def list_users():
    return jsonify(listar_usuarios()), 200

# buscar_usuario(id) de serviços
@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def search_user(id):
    usuario, erro = buscar_usuario(id)

    if erro:
        erro_info = ERROS[erro]
        return jsonify({"mensagem": erro_info["mensagem"]})
    return jsonify(usuario.to_dict()), 200

# atualizar_usuario(id, dados) de serviços
@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def update_user(id):
    dados = request.json
    usuario, erro = atualizar_usuario(id, dados)

    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(usuario.to_dict()), 200

# excluir_usuario(id) de serviços
@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_user(id):
    sucesso, erro = excluir_usuario(id)

    if erro:
        erro_info = ERROS[erro]
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return "", 204