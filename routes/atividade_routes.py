from flask import Blueprint, request, jsonify
from services.atividade_services import *
from utils.mensagens_erro import ERROS

# registrando rota no blueprint
atividades_bp = Blueprint("atividades", __name__)

# criar_atividade(dados) de serviços
@atividades_bp.route("/atividades", methods=["POST"])
def create_atividade():
    dados = request.json
    atividade, erro = criar_atividade(dados)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(atividade.to_dict()), 201

# listar_atividades() de serviços
@atividades_bp.route("/atividades", methods=["GET"])
def list_atividades():
    return jsonify(listar_atividades()), 200

# buscar_atividade(id) de serviços
@atividades_bp.route("/atividades/<int:id>", methods=["GET"])
def search_atividade(id):
    atividade, erro = buscar_atividade(id)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(atividade.to_dict()), 200

# atualizar_atividade(id, dados) de serviços
@atividades_bp.route("/atividades/<int:id>", methods=["PUT"])
def update_atividade(id):
    dados = request.json
    atividade, erro = atualizar_atividade(id, dados)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return jsonify(atividade.to_dict()), 200

# excluir_atividade(id) de serviços
@atividades_bp.route("/atividades/<int:id>", methods=["DELETE"])
def delete_atividade(id):
    sucesso, erro = excluir_atividade(id)
    if erro:
        erro_info = ERROS.get(erro, {"mensagem": "Erro desconhecido", "status": 500})
        return jsonify({"mensagem": erro_info["mensagem"]}), erro_info["status"]
    return "", 204