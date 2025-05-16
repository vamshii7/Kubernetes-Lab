from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    env = os.getenv("APP_ENV", "development")
    secret = os.getenv("SECRET_KEY", "no-secret")
    return render_template("index.html", env=env, secret=secret)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
