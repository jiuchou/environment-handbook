# JavaScript


## 第一部分 样式

### 0 扉页

* 字体
  * [如何优雅的选择字体(font-family)](https://segmentfault.com/a/1190000006110417)
* 布局

  * 经典布局网站： https://adminlte.io/
  * 页面布局的几点建议，来自vue-element-admin： https://github.com/PanJiaChen/vue-element-admin/issues/1085
  * CSS Grid 系列(上)-Grid布局完整指南： https://segmentfault.com/a/1190000012889793
* ECMAScript
  * [ES6 基础](https://www.cnblogs.com/libin-1/p/6716470.html)
* Webpack 构建
  * webpack 升级: https://blog.csdn.net/qq_25243451/article/details/80331269
  * webpack4 入门: https://blog.csdn.net/MessageBox_/article/details/81325034
  * https://blog.csdn.net/qq_27184497/article/details/84592953

### 1 网页标题栏添加favicon.ico图标

#### 1.1 favicon.ico图标文件制作

> 建议图标大小为 `16*16` 或 `32*32`
>
> 根据实际测试，超过 32x32 的 favicon.ico 图标，不但效果没有明显改变，而且还会导致某些浏览器无法展示。而且之前的谷歌网站图标缓存服务器，超过 16kb 就不会缓存，而是直接展示默认的图标。而 **16x16** **和 32x32** **的网站图标，实际展示在浏览器标签栏的效果也没有很明显的区别**。
>
> 所以，对于网站 favicon.ico 图标的大小，建议大家选择 16x16 或者 32x32，再大也是完全没有必要的。效果不见涨，还可能会影响网站速度。
>
> （以上说明内容转载自 [关于网站图标favicon.ico那点事儿](https://zhang.ge/4344.html)）

1.准备好合适的图标图片文件

2.使用 `在线ico图标转换工具` 制作图标文件

可用 `在线ico图标转换工具` 推荐：

* http://www.faviconico.org/
* http://www.bitbug.net/
* https://www.favicon.cc/

#### 1.2 favicon.ico图标不显示

* https://blog.csdn.net/huihui940630/article/details/80318889

##### 1.2.1 部署问题

**背景**

​	django+vue前后端分离项目，内部项目，无域名。

​	favicon.ico配置如下：

​		1.favicon.ico放置在public目录下

​		2.在入口文件 `public/index.html` 中使用如下方式调用 `<link rel="icon" href="/favicon.ico">`

**现象**

​	使用 `npm run dev` 进行前端测试时显示正常，使用 `npm run build` 打包后，将生成文件部署至Django项目中，无法显示。

**原因**

​	没有配置域名，当以绝对路径访问项目时，不能正常引入favicon.ico

**解决方案**

​	**方案一** 配置域名（如果暂时无配置域名计划，可使用方案一）

​	**方案二** 将favicon.ico放在static目录下，然后在入口文件 `public/index.html` 中使用如下方式调用

```html
<link rel="icon" href="/static/favicon.ico">
```

##### 1.2.2 缓存问题

> 暂无案例
>
> **原因**
>
> ​	可能是浏览器缓存的问题，只要清除浏览器缓存就好

##### 1.2.3 路径错误

> 暂无案例
>
> **原因**
>
> ​	图标文件 `favicon.ico` 路径出错，找到 `favicon.ico` 绝对路径如能正常显示，则为引入图标时路径出错

## 待整理

### webpack

* Webpack 4 和单页应用入门
  * https://github.com/wallstreetcn/webpack-and-spa-guide
* [官方文档](https://webpack.js.org/concepts)



待制作思维导图
错误处理机制 https://wangdoc.com/javascript/features/error.html
Error对象
  Error的6个派生对象
    SyntaxError 
    ReferenceError 
    RangeError 
    TypeError 
    URIError 
    EvalError （该错误类型已经不再使用了，只是为了保证与以前代码兼容，才继续保留）
  自定义错误对象

switch...case 结构
https://wangdoc.com/javascript/features/style.html


帮你彻底搞懂JS中的prototype、__proto__与constructor（图解）
https://blog.csdn.net/cc18868876837/article/details/81211729





扩展
AJAX，即Asynchronous Javascript And XML，介绍https://baike.baidu.com/item/ajax/8425?fr=aladdin

JavaScript中文网
https://www.javascriptcn.com/read-62382.html

vue.js文档
https://cn.vuejs.org/v2/guide/syntax.html

http://wiki.commonjs.org/wiki/CommonJS
grunt
https://gruntjs.com/who-uses-grunt

development stack
正则表达式
教程
常用
语言使用方式
  shell
  java
  JavaScript
  数据库
  Python
  Jenkins
    Jenkins权限视图Pattern只想包含某字段开头且不包含另外字段的内容(Project_ProjectName_X)
      Project_((?!ProjectName_1|ProjectName_2|ProjectName_3).)*