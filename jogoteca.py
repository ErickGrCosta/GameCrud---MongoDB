from flask import Flask

from jogos.jogos import jogos_blueprint
from categorias.categorias import categorias_blueprint

# from flask_wtf.csrf import CSRFProtect
# from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.register_blueprint(jogos_blueprint)
app.register_blueprint(categorias_blueprint)

app.config.from_pyfile('config.py')

# csrf = CSRFProtect(app)
# bcrypt = Bcrypt(app)

# from categorias.categorias import *
# from jogos.jogos import * 

if __name__ == '__main__':
    app.run(debug=True)