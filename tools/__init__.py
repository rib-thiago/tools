"""
Módulo de inicialização para o pacote 'tools'.

Este módulo contém funções de inicialização e configuração para o pacote 'tools'.

Exemplos de uso:

>>> from tools import create_app
>>> app = create_app()
"""
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from pymongo import MongoClient
from redis import Redis

from config import Config

from .db import create_user, find_user, verify_user


# Criar uma função para criar a instância da aplicação
def create_app(config_class=Config):
    """
    Cria uma instância da aplicação Flask com base na classe de configuração fornecida.

    Args:
        config_class (class): A classe de configuração a ser usada para configurar a aplicação.

    Returns:
        Flask: A instância da aplicação Flask configurada.

    Exemplos de uso:

    >>> from tools import create_app
    >>> app = create_app()
    >>> app.config['SECRET_KEY']
    '9so3jYZSbrbvPqGoxYpO5i4fqj+mwX9UA29iuk+jhVkmaWpuyVoAV7xlaz4UI+56rK61fSW1AF/Qz/DF'
    """
    app = Flask(__name__)

    # Configurar as configurações globais da aplicação
    app.config.from_object(config_class)

    # Configurar conexão com o Redis para armazenamento em cache
    redis = Redis.from_url(app.config['REDIS_URL'])

    # Configurar conexão com o MongoDB usando as informações do arquivo de configuração
    client = MongoClient(app.config['MONGODB_SETTINGS']['host'])

    # Selecionar o banco de dados padrão (no caso, 'Cluster0')
    db = client.get_default_database('Cluster0')

    # Rotas da aplicação e outras lógicas de negócio

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/test-redis')
    def test_redis():
        try:
            # Testar conexão com o Redis
            redis.ping()
            flash('Conexão com o Redis bem-sucedida!', 'success')
        except Exception as e:
            error_message = f'Erro na conexão com o Redis: {str(e)}'
            flash(error_message, 'danger')
        return redirect(url_for('index'))

    @app.route('/test-mongodb')
    def test_mongodb():
        try:
            # Testar conexão com o MongoDB
            collections = db.list_collection_names()
            flash('Conexão com o MongoDB bem-sucedida!', 'success')
        except Exception as e:
            error_message = f'Erro na conexão com o MongoDB: {str(e)}'
            flash(error_message, 'danger')
        return redirect(url_for('index'))

    return app
