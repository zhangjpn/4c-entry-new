# -*- coding:utf-8 -*-


from flask_admin import Admin
from app4c.fields import *
from flask_admin.contrib.mongoengine import ModelView
from app4c.models import *
from mongoengine import connect


# 视图函数
class CompanyView(ModelView):
    column_filters = ['StoreName', 'Registrant', 'created', 'updated']
    column_labels = COMPANY_FIELD
    can_set_page_size = True
    can_delete = False
    can_create = False
    can_edit = False
    can_view_details = True
    can_export = True
    column_list = SHOW_COMPANY_COLUMN


class CarView(ModelView):
    # http://flask-admin.readthedocs.io/en/latest/introduction/ for more information
    column_filters = []
    can_create = False
    can_edit = False
    can_delete = False
    can_view_details = True
    can_export = True
    column_labels = CAR_FIELD
    column_list = SHOW_CAR_COLUMN


class CarOwnerView(ModelView):
    column_filters = ['Name', 'created', 'updated']
    column_labels = CAROWNER_FIELD
    can_set_page_size = True
    can_delete = False
    can_create = False
    can_edit = False
    can_view_details = True
    can_export = True
    column_list = SHOW_CAROWNER_COLUMN


class CustomerConsumeView(ModelView):
    column_filters = ['CustomerConsumeNum', 'created', 'updated']
    column_labels = CUSTOMER_CONSUME_FIELD
    can_set_page_size = True
    can_delete = False
    can_create = False
    can_edit = False
    can_view_details = True
    can_export = True
    column_list = SHOW_CUSTOMERCONSUME_COLUMN


class CustomerConsumeDetailView(ModelView):
    column_filters = ['CustomerConsumeID', 'created', 'updated']
    column_labels = CUSTOMER_CONSUME_DETAIL_FIELD
    can_set_page_size = True
    can_delete = False
    can_create = False
    can_edit = False
    can_view_details = True
    can_export = True
    column_list = SHOW_CUSTOMERCONSUME_DETAIL_COLUMN


class StandardView(ModelView):
    list_template = "admin/model/list_template.html"
    # column_filters = ['ID', 'Guid', 'DataTime']
    column_labels = STANDARD_DATA_FIELD
    can_set_page_size = True
    can_delete = False
    can_create = False
    can_edit = False
    can_view_details = True
    can_export = True
    column_list = SHOW_STD_DATA_COLUMN


# 后台管理
def admin_init_app():
    connect(db='spv1', alias='spv1', host='127.0.0.1', port=27017)  # 暂存数据库
    connect(db='for4c', alias='for4c', host='127.0.0.1', port=27017)  # 暂存数据库
    admin = Admin(name='4C门店后台数据管理', url='/4c/admin')
    admin.add_view(CarView(Car, name='车辆信息'))
    admin.add_view(CarOwnerView(CarOwner, '车主信息'))
    admin.add_view(CustomerConsumeView(CustomerConsume, name='维修信息'))
    admin.add_view(CustomerConsumeDetailView(CustomerConsumeDetail, name='维修详情'))
    admin.add_view(CompanyView(MaintenanceCompany, name='维修企业信息'))
    admin.add_view(StandardView(MaintenDoc, name='标准数据'))
    return admin
