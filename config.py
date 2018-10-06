class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'my secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/sampledb' or ''


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/sampledb' or ''
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

