from dotenv import load_dotenv
import os

load_dotenv()


class MysqlConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class SqliteConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('URI1')
    SECRET_KEY = os.environ.get('SECRET_KEY')


cfg = {
    "mysql": MysqlConfig,
    "sqlite": SqliteConfig
}
