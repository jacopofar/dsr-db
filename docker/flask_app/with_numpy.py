from flask import Flask
import numpy as np

app = Flask(__name__)

@app.get("/a")
def hello_world():
    return "Hello world"

@app.get("/random")
def random():
    return f"Random number: {np.random.random()}"