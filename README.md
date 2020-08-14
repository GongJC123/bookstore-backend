python版本
- python 3.7

django版本
- django = "==2.2.10"

drf相关依赖
- djangorestframework = "*"
- markdown = "*"
- pillow = "*"
- drf过滤
    - django-filter = "==2.1.0"

mysql依赖
- pymysql = "*"

xadmin依赖
- future 0.17.1
- django-crispy-forms 1.8.1
- django-formtools 2.2
- httplib2 0.13.0
- django-import-export 2.0
 
drf文档支持
- coreapi 2.3.3 

drf对象级别的权限支持
- django-guardian 2.0.0 未安装

drf递归序列化
- djangorestframework-recursive

## todo（未完成）

- 搜索 (现在是名称搜索，可扩展)
- 评论 (前端显示的时间有点问题)
- 用户注册，登录 

## 部署
1. 复制到服务器上
2. 安装虚拟环境，修改python版本
3. 激活/切换虚拟环境
4. 新建数据库
5. 收集静态文件
6. 数据迁移
7. 安装uwsgi，配置，测试
8. 安装nginx， 部署，测试
