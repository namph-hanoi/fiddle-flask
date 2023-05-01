import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = str(Path(Path(__file__).parent.name + '/../.env').resolve())
load_dotenv(dotenv_path)


class Config:
    NAME = os.getenv('NAME', 'Management Console')
    DEBUG = bool(os.getenv('FLASK_DEBUG', False))
    # ENV = os.getenv('FLASK_DEBUG', 'production')
    APP_HOST = os.getenv('APP_HOST', '127.0.0.1')
    APP_PORT = os.getenv('APP_PORT', '5000')
    APP_SECRET = os.getenv('APP_SECRET', '')

    GRACEFUL_SHUTDOWN_SEC = int(os.getenv('GRACEFUL_SHUTDOWN_SEC', 120))
    TOKEN_VALID_SEC = int(os.getenv('TOKEN_VALID_SEC', 86400))
    TOKEN_ENCODE_SECRET = os.getenv('TOKEN_ENCODE_SECRET', 'abcxyz')
    TOKEN_HEADER_NAME = os.getenv("TOKEN_HEADER_NAME", "x-auth-token")

    SWAGGER_URL = '/api/v1/swagger'
    SWAGGER_PATH = 'documents/api/swagger.yaml'

    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        **{
            'user': os.getenv('DB_USER', 'admin'),
            'password': os.getenv('DB_PASSWORD', ''),
            'host': os.getenv('DB_HOST', 'database'),
            'port': os.getenv('DB_PORT', '5432'),
            'name': os.getenv('DB_NAME', 'deploy_console'),
        })
    if os.getenv('FLASK_DEBUG') == 'test':
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    else:
        SQLALCHEMY_POOL_SIZE = int(os.getenv('SQLALCHEMY_POOL_SIZE', 10))
        SQLALCHEMY_MAX_OVERFLOW = int(os.getenv('SQLALCHEMY_MAX_OVERFLOW', 10))
        SQLALCHEMY_POOL_TIMEOUT = int(os.getenv('SQLALCHEMY_POOL_TIMEOUT', 30))

    SQLALCHEMY_ECHO = bool(os.getenv('SQLALCHEMY_ECHO', False))

    # Todo
    # AWS_KEY = os.getenv('AWS_KEY', '')
    # AWS_SECRET = os.getenv('AWS_SECRET', '')
    # AWS_REGION = os.getenv('AWS_REGION', '')
    # S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', '')
    # S3_BUCKET_SQL_DEV = os.getenv('S3_BUCKET_SQL_DEV', '')
    # S3_PRE_SIGNED_URL_EXPIRE_SEC = int(
    #     os.getenv('S3_PRE_SIGNED_URL_EXPIRE_SEC', 3600))

    # FRONTEND_BASE_URL = os.getenv('FRONTEND_BASE_URL', '')

    # SLACK_ERROR_NOTIFICATION_WEBHOOK_URL = os.getenv(
    #     'SLACK_ERROR_NOTIFICATION_WEBHOOK_URL', '')
    # SLACK_ERROR_NOTIFICATION_ENABLED = os.getenv(
    #     'SLACK_ERROR_NOTIFICATION_ENABLED', True)
