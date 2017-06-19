# -*-coding:utf-8 -*-

import threading

from pymongo import MongoClient
import re
from .models import *
import time
import datetime
import logging
import os.path as path
from logging.handlers import RotatingFileHandler
from .config import basedir

# 记录日志
upload_log = path.join(basedir, 'upload_4c.log')
logger = logging.getLogger('upload')
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
rhandler = RotatingFileHandler(upload_log, mode='a', maxBytes=1 * 1024 * 1024, backupCount=3)
rhandler.setLevel(logging.INFO)
rhandler.setFormatter(formatter)
logger.addHandler(rhandler)  # 一般日志轮替


def str_to_date(string):
    if isinstance(string, datetime.datetime):
        return string
    if not isinstance(string, str):
        return None
    string = string.strip()
    try:
        ts = time.strptime(string, '%Y/%m/%d %H:%M:%S')
        dt = datetime.datetime(ts[0], ts[1], ts[2], ts[3] - 8, ts[4], ts[5])  # *ts[0:6]
    except:
        try:
            ts = time.strptime(string, '%Y-%m-%d %H:%M:%S')
            dt = datetime.datetime(ts[0], ts[1], ts[2], ts[3] - 8, ts[4], ts[5])
        except:
            try:  # 若数据不完整，尝试获取日期
                patt = re.compile(r'([0-9]{4})[\-\/]([0-9]{1,2})[\-\/]([0-9]{1,2})')
                d = patt.findall(string)[0]
                dt = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))
            except:
                dt = None
    return dt


def get_car_info(carnum):
    """获取车辆信息"""
    try:
        cli = MongoClient(host='127.0.0.1', port=27017, tz_aware=True)
        coll = cli.for4c.car
        car_info = coll.find_one({'CarNum': carnum}) or {}
    except:
        car_info = {}
    return car_info


def get_company_id(lic):
    """通过营业执照获取公司在数据库中的ObjectId对象，对象在spv1.compaies表中
    :param lic:营业执照
    :return ObjectId对象
    """
    try:
        cli = MongoClient(host='127.0.0.1', port=27017, tz_aware=True)
        coll = cli.spv1.companies
        company = coll.find_one({'socialCode': lic})
        return company.get('_id')
    except:
        return None


def get_store_id(lic):
    """通过营业执照获取终端门店的ObjectId对象，该对象在spv1.stores数据表中，"""
    try:
        cli = MongoClient(host='127.0.0.1', port=27017, tz_aware=True)
        store_coll = cli.spv1.stores
        company_coll = cli.spv1.companies
        company = company_coll.find_one({'socialCode': lic})
        store = store_coll.find_one({'storeName': company.get('name', '')})
        return store.get('_id')
    except:
        return None


def get_consume_detail(CustomerConsumeNum, License):
    """根据客户销售单号CustomerConsumeNum和License获取消费详情表列表"""
    cli = MongoClient(host='127.0.0.1', port=27017)
    coll = cli.for4c.customerconsumedetail
    query = coll.find({'CustomerConsumeNum': CustomerConsumeNum, 'License': License})
    consume_detail = []
    for doc in query:
        consume_detail.append(doc)
    return consume_detail


def is_valid_vin(vin):
    """判断vin是否有效"""
    if not isinstance(vin, str):
        return False
    kv = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'p': 7, 'r': 9,
        's': 2, 't': 3, 'u': 4, 'v': 5, 'w': 6, 'x': 7, 'y': 8, 'z': 9
    }  # 'q': 8, 无q
    wv = {
        '1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 10,
        '10': 9, '11': 8, '12': 7, '13': 6, '14': 5, '15': 4, '16': 3, '17': 2
    }

    if len(vin) != 17:
        return False
    lowervin = vin.lower()
    verifyCode = lowervin[8]
    if verifyCode < '0' or verifyCode > '9':
        if verifyCode != 'x':
            return False
    total = 0
    for i in range(17):
        if i == 8:
            continue
        code = lowervin[i]
        if code in kv:
            total += kv[code] * wv[str(i + 1)]
        else:
            return False
    res = str(total % 11)
    if verifyCode == 'x':
        return res == 10
    else:
        return res == verifyCode


def is_valid_lic_15(lic):
    """判断15位营业执照有效性,14位数字+1位数据校验码"""
    lic_lower = lic.lower()
    if not re.compile(r'^[0-9]{15}$').findall(lic_lower):
        return False
    x = 10
    total = 0
    for i in range(15):
        total = (x + int(lic_lower[i])) % 10
        if i == 14:
            break
        x = (total * 2) % 11
    return total == 1


