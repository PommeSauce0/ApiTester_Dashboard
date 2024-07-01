from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '63e34e3e00fed106c2aef6f6dcac624f'
MONGO_HOST = "mongodb://localhost:27017/"

from . import routes, functions
