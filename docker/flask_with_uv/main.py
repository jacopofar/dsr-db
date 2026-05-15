from flask import Flask
import numpy as np

app = Flask(__name__)

@app.get("/random")
def random():
    return f"Random number: {np.random.random()}"

