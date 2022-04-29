# 使用vue开发
> 本教程讲讲解如何使用vue开发Cooler主题
## 项目结构
项目结构请参考[`主题文件结构`](./index.md#主题文件结构)
## 构建
删除'templetas'文件夹内的所有内容，将主题的vue工程存放到theme文件夹内，并且在`vue.config.js`内中设置构建输出目录到`templates`:
```js
module.exports = {
  outputDir:'../templates'
}
```
即可完成设置。
## 可用的变量名称
请见[使用html > 可用的变量名称](index.md#可用的变量名称)
