from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    app_env = os.getenv('app', 'dev')
    port = os.getenv('port', '5000')
    return f"<h1>Welcome to the {app_env} environment on port {port}</h1>"

@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("port", 5000)))