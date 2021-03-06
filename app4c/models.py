# -*- coding:utf-8 -*-


from mongoengine import *
import datetime
from .config import TARGET_UPLOAD_DBNAME

class Car(Document):
    meta = {
        'db_alias': 'for4c',
        'collection': 'car',
        'ordering': ['-updated', '-created', '-DataTime'],
        'strict': False,
    }
    ID = StringField()
    Guid = StringField()
    DataTime = StringField()
    CarNum = StringField()
    CarStyleID = IntField()
    CarBrand = StringField()
    CarSery = StringField()
    CarStyle = IntField()
    Price = StringField()
    Color = StringField()
    VIN = StringField()
    EngineNumber = StringField()
    CurrentMileage = IntField()
    Name = StringField()
    CID = IntField()
    ContactInfo = StringField()
    ExpiryDate = StringField()
    BranchStore = StringField()
    InsuranceCompany = StringField()
    InsuranceAmount = IntField()
    InsuranceDate = StringField()
    NameSecond = StringField()
    CIDSecond = IntField()
    NameThree = StringField()
    CIDThree = IntField()
    InsuranceRemindDate = IntField()
    InsuranceRemindSendDate = StringField()
    InsuranceRemindState = StringField()
    InsuranceAutoSend = StringField()
    YearlyinspectionRemindDate = IntField()
    YearlyinspectionRemindSendDate = StringField()
    YearlyinspectionRemindState = StringField()
    YearlyinspectionAutoSend = StringField()
    DriveNoImgOne = StringField()
    DriveNoImgTwo = StringField()
    OtherImgThree = StringField()
    OtherImgFour = StringField()
    OtherImgFive = StringField()
    Remark = StringField()
    ColorNum = StringField()
    ChassisNum = StringField()
    TransmissionNum = StringField()
    License = StringField()
    created = DateTimeField()
    updated = DateTimeField()

    def __str__(self):
        return self.CarNum


class CarOwner(Document):
    meta = {
        'db_alias': 'for4c',
        'collection': 'carowner',
        'ordering': ['-updated', '-created', '-DataTime'],
        'strict': False,
    }
    ID = StringField()
    Guid = StringField()
    DataTime = StringField()
    SID = IntField()
    Stype = StringField()
    StypeInCode = StringField()
    Name = StringField()
    Sex = StringField()
    Address = StringField()
    WeixinState = StringField()
    WeChatNo = StringField()
    CusStaff = StringField()
    CusStaffID = IntField()
    DriveNo = StringField()
    DriveEndTime = StringField()
    SpendPwd = StringField()
    Birthday = StringField()
    Reward = IntField()
    Remark = StringField()
    Phone = StringField()
    AppID = StringField()
    UnitCustomer = StringField()
    ZPhone = StringField()
    DriveNoImgOne = StringField()
    DriveNoImgTwo = StringField()
    CarCard = StringField()
    CarID = IntField()
    CarStyle = StringField()
    CarBrand = StringField()
    CarSery = StringField()
    Color = StringField()
    AllowCar = StringField()
    ExplainsCustomerID = IntField()
    ExplainsCustomer = StringField()
    ClubCard = StringField()
    ClubGrade = StringField()
    ClubGradeID = IntField()
    StoreReward = DecimalField()
    Amount = DecimalField()
    NoAmount = DecimalField()
    Reference = StringField()
    ReferenceID = IntField()
    LatelySpendDataTime = StringField()
    JackpotSpendAmount = DecimalField()
    JackpotSpendMuch = IntField()
    Tab = StringField()
    DriveRemindDate = StringField()
    DriveRemindSendDate = StringField()
    DriveRemindState = StringField()
    DriveAutoSend = StringField()
    CarIDTwo = IntField()
    CarCardTwo = StringField()
    CarIDThree = IntField()
    CarCardThree = StringField()
    FractionState = StringField()
    DriveFractionRemindDateTime = StringField()
    DriveFractionRemindDate = StringField()
    GradeExpireDate = StringField()
    GradeExpireForever = StringField()
    FreeSMSCount = IntField()
    License = StringField()
    created = DateTimeField()
    updated = DateTimeField()

    def __str__(self):
        return self.Name


