from preswald.main import start_server
import os

script_path = os.environ.get('SCRIPT_PATH', '/app/hello.py')
port = int(os.environ.get('PORT',8000))

start_server(script=script_path, port=port)