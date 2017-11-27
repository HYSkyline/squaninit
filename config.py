# -*- coding:utf-8 -*-

import os
here = os.path.abspath(os.path.dirname(__file__))

f = open('config.config', 'r')
content = f.readlines()
f.close()


init_config = {}
for each in content:
    config_key, config_value = each.split(',')
    init_config[config_key] = config_value[:-1]


class Config:
    """
    配置基类
    """
    SECRET_KEY = os.environ.get('SECREC_KEY') or init_config['SECRET_KEY']
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN') or init_config['FLASK_ADMIN']


class DevelopmentConfig(Config):
    """
    开发状态
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or init_config['SQLALCHEMY_DATABASE_URI_dev']
    DEBUG = True


class TestingEmptyConfig(Config):
    """
    测试状态：数据库无数据
    """
    TESTING = True
    WTF_CSRF_ENABLED = False


class TestingFullConfig(TestingEmptyConfig):
    """
    测试状态：数据库有数据
    """


class ProductionConfig(Config):
    """
    生产状态
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or init_config['SQLALCHEMY_DATABASE_URI_dev']


class HerokuConfig(Config):
    """
    Heroku平台配置
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or init_config['SQLALCHEMY_DATABASE_URI_heroku']
    SSL_DISABLE = False     # 启动 SLL 安全检查

    @classmethod
    def init_app(cls, app):
        # 将日志输出到 stderr
        import logging
        file_handler = logging.StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)
        # 处理代理服务器首部。在 Heroku 中，客户端没有直接托管程序，而是连接反向服务
        # 代理器，最后把请求重定向到程序上。这种连接方式中，只在代理服务器中运行 SSL 模式。
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