class CustomerConsume(Document):
    meta = {
        'db_alias': 'for4c',
        'collection': 'customerconsume',
        'ordering': ['-updated', '-created', '-DataTime'],
        'strict': False,
    }
    ID = StringField()
    Guid = StringField()
    DataTime = StringField()
    CustomerConsumeNum = StringField()
    CarOwnerID = StringField()
    CarOwnerName = IntField()
    ConsumeCarID = IntField()
    ConsumeCarNum = StringField()
    ConsumeContent = StringField()
    InitialMoney = DecimalField()
    TotalMoney = DecimalField()
    GetInTime = StringField()
    GetOutTime = StringField()
    GetInMileage = DecimalField()
    GetOutMileage = DecimalField()
    ProductSalesManID = IntField()
    ProductSalesManName = StringField()
    ArticleSalesManID = IntField()
    ArticleSalesManName = StringField()
    ArticleConstructorID = IntField()
    ArticleConstructorName = StringField()
    OrderRemark = StringField()
    UserRemark = StringField()
    EmployeeID = IntField()
    EmployeeName = StringField()
    OrderTime = StringField()
    State = StringField()
    CreateTime = StringField()
    ReceivementTime = StringField()
    BranchStoreID = IntField()
    StationID = StringField()
    StationName = StringField()
    InsuranceID = IntField()
    InsuranceName = StringField()
    ConstructionID = IntField()
    ConstructionName = StringField()
    PriorScrapState = StringField()
    RedConsumeNum = StringField()
    ScrapTime = StringField()
    Stemfrom = StringField()
    IntelligentPeccancyQueryNum = StringField()
    License = StringField()
    created = DateTimeField()
    updated = DateTimeField()

    def __str__(self):
        return self.CustomerConsumeNum


class CustomerConsumeDetail(Document):
    meta = {
        'db_alias': 'for4c',
        'collection': 'customerconsumedetail',
        'ordering': ['-updated', '-created', 'CustomerConsumeID', ],
        'strict': False,
    }
    ID = StringField()
    Guid = StringField()
    DataTime = StringField()
    CustomerConsumeID = IntField()
    CustomerConsumeNum = StringField()
    ObjectType = StringField()
    ObjectID = IntField()
    ObjectName = StringField()
    Brand = StringField()
    Fit = StringField()
    Spec = StringField()
    StockID = IntField()
    StockName = StringField()
    UnitPrice = DecimalField()
    Qty = DecimalField()
    Discount = DecimalField()
    TotalPrice = DecimalField()
    Frequency = IntField()
    DetailType = StringField()
    CarOwnerPackagesID = IntField()
    BranchStoreID = IntField()
    License = StringField()
    created = DateTimeField()
    updated = DateTimeField()

    def __str__(self):
        return self.CustomerConsumeID


class MaintenanceCompany(Document):
    meta = {
        'db_alias': 'for4c',
        'collection': 'companies4c',
        'ordering': ['-updated', '-created', '-DataTime'],
        'strict': False,
    }
    ID = StringField(required=True)
    Guid = StringField()
    DataTime = StringField()
    DBName = StringField()
    StoreName = StringField()
    Address = StringField()
    Registrant = StringField()
    Telephone = StringField()
    Province = StringField()
    City = StringField()
    County = StringField()
    RegisterTime = DateTimeField()
    Range = StringField()
    F2SAmount = StringField()
    License = StringField()
    created = DateTimeField()
    updated = DateTimeField()

    def __str__(self):
        return self.StoreName


class RepairItems(EmbeddedDocument):
    """维修项目"""
    name = StringField()  # 维修项目名称
    hours = DecimalField()  # 维修工时
    price = DecimalField()  # 维修工时单价
    cost = DecimalField()  # 金额

    def __str__(self):
        return self.name


class RepairParts(EmbeddedDocument):
    """维修配件"""
    name = StringField()  # 配件名称
    partNo = StringField()  # 配件编码
    brand = StringField()  # 品牌
    quantity = IntField()  # 配件数量
    attribute = StringField()  # 配件属性
    _self = BooleanField(default=False)  # 是否为自备配件  #python关键字self无法用作变量
    price = DecimalField()  # 单价
    cost = DecimalField()  # 金额

    def __str__(self):
        return self.name


class Others(EmbeddedDocument):
    """其他费用"""
    name = StringField()  # 其他费用项目名称
    cost = DecimalField()  # 金额

    def __str__(self):
        return '%s :%.2f' % (self.name, self.cost)


class Sum(EmbeddedDocument):
    """总费用"""
    cost = DecimalField()  # 总费用
    realCost = DecimalField()  # 实收总费用

    def __str__(self):
        return '总费用：%.2f, 实收总费用：%.2f' % (self.cost, self.realcost)


class QA(EmbeddedDocument):
    """质保信息"""
    qaMileage = IntField()  # "质量保证里程":"100000"
    qaDate = DateTimeField(default=None)  # "质量保证时间":"2019-03-06"

    def __str__(self):
        return '质量保证里程：%d, 质量保证时间：%s' % (self.qaMileage, self.qaDate)


