from bson.objectid import ObjectId
from flask import current_app, g
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash


def get_db():
    """
    Retorna o banco de dados do MongoDB.

    :return: Banco de dados do MongoDB.
    :rtype: MongoClient

    Exemplo de uso:

    >>> db = get_db()
    >>> db
    <pymongo.database.Database object at 0x1234567890>
    """
    if 'db' not in g:
        client = MongoClient(current_app.config['MONGODB_SETTINGS']['host'])
        g.db = client.get_database('Cluster0')
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.client.close()


def init_db():
    """
    Cria o banco de dados e a coleção de usuários.

    Exemplo de uso:

    >>> init_db()
    """
    db = get_db()

    if 'users' not in db.list_collection_names():
        db.create_collection('users')
        users_collection = db['users']

        user_data = {
            'username': 'exemplo',
            'password': 'senha_de_exemplo',
        }
        users_collection.insert_one(user_data)


def find_user(username):
    """
    Retorna o usuário do MongoDB com o nome especificado.

    :param username: Nome do usuário.
    :type username: str

    :return: Usuário do MongoDB.
    :rtype: dict

    Exemplo de uso:

    >>> find_user('exemplo')
    {'username': 'exemplo', 'password': 'senha_de_exemplo'}
    """
    db = get_db()
    users_collection = db['users']
    return users_collection.find_one({'username': username})


def find_password(password):
    """
    Retorna o usuário do MongoDB com a senha especificada.

    :param password: Senha do usuário.
    :type password: str

    :return: Usuário do MongoDB.
    :rtype: dict

    Exemplo de uso:

    >>> find_password('senha_de_exemplo')
    {'username': 'exemplo', 'password': 'senha_de_exemplo'}
    """
    db = get_db()
    users_collection = db['users']
    return users_collection.find_one({'password': password})


with app.app_context():
    def create_user(username, password):
        """
        Cria um novo usuário no banco de dados do MongoDB.
    
        :param username: Nome do usuário.
        :type username: str
        :param password: Senha do usuário.
        :type password: str
    
        :return: True se o usuário foi criado, False caso contrário.
        :rtype: bool
    
        Exemplo de uso:
        >>> create_user('exemplo2', 'senha_de_exemplo2')
        True
        """
        db = get_db()
        users_collection = db['users']
        if find_user(username) is None:
            users_collection.insert_one(
                {'username': username, 'password': password}
            )
            return True
        return False


def verify_user(username, password):
    """
    Verifica se o usuário existe e se a senha está correta.

    :param username: Nome do usuário.
    :type username: str
    :param password: Senha do usuário.
    :type password: str

    :return: Tupla com o usuário e a senha, se o usuário foi encontrado e a senha está correta, None caso contrário.
    :rtype: tuple

    Exemplo de uso:

    >>> verify_user('exemplo', 'senha_de_exemplo')
    ('exemplo', 'senha_de_exemplo')
    """
    user = find_user(username)
    pswd = find_password(password)
    if user and pswd:
        return user, pswd
    return None
