from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DeployForge!"
@app.route("/health")
def health():
    return {"status": "healthy"}
if __name__ == "__main__":
    app.run(debug=True)