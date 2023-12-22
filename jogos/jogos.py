from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from factory.mongo import Database
import time
from helpers import deleta_arquivo
from config import UPLOAD_PATH

jogos_blueprint = Blueprint('jogos', __name__, template_folder='templates')


@jogos_blueprint.route('/')
def inicial():
    return render_template('tela_inicial.html')

@jogos_blueprint.route('/jogos')
def index():
    #alterar isso em todas as funções;
    games_db = Database('games')
    categories_db = Database('categories')
    games = games_db.selectall()
    categories = categories_db.selectall()

    titles = ['Nome', 'Categoria', 'Console', '']
    for game in games:
        for category in categories:
            if game['category'] == category['_id']:
                game['category'] = category['category']
    return render_template('lista.html', titulo='Jogos', titles=titles, games=games)

@jogos_blueprint.route('/novo')
def novo():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect(url_for('login', proxima=url_for('novo')))
    categories_db = Database('categories')
    categories = categories_db.selectall()
    return render_template('novo.html', titulo='Novo Jogo', categories=categories)

@jogos_blueprint.route('/criar', methods=['POST',])
def criar():
    timestamp = time.time()
    filename = f'capa-{timestamp}.jpg'
    arquivo = request.files['arquivo']
    if arquivo.filename == '':
        filename = ''
    else:
        arquivo.save(f'{UPLOAD_PATH}/{filename}')

    data = {
        'title': request.form.get('title'),
        'category': request.form.get('category'),
        'console': request.form.get('console'),
        'cover': filename
    }
    if not data['title'] and not data['category'] and not data['console']:
        return redirect(url_for('jogos.novo',  fields='empty'))
    
    if not data['title']:
        return redirect(url_for('jogos.novo', title='titleempty'))
    
    if data['category'] == None:
        return redirect(url_for('jogos.novo', title='categoryempty'))
    
    if not data['console']:
        return redirect(url_for('jogos.novo', console='consoleempty'))
    
    # Database.insert(data)
    games_db = Database('games')
    games_db.insert(data)

    return redirect(url_for('jogos.index'))

@jogos_blueprint.route('/editar/<string:id>')
def editar(id):
    # game = Database.select(id)
    games_db = Database('games')
    game = games_db.select(id)
    cover = game['cover']
    categories_db = Database('categories')
    categories = categories_db.selectall()

    if not cover:
        cover = 'capa_padrao.jpg'

    return render_template('editar.html', game=game, id=id, capa_jogo=cover, titulo='Editar Jogo', categories=categories)

@jogos_blueprint.route('/jogos/<string:id>', methods=['POST'])
def atualizar(id):
    current_cover = request.form.get('current_cover')
    data = {
        'title': request.form.get('title'),
        'category': request.form.get('category'),
        'console': request.form.get('console'),
        'cover': current_cover,
        '_id': id
    }
    if not data['title'] and not data['category'] and not data['console']:
        return redirect(url_for('jogos.editar', id=id,  fields='empty'))
    
    if not data['title']:
        return redirect(url_for('jogos.editar', id=id, title='titleempty'))
    
    if not data['category']:
        return redirect(url_for('jogos.editar', id=id, category='categoryempty'))
    
    if not data['console']:
        return redirect(url_for('jogos.editar', id=id, console='consoleempty'))
    
    # Database.update(data)
    games_db = Database('games')
    games_db.update(data)

    arquivo = request.files['arquivo']
    if arquivo.filename != '':
        timestamp = time.time()
        filename = f'capa-{timestamp}.jpg'
        data['cover'] = filename

        deleta_arquivo(current_cover)
        arquivo.save(f'{UPLOAD_PATH}/{filename}')

    games_db.update(data)
    return redirect(url_for('jogos.index'))

@jogos_blueprint.route('/deletar/<string:id>')
def deletar(id):
    # Database.delete(id)
    games_db = Database('games')
    games_db.delete(id)
    return redirect(url_for('jogos.index'))


@jogos_blueprint.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)