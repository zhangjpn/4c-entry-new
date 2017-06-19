# -*- coding:utf-8 -*-

from pymongo import MongoClient
from app4c.tools import to_temp_db_and_upload_data

def get_data():
    """获取维修单列表"""
    cli = MongoClient()
    coll = cli.for4c.customerconsume
    docs = coll.find()
    data_list = []
    for doc in docs:
        data_list.append(doc)
    return data_list

def test_upload():
    """测试数据上传功能"""
    print('测试开始...')
    data_list = get_data()
    count = 1
    for doc in data_list:
        print('正在处理第 %d 条数据...' % count)
        to_temp_db_and_upload_data(doc)
        count += 1

if __name__ == '__main__':
    test_upload()