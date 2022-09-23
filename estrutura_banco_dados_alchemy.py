from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar uma API flask
app = Flask(__name__) # recebe o nome da app ('estrutura_banco_dados_alchemy)
# Criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = 'Hermes82wars!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # connection string

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir a estrutura da tabela autores
# id, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autores'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem') # passa o nome da classe e não da tabela

# Definir a estrutura da tabela de Postagem
# ID, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagens'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autores.id_autor'))

def inicializar_banco():
    # Executar o comando para criar o banco de dados
    db.drop_all()
    db.create_all()
    # Criar os administradores
    autor = Autor(nome='Fernando', email='fernandoperesvalverde@gmail.com', senha='Hermes82wars!', admin=True)
    db.session.add(autor)
    db.session.commit()

postagem = Postagem(titulo='Uma nova postagem', id_autor=1)
db.session.add(postagem)
db.session.commit()


if __name__ == "__main__":
    inicializar_banco()
