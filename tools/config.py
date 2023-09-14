import os

from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {'host': os.environ.get('MONGO_URI')}
    REDIS_URL = os.environ.get('REDIS_URL')
    DEBUG = True
    SESSION_COOKIE_NAME = 'meu_app_session'
