# django-api-server

pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install djangorestframework -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django-rest-swagger -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyjwt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django-cors-headers

python manage.py startapp posts
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

python manage.py shell
from django.contrib.auth.models import User 
user = User.objects.get(username='admin') 
user.set_password('admin') 
user.save()

超级管理员
insert into backend_user (id,username,password,rid,state,create_time,mobile,email,deleted,delete_time) values (1,'admin','YWRtaW4xMjM=',1,True,'2020-04-12 16:44:34','13811111111','admin@shop.com',False,null);

权限：
insert into backend_right (id,name,pid,controler,action,level) values ('101','权限管理','0','','','0');
insert into backend_right (id,name,pid,controler,action,level) values ('121','角色列表','101','Role','index','1');
insert into backend_right (id,name,pid,controler,action,level) values ('141','添加角色','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('142','删除角色','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('143','角色授权','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('144','取消角色授权','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('145','获取角色列表','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('146','获取角色详情','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('147','更新角色信息','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('148','更新角色权限','121','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('122','权限列表','101','Right','index','1');
insert into backend_right (id,name,pid,controler,action,level) values ('149','查看权限','122','','','2');

insert into backend_right (id,name,pid,controler,action,level) values ('102','用户管理','0','','','0');
insert into backend_right (id,name,pid,controler,action,level) values ('123','用户列表','102','User','index','1');
insert into backend_right (id,name,pid,controler,action,level) values ('150','添加用户','123','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('151','删除用户','123','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('152','更新用户','123','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('153','获取用户详情','123','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('154','分配用户角色','123','','','2');
insert into backend_right (id,name,pid,controler,action,level) values ('155','设置用户状态','123','','','2');

角色：
insert into backend_role(id,role_name,ids,controler_action,role_desc,create_time,deleted,delete_time) values (1,'超级管理员','101,121,141,142,143,144,145,146,147,148,122,149,102,123,150,151,152,153,154,155,123,150,151,152,153,154,155',null,'超级管理员','2020-04-12 16:44:34',False,null);
