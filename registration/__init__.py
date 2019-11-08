from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ffe2e8db1de097bf0d709a1bbab1e647'

from registration import routes