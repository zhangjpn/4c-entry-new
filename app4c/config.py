# -*-coding:utf-8 -*-
import os.path as path

basedir = path.dirname(path.dirname(__file__))
DEBUG = False
MONGODB_DB = 'for4c'
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
SECRET_KEY = 'eyJhbGciOiJIUzI1NiJ9.ImFzZGZhZiI.YU5Bg4blESJJxXM7aCeQ_Q_2Sui0gRfn-JLJWJoAez8'

TARGET_UPLOAD_DBNAME = 'spv1'  # 数据上传的目标数据库 正式数据库：'spv1'