def is_valid_lic_18(lic):
    """判断18位营业执照有效性"""
    kv = {'a': 10, 'h': 17, 'r': 25, 'l': 20, '8': 8, '3': 3, 'j': 18, 'q': 24, 'e': 14, 'n': 22,
          'k': 19, '6': 6, '0': 0, '5': 5, '4': 4, '1': 1, '9': 9, 'd': 13, 'u': 27, '7': 7, '2': 2,
          'f': 15, 't': 26, 'w': 28, 'g': 16, 'y': 30, 'p': 23, 'b': 11, 'm': 21, 'c': 12, 'x': 29}
    lic_lower = lic.lower()
    if not re.compile(r'^([159y])([1239])([0-9]{6})([[0-9abcdefghjklmnpqrtuwxy]{10})$').findall(lic_lower):
        return False
    total = 0
    for i in range(17):
        total += kv[lic_lower[i]] * (3 ** i % 31)
    c18 = 31 - (total % 31)
    if c18 == 31:
        c18 = 0
    return c18 == kv[lic_lower[-1]]


def is_valid_license(lic):
    lic_len = len(lic)
    if lic_len != 15 and lic_len != 18:
        return False
    if lic_len == 18:
        if not is_valid_lic_18(lic):  # 长度18位，由大写英文或数字构成
            return False
    if lic_len == 15:
        if not is_valid_lic_15(lic):
            return False
    return True


