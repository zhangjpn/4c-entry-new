# -*- coding:utf-8 -*-

from flask import Blueprint, jsonify

api = Blueprint(name='serverapi')


@api.route(r'/4c/car/create', methods=['POST'])
def create_car():

    return jsonify({'status':'ok', 'code':'200'}), 200

