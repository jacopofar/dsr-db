import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = np.random.random(12)
    return str(np.median(a))