class Company(Document):
    meta = {
        'db_alias': 'spv1',
        'collection': 'companies',
        'strict': False,
    }
    name = StringField(required=True)  # 企业名称
    ID = StringField(required=True)  # 企业系统ID
    businessLicense = StringField()  # 经营许可证
    socialCode = StringField(required=True, unique=True)  # 统一社会信用代码
    address = StringField(required=True)  # 详细地址
    scope = StringField(required=True)  # 经营范围
    businessPhoto = StringField(required=True)  # 营业执照照片url
    licenseNo = StringField()  # 道路运输经营许可证号
    licensePublish = StringField()  # 发证日期
    licenseBegin = StringField()  # 开始日期
    licenseEnd = StringField()  # 结束日期
    roadPhoto = StringField()  # 道理运输许可照片url
    contactName = StringField()  # 企业联系人姓名
    updated = DateTimeField()  # 创建日期
    created = DateTimeField()  # 更新日期
    # 部分字段省略

    def __str__(self):
        return self.name


class Store(Document):
    meta = {
        'db_alias': 'spv1',
        'collection': 'stores',
        'strict': False,
    }
    storeName = StringField(required=True)  # 门店名称
    scope = StringField()  # 门店摘要
    serviceTel = StringField(required=True)  # 客服电话
    zipCode = StringField()  # 邮编
    provinceCode = IntField(required=True)  # 门店省份代码
    cityCode = IntField(required=True)  # 公司市级代码
    countyCode = IntField(required=True)  # 公司县区域代码
    specificAddress = StringField()  # 具体地址
    imgId = ListField(field=DictField)  # 图片ID
    company = ReferenceField(Company)  # 发布信息的用户
    status = IntField(default=1)  # 门店状态，1:营业
    score = IntField()  # 门店评分
    dstCoordinates = DictField()  # 方位
    updated = DateTimeField()  # 创建日期
    created = DateTimeField()  # 更新日期
    distance = IntField()  # 距离

    def __str__(self):
        return self.storeName


class MaintenDoc(Document):
    meta = {
        'db_alias':  TARGET_UPLOAD_DBNAME,
        'collection': 'maintenaces',
        'ordering': ['-updated', '-created', '-DataTime'],
        'strict': False,
    }
    plateNo = StringField(default=None)  # 车牌号码
    engineNo = StringField(default=None)  # 发动机号码
    statementNo = StringField(required=True, unique=True)  # 结算清单编号
    settlementDate = DateTimeField(default=None)  # 结算日期
    deliveryDate = DateTimeField(default=None)  # 送修日期
    deliveryMileage = IntField(default=0)  # 送修里程
    description = StringField(default=None)  # 故障信息
    repairItems = EmbeddedDocumentListField(RepairItems)  # 维修项目列表
    repairParts = EmbeddedDocumentListField(RepairParts)  # 维修配件列表
    others = EmbeddedDocumentListField(Others)  # 其他费用列表
    sum = EmbeddedDocumentField(Sum)  # 总费用
    QAInfo = EmbeddedDocumentField(QA)  # 质保信息
    VINCode = StringField(default=None)  # VIN码
    vehicleOwner = StringField(default=None)  # 车辆所有者
    vehicleBrand = StringField(default='')  # 车辆品牌
    vehicleType = IntField(default=None)  # 车辆类型  原类型：Number
    repairType = IntField(default=None)  # 维修类型  原类型：Number
    repairName = StringField(default=None)  # 送修人名称
    repairMobile = StringField(default=None)  # 送修人联系方式
    source = IntField(default=4)  # 维修表单来源：1:新增，2：上传，3：接口 # 新增4：4C来源
    status = IntField(default=0)  # 维修表单是否同步，0:未同步，1：同步
    integratedRate = IntField(default=3)  # 表单完整率 0:不合格，1:高，2:中，3:低，
    companyId = ReferenceField(Company)  # 维修企业
    xlsxPath = StringField(default=None)  # XLSX文件下载
    originalXLSXName = StringField(default=None)  # 原xlsx名称
    xlsxStatus = IntField(default=None)  # 数据标准化,0: 标准中，1:已标准, 2:标准失败
    factoryDate = DateTimeField(default=None)  # 出厂日期
    factoryMileage = IntField(default=0)  # 出厂里程
    updated = DateTimeField(default=datetime.datetime.utcnow())  # 更新日期
    created = DateTimeField(default=datetime.datetime.utcnow())  # 创建日期
    is_status_fix = IntField(default=0)  # 非标准数据,0: 未确认，1:已确认， 2:已核对确认
    store = ReferenceField(Store)  # 关联对应门店

    def __str__(self):
        return self.plateNo
