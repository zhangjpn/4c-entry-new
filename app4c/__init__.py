# -*- coding:utf-8 -*-

from flask import Flask
from .views import init_views
from .admin import administrator
from .serverapi import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.register_blueprint(blueprint=administrator)
    app.register_blueprint(blueprint=api)
    return app
