# -*-coding:utf-8 -*-

"""用于测试客户调用api的情况"""


import requests

host = 'http://127.0.0.1:5000'
# 创建车辆api
def create_update_test(url, data):
    """
    :param data: 字典格式数据
    :return: 请求返回的结果
    """

    full_url = host + url
    data = dict({'url': full_url}, **data)
    res = requests.post(url=full_url, json=data)
    return res.text

def get_list(url, page=1, rows=12):
    full_url = host + url

    params = {
        'page': page,
        'rows': rows,
    }
    res = requests.get(url=full_url, params=params)
    return res.text


if __name__ == '__main__':
    # car_item = {
    #     'CarNum': '33',  # 车牌
    #     'CarStyleID': 1311,  # 车型id
    #     'CarBrand': 'ggg',  # 车辆品牌
    #     'CarSery': 'series1',  # 车系
    #     'Price': 13600  # 车价
    # }
    #
    # url = '/api/serverapi/car/list/'
    # res = create_update_test(url, car_item)
    # print(res)
    # url = '/api/serverapi/car/create/'
    # res = get_list(url)
    # print(res)

    # 测试  创建车辆信息
    car_item = {
        'CarNum': '粤nnnnn',  # 车牌
        'CarStyleID': 1234,  # 车型id
        'CarBrand': '0000',  # 车辆品牌
        'CarSery': 'series1',  # 车系
        'Price': 22200  # 车价
    }
    create_url = 'http://app.xiulianzone.com/4c/car/create/'
    r = requests.post(url=create_url,json=car_item)
    print(r.headers)
    print(r.json())

    # 测试  更新车辆信息
    # car_item = {
    #     'CarNum': '粤nnnnn',  # 车牌
    #     'CarStyleID': 0000,  # 车型id
    #     'CarBrand': '0000',  # 车辆品牌
    #     'CarSery': 'series1',  # 车系
    #     'Price': 1333  # 车价
    # }
    # update_url = 'http://127.0.0.1:5000/api/serverapi/car/update/'
    # r = requests.put(url=update_url, data=json.dumps(car_item))
    # print(r.headers)
    # print(r.json())

    # 测试 查询车辆信息
    # url = 'http://127.0.0.1:5000/api/serverapi/car/list/'
    # params = {
    #     'page':2,
    #     'rows':10,
    # }
    # r = requests.get(url,params=params)
    # print(r.headers)
    # for k,v in r.json()['data'].items():
    #     print(k,v['CarNum'])

    # 测试 创建车主信息
    # owner = {
    #     'SID': 4,
    #     'Stype': 7,
    #     'StypeInCode': 3,
    #     'Name': 'eric',
    #     'Sex': 'male',
    #     'Created': '2017-05-04',
    #     'tag': 'vip',
    # }
    # create_url = 'http://127.0.0.1:5000/api/serverapi/carowner/create/'
    # r = requests.post(url=create_url,json=owner)
    # print(r.headers)
    # print(r.json())

    # 测试 查询车辆信息
    # url = 'http://127.0.0.1:5000/api/serverapi/carowner/list/'
    # params = {
    #     'page':1,
    #     #'rows':10,
    # }
    # r = requests.get(url,params=params)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())
    # for k,v in r.json()['data'].items():
    #     print(k,v['Name'])



    # 测试  创建用户消费信息
    # item = {
    #     'CustomerConsumeNum': '124444789',
    #     'CarOwnerID': 9999,
    #     'CarOwnerName': 'jack',
    #     'ConsumeCarID': 'rose',
    #     'ConsumeCarNum': '京899988',
    # }
    #
    # create_url = 'http://127.0.0.1:5000/api/serverapi/customer/consume/create/'
    # r = requests.post(url=create_url,json=item)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())


    # 测试 更新消费信息
    # item = {
    #     'CustomerConsumeNum': '124444781',
    #     'CarOwnerID': 293,
    #     'CarOwnerName': 'jack',
    #     'ConsumeCarID': '111',
    #     'ConsumeCarNum': 's;alfjds;af',
    # }
    # update_url = 'http://127.0.0.1:5000/api/serverapi/customer/consume/update/'
    # r = requests.post(url=update_url, json=item)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())

    # 测试 查询消费信息
    # url = 'http://127.0.0.1:5000/api/serverapi/customer/consume/list/'
    # params = {
    #     'page':1,
    #     'rows':10,
    # }
    # r = requests.get(url,params=params)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())

    # 测试  创建用户消费详细信息
    # item = {
    #     'CustomerConsumeID': '777777777',
    #     'CustomerConsumeNum': '12444478333',
    #     'ObjectType': '123',
    #     'ObjectID': '3--------33',
    #     'ObjectName': '--55555555-----',
    #     'Brand': 'aabbbbbbbbbaa',
    # }
    #
    # create_url = 'http://127.0.0.1:5000/api/serverapi/customer/consume/detail/create/'
    # r = requests.post(url=create_url,json=item)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())


    # 测试  更新用户消费详细信息
    # item = {
    #     'CustomerConsumeID': '9999999999999999999999999999999999999',
    #     'CustomerConsumeNum': '12444478333',
    #     'ObjectType': '123',
    #     'ObjectID': '33333333',
    #     'ObjectName': '--------------',
    #     'Brand': 'aaaaa',
    # }
    #
    # create_url = 'http://127.0.0.1:5000/api/serverapi/customer/consume/detail/update/'
    # r = requests.post(url=create_url, json=item)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())

    # 测试 查询消费详细信息
    # url = 'http://127.0.0.1:5000/api/serverapi/customer/consume/detail/list/'
    # params = {
    #     'page': 1,
    #     'rows': 10,
    # }
    # r = requests.get(url, params=params)
    # print(r.headers)
    # print(r.status_code)
    # print(r.json())