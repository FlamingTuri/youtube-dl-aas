import sys
from src.config.flask_config import app, init_api

def get_argv_param(key: str, default_value: str = None) -> str:
    value = next(filter(lambda arg: key in arg, sys.argv), default_value)
    return value if value == None else value.removeprefix(key)

def start_flask_app(fs_storage: bool = True):
    print(f"Input argv: ${str(sys.argv)}")
    port=int(get_argv_param('--port=', '5000'))
    ssl_context=get_argv_param('--ssl_context=', None)
    print(f" * App swagger will be available at: http://127.0.0.1:${port}/swagger")
    init_api(fs_storage)
    app.run(host="0.0.0.0", debug=False, port=port, ssl_context=ssl_context)


if __name__ == '__main__':
    start_flask_app()
