# -*- coding:utf-8 -*-


"""用于测试数据标准化和上传功能"""

from app4c.tools import to_temp_db_and_upload_data
from pymongo import MongoClient
import unittest


def get_data():
    """获取维修单列表"""
    cli = MongoClient()
    coll = cli.for4c.customerconsume
    docs = coll.find()
    data_list = []
    for doc in docs:
        data_list.append(doc)
    return data_list


class TestUpload(unittest.TestCase):
    def setUp(self):
        self.data = get_data()

    def test_upload(self):
        for doc in self.data:
            self.assertIsNone(to_temp_db_and_upload_data(doc), msg='result should not be None')

    def tearDown(self):
        self.data = None


if __name__ == '__main__':
    unittest.main()
