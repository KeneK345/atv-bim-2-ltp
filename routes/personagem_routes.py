from flask import Blueprint, request, jsonify
from services.personagem_services import *
from utils.mensagens_erro import ERROS

# registrando rota no blueprint
personagens_bp = Blueprint("personagens", __name__)

# criar_personagem(dados) de serviços
@personagens_bp.route("/personagens", methods=["POST"])
def create_personagem():
    dados = request.json
    personagem, erro = criar_personagem(dados)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(personagem.to_dict()), 201

# listar_personagens() de serviços
@personagens_bp.route("/personagens", methods=["GET"])
def list_personagens():
    return jsonify(listar_personagens()), 200

# buscar_personagem(id) de serviços
@personagens_bp.route("/personagens/<int:id>", methods=["GET"])
def search_personagem(id):
    personagem, erro = buscar_personagem(id)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(personagem.to_dict()), 200

# atualizar_personagem(id, dados) de serviços
@personagens_bp.route("/personagens/<int:id>", methods=["PUT"])
def update_personagem(id):
    dados = request.json
    personagem, erro = atualizar_personagem(id, dados)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(personagem.to_dict()), 200

# excluir_personagem(id) de serviços
@personagens_bp.route("/personagens/<int:id>", methods=["DELETE"])
def delete_personagem(id):
    sucesso, erro = excluir_personagem(id)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return "", 204