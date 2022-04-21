import os


class Config(object):
    SECRET_KEY = os.urandom(16)


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///apl.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False


config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}