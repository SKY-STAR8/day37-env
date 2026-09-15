from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello SK! Welcome to Day 59 Multi-Container CI/CD Project</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
