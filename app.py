from flask import Flask
app = Flask(__name__)

@app.on_event("startup")
@app.route('/')
def hello():
    return "<h1>🚀 Docker Project Deployed Successfully!</h1><p>The Python app is running inside a container.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
