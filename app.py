from flask import Flask
from flask_cors import CORS
from src.word_count.views import home, word_count

# initialization
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(home)
    app.register_blueprint(word_count)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)