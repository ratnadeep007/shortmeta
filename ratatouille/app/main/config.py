import os

postgres_url = os.environ["DATABASE_URL"]


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_url


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_url


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)

