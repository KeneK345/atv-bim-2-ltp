from flask import Flask
from routes.usuarios_routes import usuarios_bp
from routes.atividade_routes import atividades_bp

app = Flask(__name__)
app.register_blueprint(usuarios_bp)


if __name__ == "__main__":
    app.run(debug=True)