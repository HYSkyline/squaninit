# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()

def create_app(config_name):
    """ 工厂函数，用于创建 app 实例
    :param config_name: 配置类型
    :return: app 实例
    """
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)

    if app.config.get('SSL_DISABLE', None):
        from flask_sslify import SSLify
        sslify = SSLify(app)
    from .main import main as main_buleprint            # 注册 main 蓝图
    app.register_blueprint(main_buleprint)
    return app
