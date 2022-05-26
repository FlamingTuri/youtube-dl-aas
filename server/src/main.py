from src.config.flask_config import app, init_api


def start_flask_app(fs_storage: bool = True):
    print(" * App swagger will be available at: http://127.0.0.1:5000/swagger")
    init_api(fs_storage)
    app.run(host="0.0.0.0", debug=False)


if __name__ == '__main__':
    start_flask_app()
