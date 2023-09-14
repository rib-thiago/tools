import os

from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    """
    Classe de configuração para o aplicativo 'meu_app'.

    Esta classe define as configurações do aplicativo, incluindo a chave secreta,
    configurações do MongoDB, URL do Redis e opções de depuração.

    Exemplos de uso:

    >>> config = Config()

    >>> config.SECRET_KEY
    '9so3jYZSbrbvPqGoxYpO5i4fqj+mwX9UA29iuk+jhVkmaWpuyVoAV7xlaz4UI+56rK61fSW1AF/Qz/DF'

    >>> config.MONGODB_SETTINGS['host']
    'mongodb+srv://mackandalls:P260Hsp2qkOCogR8@aplicacao-tcc.5z9bk1q.mongodb.net/?retryWrites=true&w=majority'

    >>> config.REDIS_URL
    'redis://:FZgCwxjSpwLwiumD2WwBOerLmcHt1B06rJthGvjTPNHMKJJqR1rdAd+0fFdQWJYqb9OxoV+U3bKoAZ3E@localhost:6379/0'

    >>> config.DEBUG
    False

    >>> config.SESSION_COOKIE_NAME
    'meu_app_session'
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {'host': os.environ.get('MONGO_URI')}
    REDIS_URL = os.environ.get('REDIS_URL')
    DEBUG = True
    SESSION_COOKIE_NAME = 'meu_app_session'
