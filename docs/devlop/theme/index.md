# 使用html开发Cooler主题
Cooler使用Django开发，所以，主题开发需遵循Django的模板语法，您可以直接编写html，也可以使用第三方框架，如：`vue`，`react`等，但请确保构建后的主题文件存放在`templates`目录内。

## 主题文件结构
```text
.
├── footer.html
├── head.html
├── header.html
├── home.html
└── post.html
```
- `footer`: 页脚内容，请保留Powered by Cooler。
- `head`: head标签内的内容，用于引用`css`、`js`等所需文件。
- `header`: 此文件中内容会显示在每个页面的正上方，可以编写菜单。
- `home`: 主页文件。
- `post`: 文章详情页面。

## 可用的变量名称

### home.html

#### posts
- posts.id: 用于获取文章的id。
- posts.title: 获取文章的标题。
- posts.body: 文章的正文部分，引用时请附带`safe`参数，以保证富文本内容的正确加载。

#### meta
- meta.title: 站点的标题
- meta.author: 站点的作者

### post.html
- posts.title: 文章的标题。
- meta.title: 站点的标题。
以上用于在head标签内引用，以下用于在body内引用，请勿混淆。
- name: 文章的标题
- body: 文章的正文，在引用时请以这种方式引用，避免富文本与代码高亮出现错误。
```html
{{ body | safe | linebreaksbr }}
```

### header.html
我们并未向header.html传入任何上文。

### head.html
我们向head.html传入了站点元信息，用法请见[home.html > meta](index.md#meta)

### footer.html
我们并未向footer.html传入任何上文。

## 建议
1. 在引用css等静态资源时，请尽量引用cdn内的内容，避免与Cooler后台、代码高亮等功能所使用的静态资源产生冲突，以至不可估量的后果。
2. Cooler正处于早期开发中，传入模板的上文可能会有所改变，所以旧版本的主题可能不适用于新版本。
