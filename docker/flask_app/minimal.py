from flask import Flask

app = Flask(__name__)

@app.get("/a")
def hello_world():
    return "<p>Hello, <strong>World!</strong></p>"