def upload_data(consume_data):
    """从原始维修单中判断注册维修企业、获取标准化的字段和有效性判断，
    清洗之后获得标准化的数据，上传到暂存的标准数据库
    :param consume_data:维修单数据"""
    time.sleep(2)  # 等待车辆详细信息到库
    # 初步判断，只上传'State'=’完成‘的单
    if consume_data.get('State').strip() != '完成':
        logger.warning('维修单状态 State != 完成')
        return False
    # 获取相关数据
    car_info = get_car_info(consume_data.get('ConsumeCarNum'))
    company_id = get_company_id(consume_data.get('License'))
    store_id = get_store_id(consume_data.get('License'))
    consume_detail_list = get_consume_detail(consume_data.get('CustomerConsumeNum'),
                                             consume_data.get('License'))  # 维修单详细列表

    connect(db='for4c', alias='for4c', host='127.0.0.1', port=27017)  # 测试数据库
    connect(db='spv1', alias='spv1', host='127.0.0.1', port=27017)  # 正式上传的时候数据放到spv1数据库中

    # 获取repairItems列表
    repairitems = []
    repairparts = []
    for doc in consume_detail_list:
        if doc.get('ObjectType') == 'Article':  # 项目
            item = {
                'name': doc.get('ObjectName'),  # 维修项目名称
                'hours': 0,  # 维修工时
                'price': 0,  # 维修工时单价
                'cost': doc.get('TotalPrice', 0)  # 金额
            }
            repairitems.append(item)
        if doc.get('ObjectType') == 'Product':
            part = {
                'name': doc.get('ObjectName'),
                'partNo': '',
                'brand': doc.get('Brand', ''),  # 品牌
                'quantity': doc.get('Qty', 0),  # 配件数量
                'attribute': doc.get('Spec', ''),  # 配件属性
                '_self': False,  # 是否为自备配件  #python关键字self无法用作变量
                'price': doc.get('UnitPrice', 0),  # 单价
                'cost': doc.get('TotalPrice', 0),  # 金额
            }
            repairparts.append(part)

    others = [
        {
            'name': '',  # 其他费用项目名称
            'cost': 0,  # 金额
        },
    ]

    qainfo = {
        'qaMileage': 0,  # 质量保证里程
        'qaDate': 0,  # 质量保证时间
    }
    sum_doc = {
        'cost': consume_data.get('InitialMoney', 0),  # 总费用
        'realCost': consume_data.get('TotalMoney', 0),  # 实收总费用
    }
    default_time = datetime.datetime.utcnow()
    std_data = {
        'plateNo': consume_data.get('ConsumeCarNum', ''),
        'engineNo': car_info.get('EngineNumber', ''),  # 待补充
        'statementNo': consume_data.get('License', '') + consume_data.get('CustomerConsumeNum', ''),  # 结算清单编号=营业执照 + 客户销售单号
        'settlementDate': str_to_date(consume_data.get('ReceivementTime', default_time)),  # 结算日期=收款时间
        'deliveryDate': str_to_date(consume_data.get('GetInTime', default_time)),  # 送修日期=进场时间
        'deliveryMileage': consume_data.get('GetInMileage', 0),  # 送修里程
        'description': consume_data.get('ConsumeContent', ''),  # 故障信息
        'repairItems': repairitems,  # 维修项目列表
        'repairParts': repairparts,  # 维修配件列表
        'others': others,  # 其他费用列表
        'sum': sum_doc,  # 总费用
        'QAInfo': qainfo,  # 质保信息
        'VINCode': car_info.get('VIN'),  # VIN码
        'vehicleOwner': consume_data.get('CarOwnerName', ''),  # 车辆所有者
        'vehicleBrand': car_info.get('CarBrand', ''),  # 车辆品牌 # 待补充
        'vehicleType': 0,  # 车辆类型  原类型：Number
        'repairType': 0,  # 维修类型  原类型：Number
        'repairName': consume_data.get('CarOwnerName', ''),  # 送修人名称
        'repairMobile': car_info.get('ContactInfo', ''),  # 送修人联系方式
        'source': 4,  # 维修表单来源：1:新增，2：上传，3：接口 # 新增4：4C来源
        'status': 0,  # 维修表单是否同步，0:未同步，1：同步
        'integratedRate': 3,  # 表单完整率 0:不合格，1:高，2:中，3:低，
        'companyId': company_id,  # 维修企业
        'xlsxPath': '',  # XLSX文件下载
        'originalXLSXName': '',  # 原xlsx名称
        'xlsxStatus': 1,  # 数据标准化,0: 标准中，1:已标准, 2:标准失败
        'factoryDate': str_to_date(consume_data.get('GetOutTime', default_time)),  # 出厂日期
        'factoryMileage': consume_data.get('GetOutMileage'),  # 出厂里程
        'updated': str_to_date(consume_data.get('updated', default_time)),  # 更新日期
        'created': str_to_date(consume_data.get('created', default_time)),  # 创建日期
        'is_status_fix': 1,  # 非标准数据,0: 未确认，1:已确认， 2:已核对确认
        'store': store_id,  # 关联对应门店
    }

    # 判断车辆信息是否存在，若是则继续，否则舍弃放入标准数据库
    if not car_info:
        logger.warning('没有对应车辆信息，车牌号：%s' % std_data.get('plateNo'))
        return False
    # 验证必要的字段是否存在
    required_fields = ['VINCode', 'plateNo', ]  # 'vehicleBrand', 'deliveryDate', 'factoryDate'
    for key in required_fields:
        if not std_data.get(key):
            logger.warning('缺少必需字段：%s' % key)
            return False
    # 验证营业执照是否有效
    if not is_valid_license(consume_data.get('License')):
        logger.error('无效的营业执照（社会统一信用代码）： %s' % consume_data.get('License'))
        return False
    # 验证vin是否有效
    if not is_valid_vin(std_data.get('VINCode')):  # 判断vin码有效性
        logger.warning('无效的车架号（VIN）: %s' % std_data.get('VINCode'))
        return False
    # 数据保存到临时标准数据表
    try:
        coll = MongoClient()['for4c'].maintenaces  # 临时标准数据表
        coll.insert_one(std_data)  # 储存在临时标准数据库
        std_data.pop('_id')
        logger.info('数据保存成功，数据保存位置：for4c.maintenaces 结算清单编号(statementNo):%s' % std_data.get('statementNo'))
    except Exception as e:
        logger.exception('标准数据保存失败，触发异常：%s' % e)

    # 判断企业是否在后台注册，若是则继续，否则舍弃放入标准数据
    if not company_id:
        logger.warning('丢弃数据，数据库中不存在该维修企业的信息（营业执照）：%s' % consume_data.get('License'))
        return False
    # 上传到正式的标准数据库
    try:
        std_data.pop('_id', '')
        upload_client = MongoClient(host='127.0.0.1', port=27017)
        upload_client[TARGET_UPLOAD_DBNAME].maintenaces.insert_one(std_data)
        logger.info('数据上传成功，结算清单编号(statementNo):%s' % std_data.get('statementNo'))
        return True
    except Exception as e:
        logger.exception('标准数据上传失败，触发异常：%s' % e)
        return False


def to_temp_db_and_upload_data(raw_data):
    """创建新线程，用于标准化数据和上传标准化数据
    :param raw_data:聚合数据
    """
    threading.Thread(target=upload_data, args=(raw_data,)).start()
