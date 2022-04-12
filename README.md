# Cooler
各位参与Cooler早期开发的同学们注意，Cooler处于前期的不稳定状态，请勿公开源代码！  

## 安装
cooler目前仅支持docker安装，官方镜像在`ghcr.io/cooler-dev/cooler:alpha`，使用docker部署时的初始用户名和密码均为`admin`，安装后请修改密码
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
