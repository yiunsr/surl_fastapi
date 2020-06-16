import os

class Config:
    SERVER_TYPE = 'none'
    DATABASE_URL = \
       "postgresql://surl_user:abcd1234@127.0.0.1:5432/surl_dev"
    @staticmethod
    def init_app(app):
        print('!!!! CHOOSE SERVER TYPE !!!!')

    def env(self, key):
        return getattr(self, key)


class DevelopmentConfig(Config):
    SERVER_TYPE = 'development'
    DATABASE_URL = \
       "postgresql://surl_user:abcd1234@127.0.0.1:5432/surl_dev"

    @staticmethod
    def init_app(app):
        print('THIS SERVER IS IN development MODE.')


class TestingConfig(Config):
    SERVER_TYPE = 'test'
    DATABASE_URL = \
        "postgresql://surl_user:abcd1234@127.0.0.1:5432/surl_test"

    @staticmethod
    def init_app(app):
        print('THIS SERVER IS IN test MODE.')


class ProductionConfig(Config):
    SERVER_TYPE = 'production'
    DATABASE_URL = \
        "postgresql://surl_user:User_PW!@127.0.0.1:5432/surl"

    @staticmethod
    def init_app(app):
        print('THIS SERVER IS IN production MODE.')

class PytestConfig(Config):
    SERVER_TYPE = 'pytest'
    DATABASE_URL = \
        "postgresql://surl_user:User_PW!@127.0.0.1:5432/pytest"

    @staticmethod
    def init_app(app):
        print('THIS SERVER IS IN pytest MODE.')


app_config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'pytest': PytestConfig,
    'default': DevelopmentConfig
}
_server_type = os.getenv('SERVER_TYPE') or 'default'
AppConfig = app_config_map[_server_type]
