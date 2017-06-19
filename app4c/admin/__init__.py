# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template


administrator = Blueprint('admin', url_prefix='/admin')


@administrator.route(r'/')
def index():
    return render_template()