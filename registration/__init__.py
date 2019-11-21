from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a641063612fd4d95'
bootstrap = Bootstrap(app)

from registration import routes