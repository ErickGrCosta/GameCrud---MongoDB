import os
from config import UPLOAD_PATH
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, PasswordField, validators

def recupera_imagem(id):
    for nome_arquivo in os.listdir(UPLOAD_PATH):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
        
    return 'capa_padrao.jpg'
    
def deleta_arquivo(filename):
    if filename == 'capa_padrao.jpg':
        return 
    file_path = os.path.join(UPLOAD_PATH, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    