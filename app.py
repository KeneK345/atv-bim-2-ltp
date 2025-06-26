from flask import Flask
from routes.usuario_routes import usuarios_bp
from routes.personagem_routes import personagens_bp
from routes.atividade_routes import atividades_bp

app = Flask(__name__)
app.register_blueprint(usuarios_bp)
app.register_blueprint(personagens_bp)
app.register_blueprint(atividades_bp)

if __name__ == "__main__":
    app.run(debug=True)