from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from factory.mongo import Database
# from helpers import deleta_arquivo

categorias_blueprint = Blueprint('categorias', __name__, template_folder='templates')

@categorias_blueprint.route('/categories')
def indexcategories():
    # categories = Category.selectall()
    categories_db = Database('categories')
    categories = categories_db.selectall()
    titles = ['Categorias', '']
    return render_template('lista_categoria.html', titulo='Categorias', titles=titles, games=categories)

@categorias_blueprint.route('/categoria')
def categoria():
    return render_template('categoria.html', titulo='Nova categoria')

@categorias_blueprint.route('/novo', methods=['POST',])
def criarcategoria():

    data = {
        'category': request.form.get('category')
    }

    if not data['category']:
        return redirect(url_for('categoria', title='categoryempty'))
    
    # Category.insert(data)
    categories_db = Database('categories')
    categories_db.insert(data)
    return redirect(url_for('categorias.indexcategories'))

@categorias_blueprint.route('/editarcateg/<string:id>')
def editarcategoria(id):
    # categories = Category.select(id)
    categories_db = Database('categories')
    categories = categories_db.select(id)
    return render_template('editar_categoria.html',id=id, titulo='Editar Categoria', categories=categories)

@categorias_blueprint.route('/editarcateg/<string:id>', methods=['POST'])
def atualizarcategoria(id):
    data = {
        'category': request.form.get('category'),
        '_id': id
    }
    if not data['category']:
        return redirect(url_for('editar', id=id, category='categoryempty'))

    # Category.update(data)
    categories_db = Database('categories')
    categories_db.update(data)
    return redirect(url_for('categorias.indexcategories'))

@categorias_blueprint.route('/deletarcategory/<string:id>')
def deletarcategory(id):
    # Category.delete(id)
    categories_db = Database('categories')
    categories_db.delete(id)
    
    return redirect(url_for('categorias.indexcategories'))