# Cooler
## 部署
### docker部署（推荐）
拉取镜像`ghcr.io/cooler-dev/cooler`，运行镜像，如果应用在生产环境，请配置服务器上的反向代理。  
运行后即可登录后台，默认账户与密码均为`admin`
### 源码部署（不推荐）
从发行版下载源代码，在根目录执行:
```bash
pip install django==3.2
python manage.py migrate
```
然后使用此命令创建管理员账号：
```bash
python manage.py createsuperuser
```
之后通过此命令运行服务器：
```bash
python manage.py runserver
```
最后使用反向代理到`127.0.0.1:8000`
## 目录结构解析
懒得写了
## 代码风格要求
使用PEP 8风格的代码
## commit信息规范
每次commit信息由以下部分组成：
```text
<类型>: 注释
```
有以下类型可选
A: 即add，增加新功能时使用  
R: 即remove，删除功能时使用  
F: 即fix，修复bug时使用  
D: 即doc，修改文档时使用  
注释为此次修改的简短描述
示例：
```text
A: 增加了自动更新功能
```
