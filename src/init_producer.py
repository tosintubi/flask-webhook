

from flask import Flask

app = Flask(__name__)


# Load Flask configuration from config file
app.secret_key = app.config.get['SECRET_KEY']
app.config.from_object('config')
