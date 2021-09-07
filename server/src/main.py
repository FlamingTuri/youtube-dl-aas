from src.config.flask_config import app


def start_flask_app():
    app.run(host="0.0.0.0", debug=False)


if __name__ == '__main__':
    start_flask_app()
