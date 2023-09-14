"""Módulo iniciador da aplicação Flask."""


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

from .config import Config

from .db import create_user, find_user, verify_user


# Criar uma função para criar a instância da aplicação
def create_app(config_class=Config):
    """
    Cria e configura uma instância da aplicação Flask.

    :param config_class: Classe de configuração da aplicação.
    :type config_class: class

    :return: Instância da aplicação Flask.
    :rtype: Flask

    Exemplo de uso:

    >>> create_app(config_class=Config)  
    <Flask 'tools'>
    """
    app = Flask(__name__)

    # Configurar as configurações globais da aplicação
    app.config.from_object(config_class)

    # Configurar conexão com o Redis para armazenamento em cache
    redis = Redis.from_url(app.config['REDIS_URL'])

    # Configurar conexão com o MongoDB usando
    # as informações do arquivo de configuração
    client = MongoClient(app.config['MONGODB_SETTINGS']['host'])

    # Selecionar o banco de dados padrão (no caso, 'Cluster0')
    db = client.get_default_database('Cluster0')

    # Rotas da aplicação e outras lógicas de negócio

    @app.route('/')
    def index():
        """
        Exibe a página inicial.
    
        Exemplos de teste:
    
        >>> index()
        200 OK
        >>> request.path = '/invalid-path'
        >>> index()
        404 Not Found
        """
        return render_template('index.html')

    @app.route('/test-redis')
    def test_redis():
        """
        Testa a conexão com o Redis.
    
        Exemplos de teste:
    
        >>> test_redis()
        'Conexão com o Redis bem-sucedida!'
        >>> redis = None
        >>> test_redis()
        'Erro na conexão com o Redis: NoneType object has no attribute "ping"'
        """
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
        """
        Testa a conexão com o MongoDB.

        Exemplos de teste:

        >>> test_mongodb()
        ['test_collection']
        >>> db = None
        >>> test_mongodb()
        'Erro na conexão com o MongoDB: NoneType object has no attribute "list_collection_names"'
        """
        try:
            # Testar conexão com o MongoDB
            collections = db.list_collection_names()
            flash('Conexão com o MongoDB bem-sucedida!', 'success')
        except Exception as e:
            error_message = f'Erro na conexão com o MongoDB: {str(e)}'
            flash(error_message, 'danger')
        return redirect(url_for('index'))

    return app
