# -*-coding:utf-8 -*-

from flask import request, jsonify, make_response
from pymongo import MongoClient
import datetime
from .tools import to_temp_db_and_upload_data
import logging
import os.path as path
from .config import basedir
import requests
# 日志记录
db = MongoClient()['for4c']  # 暂存数据库
view_log = path.join(basedir, 'views_4c.log')
logger = logging.getLogger('views')
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
fhandler = logging.FileHandler(view_log, mode='a')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.INFO)
logger.addHandler(fhandler)  # 一般日志轮替


def init_views(app):
    @app.route('/4c/car/create/', methods=['POST'])
    def create_car_info():
        """创建车辆信息
        集合名称：car
        """
        collection = db.car
        try:
            production_api = 'http://b.xiulianzone.com/4c/car/create/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据验证
        # if not isinstance(request.json['CarNum'], str):
        #     return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):
            return make_response(jsonify({'message': 'failed', 'reason': 'item exists'})), 400

        # 数据入库
        else:
            car_info = {}
            # 数据重组
            car_info['ID'] = request.json.get('ID', '')
            car_info['Guid'] = request.json.get('Guid', '')
            car_info['DataTime'] = request.json.get('DataTime', '')
            car_info['CarNum'] = request.json.get('CarNum', '')
            car_info['CarStyleID'] = request.json.get('CarStyleID', '')
            car_info['CarBrand'] = request.json.get('CarBrand', '')
            car_info['CarSery'] = request.json.get('CarSery', '')
            car_info['CarStyle'] = request.json.get('CarStyle', '')
            car_info['Price'] = request.json.get('Price', '')
            car_info['Color'] = request.json.get('Color', '')
            car_info['VIN'] = request.json.get('VIN', '')
            car_info['EngineNumber'] = request.json.get('EngineNumber', '')
            car_info['CurrentMileage'] = request.json.get('CurrentMileage', '')
            car_info['Name'] = request.json.get('Name', '')
            car_info['CID'] = request.json.get('CID', '')
            car_info['ContactInfo'] = request.json.get('ContactInfo', '')
            car_info['ExpiryDate'] = request.json.get('ExpiryDate', '')
            car_info['BranchStore'] = request.json.get('BranchStore', '')
            car_info['InsuranceCompany'] = request.json.get('InsuranceCompany', '')
            car_info['InsuranceAmount'] = request.json.get('InsuranceAmount', '')
            car_info['InsuranceDate'] = request.json.get('InsuranceDate', '')
            car_info['NameSecond'] = request.json.get('NameSecond', '')
            car_info['CIDSecond'] = request.json.get('CIDSecond', '')
            car_info['NameThree'] = request.json.get('NameThree', '')
            car_info['CIDThree'] = request.json.get('CIDThree', '')
            car_info['InsuranceRemindDate'] = request.json.get('InsuranceRemindDate', '')
            car_info['InsuranceRemindSendDate'] = request.json.get('InsuranceRemindSendDate', '')
            car_info['InsuranceRemindState'] = request.json.get('InsuranceRemindState', '')
            car_info['InsuranceAutoSend'] = request.json.get('InsuranceRemindDate', '')
            car_info['YearlyinspectionRemindDate'] = request.json.get('YearlyinspectionRemindDate', '')
            car_info['YearlyinspectionRemindSendDate'] = request.json.get('YearlyinspectionRemindSendDate', '')
            car_info['YearlyinspectionRemindState'] = request.json.get('YearlyinspectionRemindState', '')
            car_info['YearlyinspectionAutoSend'] = request.json.get('YearlyinspectionAutoSend', '')
            car_info['DriveNoImgOne'] = request.json.get('DriveNoImgOne', '')
            car_info['DriveNoImgTwo'] = request.json.get('DriveNoImgTwo', '')
            car_info['OtherImgThree'] = request.json.get('OtherImgThree', '')
            car_info['OtherImgFour'] = request.json.get('OtherImgFour', '')
            car_info['OtherImgFive'] = request.json.get('OtherImgFive', '')
            car_info['Remark'] = request.json.get('Remark', '')
            car_info['ColorNum'] = request.json.get('ColorNum', '')
            car_info['ChassisNum'] = request.json.get('ChassisNum', '')
            car_info['TransmissionNum'] = request.json.get('TransmissionNum', '')
            car_info['License'] = request.json.get('License', '')
            create_time = datetime.datetime.utcnow()  # 数据创建时间
            car_info['created'] = request.json.get('created', create_time)  # 创建时间
            car_info['updated'] = request.json.get('updated', create_time)  # 更新时间
            # 写入数据库
            collection.insert_one(car_info)
            car_info.pop('_id')  # 删除操作数据库时自动添加的键值对
        return jsonify({'message': 'success', 'item': car_info}), 200


    @app.route('/4c/car/update/', methods=['POST'])
    def update_car_info():
        """
        更新车辆信息
        集合名称：car
        """

        collection = db.car
        try:
            production_api = 'http://b.xiulianzone.com/4c/car/update/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if not collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):  # 车辆信息不存在
            return make_response(jsonify({'message': 'failed', 'reason': 'item not exist'})), 400

        else:
            car_update = {}
            keys = list(request.json.keys())  # 获取key，生成list
            for key in keys:
                car_update[key] = request.json.get(key, '')
            update_time = datetime.datetime.utcnow()
            car_update['updated'] = request.json.get('updated', update_time)  # 更新时间

            # 写入数据库
            collection.update({'ID': request.json['ID'], 'Guid': request.json['Guid']}, {'$set': car_update})
            return jsonify({'message': 'success', 'item': request.json}), 200


    @app.route('/4c/car/list/', methods=['GET'])
    def query_car_info():
        """查询车辆信息
        query_string:page=1,rows=12
        """
        collection = db.car
        try:
            page = int(request.args['page'])
            rows = int(request.args['rows'])
        except:
            page = 1
            rows = 10
        finally:
            cursor = collection.find().skip((page - 1) * rows).limit(rows)
            items = [item for item in cursor]
            for item in items:
                try:
                    item.pop('_id')
                    item.pop('created')
                    item.pop('updated')
                except Exception as e:
                    logger.exception(e)
        return jsonify({'message': 'success', 'data': items}), 200


    @app.route('/4c/carowner/create/', methods=['POST'])
    def create_carowner_info():
        """创建车主信息
        集合名称:carOwner
        """
        collection = db.carowner
        try:
            production_api = 'http://b.xiulianzone.com/4c/carowner/create/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400

        # 数据查重
        if collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):  # 有重复值
            return make_response(jsonify({'message': 'failed', 'reason': 'item exists'})), 400

        # 数据入库
        else:
            carOwner = {}
            # 数据重组
            carOwner['ID'] = request.json.get('ID', '')
            carOwner['Guid'] = request.json.get('Guid', '')
            carOwner['DataTime'] = request.json.get('DataTime', '')
            carOwner['SID'] = request.json.get('SID', '')
            carOwner['Stype'] = request.json.get('Stype', '')
            carOwner['StypeInCode'] = request.json.get('StypeInCode', '')
            carOwner['Name'] = request.json.get('Name', '')
            carOwner['Sex'] = request.json.get('Sex', '')
            carOwner['Address'] = request.json.get('Address', '')
            carOwner['WeixinState'] = request.json.get('WeixinState', '')
            carOwner['WeChatNo'] = request.json.get('WeChatNo', '')
            carOwner['CusStaff'] = request.json.get('CusStaff', '')
            carOwner['CusStaffID'] = request.json.get('CusStaffID', '')
            carOwner['DriveNo'] = request.json.get('DriveNo', '')
            carOwner['DriveEndTime'] = request.json.get('DriveEndTime', '')
            carOwner['SpendPwd'] = request.json.get('SpendPwd', '')
            carOwner['Birthday'] = request.json.get('Birthday', '')
            carOwner['Reward'] = request.json.get('Reward', '')
            carOwner['Remark'] = request.json.get('Remark', '')
            carOwner['Phone'] = request.json.get('Phone', '')
            carOwner['AppID'] = request.json.get('AppID', '')
            carOwner['UnitCustomer'] = request.json.get('UnitCustomer', '')
            carOwner['ZPhone'] = request.json.get('ZPhone', '')
            carOwner['DriveNoImgOne'] = request.json.get('DriveNoImgOne', '')
            carOwner['DriveNoImgTwo'] = request.json.get('DriveNoImgTwo', '')
            carOwner['CarCard'] = request.json.get('CarCard', '')
            carOwner['CarID'] = request.json.get('CarID', '')
            carOwner['CarStyle'] = request.json.get('CarStyle', '')
            carOwner['CarBrand'] = request.json.get('CarBrand', '')
            carOwner['CarSery'] = request.json.get('CarSery', '')
            carOwner['Color'] = request.json.get('Color', '')
            carOwner['AllowCar'] = request.json.get('AllowCar', '')
            carOwner['ExplainsCustomerID'] = request.json.get('ExplainsCustomerID', '')
            carOwner['ExplainsCustomer'] = request.json.get('ExplainsCustomer', '')
            carOwner['ClubCard'] = request.json.get('ClubCard', '')
            carOwner['ClubGrade'] = request.json.get('ClubGrade', '')
            carOwner['ClubGradeID'] = request.json.get('ClubGradeID', '')
            carOwner['StoreReward'] = request.json.get('StoreReward', '')
            carOwner['Amount'] = request.json.get('Amount', '')
            carOwner['NoAmount'] = request.json.get('NoAmount', '')
            carOwner['Reference'] = request.json.get('Reference', '')
            carOwner['ReferenceID'] = request.json.get('ReferenceID', '')
            carOwner['LatelySpendDataTime'] = request.json.get('LatelySpendDataTime', '')
            carOwner['JackpotSpendAmount'] = request.json.get('JackpotSpendAmount', '')
            carOwner['JackpotSpendMuch'] = request.json.get('JackpotSpendMuch', '')
            carOwner['Tab'] = request.json.get('Tab', '')
            carOwner['DriveRemindDate'] = request.json.get('DriveRemindDate', '')
            carOwner['DriveRemindSendDate'] = request.json.get('DriveRemindSendDate', '')
            carOwner['DriveRemindState'] = request.json.get('DriveRemindState', '')
            carOwner['DriveAutoSend'] = request.json.get('DriveAutoSend', '')
            carOwner['CarIDTwo'] = request.json.get('CarIDTwo', '')
            carOwner['CarCardTwo'] = request.json.get('CarCardTwo', '')
            carOwner['CarIDThree'] = request.json.get('CarIDThree', '')
            carOwner['CarCardThree'] = request.json.get('CarCardThree', '')
            carOwner['FractionState'] = request.json.get('FractionState', '')
            carOwner['DriveFractionRemindDateTime'] = request.json.get('DriveFractionRemindDateTime', '')
            carOwner['DriveFractionRemindDate'] = request.json.get('DriveFractionRemindDate', '')
            carOwner['GradeExpireDate'] = request.json.get('GradeExpireDate', '')
            carOwner['GradeExpireForever'] = request.json.get('GradeExpireForever', '')
            carOwner['FreeSMSCount'] = request.json.get('FreeSMSCount', '')
            carOwner['License'] = request.json.get('License', '')
            create_time = datetime.datetime.utcnow()  # 数据创建默认时间
            carOwner['created'] = request.json.get('created', create_time)  # 创建时间
            carOwner['updated'] = request.json.get('updated', create_time)  # 更新时间
            # 写入数据库
            collection.insert_one(carOwner)
            carOwner.pop('_id')  # 删除操作数据库时自动添加的键值对
        return jsonify({'message': 'success', 'item': carOwner}), 200


    @app.route('/4c/carowner/update/', methods=['POST'])
    def update_carowner_info():
        """
        更新车主信息
        :return:
        """

        collection = db.carowner
        try:
            production_api = 'http://b.xiulianzone.com/4c/carowner/update/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if not collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):  # 信息不存在
            return make_response(jsonify({'message': 'failed', 'reason': 'item not exist'})), 400

        else:
            carOwner_update = {}
            keys = list(request.json.keys())  # 获取key，生成list
            for key in keys:
                carOwner_update[key] = request.json.get(key, '')
            update_time = datetime.datetime.utcnow()
            carOwner_update['updated'] = request.json.get('updated', update_time)  # 更新时间

            # 写入数据库
            collection.update({'ID': request.json['ID'], 'Guid': request.json['Guid']}, {'$set': carOwner_update})
            return jsonify({'message': 'success', 'item': request.json}), 200


    @app.route('/4c/carowner/list/', methods=['GET'])
    def query_carowner_info():
        """
        查询车主信息
        query_string:page=1,rows=12
        :return:
        """
        collection = db.carowner
        try:
            page = int(request.args['page'])
            rows = int(request.args['rows'])
        except:
            page = 1
            rows = 10
        finally:
            cursor = collection.find().skip((page - 1) * rows).limit(rows)
            items = [item for item in cursor]
            for item in items:
                try:
                    item.pop('_id')
                    item.pop('created')
                    item.pop('updated')
                except Exception as e:
                    logger.exception(e)
        return jsonify({'message': 'success', 'data': items}), 200


    @app.route('/4c/customer/consume/create/', methods=['POST'])
    def create_customer_consume():
        """创建客户消费记录"""
        collection = db.customerconsume
        try:
            production_api = 'http://b.xiulianzone.com/4c/customer/consume/create/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):
            return make_response(jsonify({'message': 'failed', 'reason': 'item exists'})), 400
        # 数据入库
        else:
            consume = {}
            # 数据重组
            consume['ID'] = request.json.get('ID', '')
            consume['Guid'] = request.json.get('Guid', '')
            consume['DataTime'] = request.json.get('DataTime', '')
            consume['CustomerConsumeNum'] = request.json.get('CustomerConsumeNum', '')
            consume['CarOwnerID'] = request.json.get('CarOwnerID', '')
            consume['CarOwnerName'] = request.json.get('CarOwnerName', '')
            consume['ConsumeCarID'] = request.json.get('ConsumeCarID', '')
            consume['ConsumeCarNum'] = request.json.get('ConsumeCarNum', '')
            consume['ConsumeContent'] = request.json.get('ConsumeContent', '')
            consume['InitialMoney'] = request.json.get('InitialMoney', '')
            consume['TotalMoney'] = request.json.get('TotalMoney', '')
            consume['GetInTime'] = request.json.get('GetInTime', '')
            consume['GetOutTime'] = request.json.get('GetOutTime', '')
            consume['GetInMileage'] = request.json.get('GetInMileage', '')
            consume['GetOutMileage'] = request.json.get('GetOutMileage', '')
            consume['ProductSalesManID'] = request.json.get('ProductSalesManID', '')
            consume['ProductSalesManName'] = request.json.get('ProductSalesManName', '')
            consume['ArticleSalesManID'] = request.json.get('ArticleSalesManID', '')
            consume['ArticleSalesManName'] = request.json.get('ArticleSalesManName', '')
            consume['ArticleConstructorID'] = request.json.get('ArticleConstructorID', '')
            consume['ArticleConstructorName'] = request.json.get('ArticleConstructorName', '')
            consume['OrderRemark'] = request.json.get('OrderRemark', '')
            consume['UserRemark'] = request.json.get('UserRemark', '')
            consume['EmployeeID'] = request.json.get('EmployeeID', '')
            consume['EmployeeName'] = request.json.get('EmployeeName', '')
            consume['OrderTime'] = request.json.get('OrderTime', '')
            consume['State'] = request.json.get('State', '')
            consume['CreateTime'] = request.json.get('CreateTime', '')
            consume['ReceivementTime'] = request.json.get('ReceivementTime', '')
            consume['BranchStoreID'] = request.json.get('BranchStoreID', '')
            consume['StationID'] = request.json.get('StationID', '')
            consume['StationName'] = request.json.get('StationName', '')
            consume['InsuranceID'] = request.json.get('InsuranceID', '')
            consume['InsuranceName'] = request.json.get('InsuranceName', '')
            consume['ConstructionID'] = request.json.get('ConstructionID', '')
            consume['ConstructionName'] = request.json.get('ConstructionName', '')
            consume['PriorScrapState'] = request.json.get('PriorScrapState', '')
            consume['RedConsumeNum'] = request.json.get('RedConsumeNum', '')
            consume['ScrapTime'] = request.json.get('ScrapTime', '')
            consume['Stemfrom'] = request.json.get('Stemfrom', '')
            consume['IntelligentPeccancyQueryNum'] = request.json.get('IntelligentPeccancyQueryNum', '')
            consume['License'] = request.json.get('License', '')
            create_time = datetime.datetime.utcnow()  # 数据默认上传时间
            consume['created'] = request.json.get('created', create_time)  # 上传时间
            consume['updated'] = request.json.get('updated', create_time)  # 更新时间
            # 写入数据库
            collection.insert_one(consume)
            consume.pop('_id')  # 删除操作数据库时自动添加的键值对
            # 执行数据标准化和上传操作
            to_temp_db_and_upload_data(consume)

        return jsonify({'message': 'success', 'item': consume}), 200


    @app.route('/4c/customer/consume/update/', methods=['POST'])
    def update_customer_consume():
        """更新客户消费记录"""
        collection = db.customerconsume
        try:
            production_api = 'http://b.xiulianzone.com/4c/customer/consume/update/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if not collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):  # 信息不存在
            return make_response(jsonify({'message': 'failed', 'reason': 'item not exist'})), 400

        else:
            consume_update = {}
            keys = list(request.json.keys())  # 获取key，生成list
            for key in keys:
                consume_update[key] = request.json.get(key)
            update_time = datetime.datetime.utcnow()
            consume_update['updated'] = request.json.get('updated', update_time)  # 更新时间

            # 写入数据库
            collection.update({'ID': request.json['ID'], 'Guid': request.json['Guid']}, {'$set': consume_update})
            # 执行数据标准化和上传操作
            to_temp_db_and_upload_data(consume_update)

            return jsonify({'message': 'success', 'item': request.json}), 200


    @app.route('/4c/customer/consume/list/', methods=['GET'])
    def query_customer_consume():
        """查询客户消费记录
        query_string:page=1,rows=12
        :return:
        """
        collection = db.customerconsume
        try:
            page = int(request.args['page'])
            rows = int(request.args['rows'])
        except:
            page = 1
            rows = 10
        finally:
            cursor = collection.find().skip((page - 1) * rows).limit(rows)
            items = [item for item in cursor]
            for item in items:
                try:
                    item.pop('_id')
                    item.pop('created')
                    item.pop('updated')
                except Exception as e:
                    logger.exception(e)
        return jsonify({'message': 'success', 'data': items}), 200


    @app.route('/4c/customer/consume/detail/create/', methods=['POST'])
    def create_consume_detail():
        """创建客户详细消费记录"""
        collection = db.customerconsumedetail
        try:
            production_api = 'http://b.xiulianzone.com/4c/customer/consume/detail/create/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):
            return make_response(jsonify({'message': 'failed', 'reason': 'item exists'})), 400
        # 数据入库
        else:
            detail = {}
            # 数据重组
            detail['ID'] = request.json.get('ID', '')
            detail['Guid'] = request.json.get('Guid', '')
            detail['DataTime'] = request.json.get('DataTime', '')
            detail['CustomerConsumeID'] = request.json.get('CustomerConsumeID', '')
            detail['CustomerConsumeNum'] = request.json.get('CustomerConsumeNum', '')
            detail['ObjectType'] = request.json.get('ObjectType', '')
            detail['ObjectID'] = request.json.get('ObjectID', '')
            detail['ObjectName'] = request.json.get('ObjectName', '')
            detail['Brand'] = request.json.get('Brand', '')
            detail['Fit'] = request.json.get('Fit', '')
            detail['Spec'] = request.json.get('Spec', '')
            detail['StockID'] = request.json.get('StockID', '')
            detail['StockName'] = request.json.get('StockName', '')
            detail['UnitPrice'] = request.json.get('UnitPrice', '')
            detail['Qty'] = request.json.get('Qty', '')
            detail['Discount'] = request.json.get('Discount', '')
            detail['TotalPrice'] = request.json.get('TotalPrice', '')
            detail['Frequency'] = request.json.get('Frequency', '')
            detail['DetailType'] = request.json.get('DetailType', '')
            detail['CarOwnerPackagesID'] = request.json.get('CarOwnerPackagesID', '')
            detail['BranchStoreID'] = request.json.get('BranchStoreID', '')
            detail['License'] = request.json.get('License', '')
            create_time = datetime.datetime.utcnow()  # 数据创建默认时间
            detail['created'] = request.json.get('created', create_time)  # 创建时间
            detail['updated'] = request.json.get('updated', create_time)  # 更新时间
            # 写入数据库
            collection.insert_one(detail)
            detail.pop('_id')  # 删除操作数据库时自动添加的键值对

        return jsonify({'message': 'success', 'item': detail}), 200

    @app.route('/4c/customer/consume/detail/update/', methods=['POST'])
    def update_consume_detail():
        """创建客户详细消费记录"""
        collection = db.customerconsumedetail
        try:
            production_api = 'http://b.xiulianzone.com/4c/customer/consume/detail/update/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if not collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):  # 信息不存在
            return make_response(jsonify({'message': 'failed', 'reason': 'item not exist'})), 400

        else:
            detail = {}
            keys = list(request.json.keys())  # 获取key，生成list
            for key in keys:
                detail[key] = request.json.get(key, '')
            update_time = datetime.datetime.utcnow()
            detail['updated'] = request.json.get('updated', update_time)  # 更新时间

            # 写入数据库
            collection.update({'ID': request.json['ID'], 'Guid': request.json['Guid']}, {'$set': detail})

            return jsonify({'message': 'success', 'item': request.json}), 200

    @app.route('/4c/customer/consume/detail/list/', methods=['GET'])
    def query_consume_detail():
        """查询客户详细消费记录
        query_string:page=1,rows=12
        :return:
        """
        collection = db.customerconsumedetail
        try:
            page = int(request.args['page'])
            rows = int(request.args['rows'])
        except:
            page = 1
            rows = 10
        finally:
            cursor = collection.find().skip((page - 1) * rows).limit(rows)
            items = [item for item in cursor]
            for item in items:
                try:
                    item.pop('_id', '')
                    item.pop('created', '')
                    item.pop('updated', '')
                except Exception as e:
                    logger.exception(e)
        return jsonify({'message': 'success', 'data': items}), 200

    @app.route('/4c/company/create/', methods=['POST'])
    def create_company():
        """创建维修企业信息"""
        collection = db.companies4c
        try:
            production_api = 'http://b.xiulianzone.com/4c/company/create/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):
            return make_response(jsonify({'message': 'failed', 'reason': 'item exists'})), 400
        # 数据入库
        else:
            company = {}
            # 数据重组
            company['ID'] = request.json.get('ID', '')
            company['Guid'] = request.json.get('Guid', '')
            company['DataTime'] = request.json.get('DataTime', '')
            company['DBName'] = request.json.get('DBName', '')
            company['StoreName'] = request.json.get('StoreName', '')
            company['Address'] = request.json.get('Address', '')
            company['Registrant'] = request.json.get('Registrant', '')
            company['Telephone'] = request.json.get('Telephone', '')
            company['Province'] = request.json.get('Province', '')
            company['City'] = request.json.get('City', '')
            company['County'] = request.json.get('County', '')
            company['RegisterTime'] = request.json.get('RegisterTime', '')
            company['Range'] = request.json.get('Range', '')
            company['F2SAmount'] = request.json.get('F2SAmount', 0)
            company['License'] = request.json.get('License', '')
            create_time = datetime.datetime.utcnow()  # 数据创建默认时间
            company['created'] = request.json.get('created', create_time)  # 创建时间
            company['updated'] = request.json.get('updated', create_time)  # 更新时间
            # 写入数据库
            collection.insert_one(company)
            company.pop('_id')  # 删除操作数据库时自动添加的键值对
        return jsonify({'message': 'success', 'item': company}), 200

    @app.route('/4c/company/update/', methods=['POST'])
    def update_company():
        """更新维修企业信息"""
        collection = db.companies4c
        try:
            production_api = 'http://b.xiulianzone.com/4c/company/update/'
            temp = request.json
            requests.post(url=production_api, json=temp)
        except:
            pass
        if not request.json or 'ID' not in request.json or 'Guid' not in request.json:
            return make_response(jsonify({'message': 'failed', 'reason': 'invalid data'})), 400
        # 数据查重
        if not collection.find_one({'ID': request.json['ID'], 'Guid': request.json['Guid']}):  # 信息不存在
            return make_response(jsonify({'message': 'failed', 'reason': 'item not exist'})), 400

        else:
            company = {}
            keys = list(request.json.keys())  # 获取key，生成list
            for key in keys:
                company[key] = request.json.get(key, '')
            update_time = datetime.datetime.utcnow()
            company['updated'] = request.json.get('updated', update_time)  # 更新时间

            # 写入数据库
            collection.update({'ID': request.json['ID'], 'Guid': request.json['Guid']}, {'$set': company})

            return jsonify({'message': 'success', 'item': request.json}), 200

    @app.route('/4c/company/list/', methods=['GET'])
    def query_company():
        """查询注册维修企业的信息
        query_string: page=1, rows=10
        :return: json字符串列表
        """
        collection = db.companies4c
        try:
            page = int(request.args['page'])
            rows = int(request.args['rows'])
        except:
            page = 1
            rows = 10
        finally:
            cursor = collection.find().skip((page - 1) * rows).limit(rows)
            items = [item for item in cursor]
            for item in items:
                try:
                    item.pop('_id')
                    item.pop('created')
                    item.pop('updated')
                except Exception as e:
                    logger.exception(e)
        return jsonify({'message': 'success', 'data': items}), 200

    @app.errorhandler(404)
    def page_not_found(error):
        logger.error(error)
        return make_response(jsonify({'message': 'Page not found'}), 404)

    @app.errorhandler(400)
    def bad_request(error):
        logger.error(error)
        return make_response(jsonify({'message': 'failed', 'reason': 'invalid arguments'}), 400)
    @app.errorhandler(405)
    def server_error(error):
        logger.error(error)
        return make_response(jsonify({'message': 'Method Not Allowed'}), 405)