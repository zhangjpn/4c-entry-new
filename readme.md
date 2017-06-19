端口：3503

4c平台上传接口：
    http://example.com/4c/

部署
    1、将app/config.py的DEBUG修改成False
    2、将app/__init__.py内的init_admin函数注释掉
    3、将config.py下的TARGET_UPLOAD_DBNAME从for4h指向spv1
    4、创建虚拟环境：virtualenv -p /usr/bin/python3 venvfor4c
    5、转到api4c文件夹下，使用虚拟环境执行下述命令
        gunicorn -w 1 -b 127.0.0.1:3503 -D --log-syslog-prefix /var/log --access-logfile for4c.log wsgi:application
        如果不是root权限 --log-syslog-prefix /var/log无效 忽略该参数，默认log在当前文件夹内

接口说明：
    暂存数据库：for4c
    车辆信息collection:car
    车主信息collection:carowner
    车辆消费信息（主表）collection:customerconsume
    车辆消费信息（从表）collection:customerconsumedetail


    >创建车辆信息：http://example.com/4c/car/create/
        方法：post
        参数：{ 数据库相应字段  CarNum:.... Guid。。。。。 }
        说明：必填字段CarNum

    >更新车辆信息：http://example.com/4c/car/update/
        方法：post
        参数：{ 数据库相应字段 CarNum:.... 。。。。。 }
        说明：必填字段CarNum

    >查询车辆信息：http://example.com/4c/car/list
        方法：get
        参数：page=1,rows=10



    >创建车主信息：http://example.com/4c/carowner/create/
        方法：post
        参数：{ 数据库相应字段 Name:,SID:,DriveNo:...}
        说明：必填字段DriveNo
        返回：
            成功：'message':'success','item':写入的数据,200
            失败：'message':'failed','reason':'invalid data',400

    >更新车主信息：http://example.com/4c/carowner/update/
        方法：post
        参数：{ 数据库相应字段 Name:'',SID:,DriveNo:...}
        说明：必填字段DriveNo
        返回：
            成功：'message':'success','item':写入的数据,200
            失败：'message':'failed','reason':'invalid data',400

    >查询车主信息：http://example.com/4c/carowner/list
        方法：get
        参数：page=1,rows=10
        返回：
            成功：'message':'success','data':数据,200
            失败：'message':'failed','reason':'invalid arguments',400


    >创建客户消费信息：http://example.com/4c/customer/consume/create/
        方法：post
        参数：{ 数据库相应字段  CustomerConsumeNum:,CarOwnerID:...}
        说明：必填字段CustomerConsumeNum
        返回：
            成功：'message':'success','item':写入的数据,200
            失败：'message':'failed','reason':'invalid data',400

    >更新客户消费信息：http://example.com/4c/customer/consume/update/
        方法：post
        参数：{ 数据库相应字段  CustomerConsumeNum:,CarOwnerID:...}
        说明：必填字段CustomerConsumeNum
        返回：
            成功：'message':'success','item':原始数据,200
            失败：'message':'failed','reason':'invalid data',400

    >查询客户消费信息：http://example.com/4c/customer/consume/list
        方法：get
        参数：page=1,rows=10
        返回：
            成功：'message':'success','data':数据,200
            失败：'message':'failed','reason':'invalid arguments',400

    >创建消费详细信息：http://example.com/4c/customer/consume/detail/create/
        方法：post
        参数：{ 数据库相应字段 CustomerConsumeNum:,CustomerConsumeID:... }
        说明：必填字段CustomerConsumeNum
        返回：
            成功：'message':'success','item':写入的数据,200
            失败：'message':'failed','reason':'invalid data',400

    >更新消费详细信息：http://example.com/4c/customer/consume/detail/update/
        方法：post
        参数：{ 数据库相应字段 CustomerConsumeNum:,CustomerConsumeID:... }
        说明：必填字段CustomerConsumeNum
        返回：
            成功：'message':'success','item':原始数据,200
            失败：'message':'failed','reason':'invalid data',400

    >查询消费详细信息：http://example.com/4c/customer/consume/detail/list
        方法：get
        参数：page=1,rows=10
        返回：
            成功：'message':'success','data':数据,200
            失败：'message':'failed','reason':'invalid arguments',400