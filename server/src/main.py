import sys
from src.config.flask_config import app, init_api


def start_flask_app(fs_storage: bool = True):
    print(f"Input argv: ${str(sys.argv)}")
    print(f"Input argv: ${str(sys.argv)}")
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(f" * App swagger will be available at: http://127.0.0.1:${port}/swagger")
    init_api(fs_storage)
    app.run(host="0.0.0.0", debug=False, port=port)


if __name__ == '__main__':
    start_flask_app()
