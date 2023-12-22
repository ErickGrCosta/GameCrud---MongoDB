# from jogoteca import app
# from flask import render_template, request, redirect, session, flash, url_for
# from flask_bcrypt import check_password_hash


# @app.route('/login')
# def login():
#     proxima = request.args.get('proxima')
#     form = FormularioUsuario()
#     return render_template('login.html', proxima=proxima, form=form)

# @app.route('/autenticar', methods=['POST',])
# def autenticar():
    
    # pass
    # if usuario and senha:
        
    #     return redirect(proxima_pagina)
    # else:
    #     flash('Usuário não logado.')
    #     return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session['usuario_logado'] = None
#     flash('Logout efetuado com sucesso!')
#     return redirect(url_for('login'))