# JavaScript

* UpdateTime: 2019.08.16

## 第一部分 nodejs的安装及配置

下载地址：https://nodejs.org/zh-cn/download/

### 0 Linux

#### 0.1 源码编译安装

**下载**

```bash
wget https://nodejs.org/dist/v10.16.2/node-v10.16.2.tar.gz
```

#### 0.2 二进制安装

```bash
wget https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz
tar xf node-v10.16.3-linux-x64.tar.xz
cd /usr/local/bin
ln -s /usr/local/src/node-v10.16.3-linux-x64/bin/npm
ln -s /usr/local/src/node-v10.16.3-linux-x64/bin/node
```

#### 0.3 通过nvm安装（推荐）

详细安装参考官方安装指南：https://github.com/nvm-sh/nvm#installation

1. 安装nvm

   ```bash
   # 推荐
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
   # 或者
   # wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
   # 启用
   source ~/.bashrc
   ```

2. 使用

   由于nvm自带的nodejs版本是最新开发版本，即当前的v12.8.1版本。

   由于日常使用稳定版本进行开发，所以想要使用期望的nodejs版本需要进行安装。当前最新稳定版本为v10.16.2，本文档使用此版本记录。

   ```bash
   # 安装nodejs版本
   nvm install v10.16.2
   # 切换版本
   nvm use v10.16.2
   # v10.16.2
   node -v
   # 6.9.0
   npm -v
   ```

   默认情况下，The script clones the nvm repository to `~/.nvm` and adds the source line to your profile (`~/.bash_profile`, `~/.zshrc`, `~/.profile`, or `~/.bashrc`).

   由于使用Ubuntu18.04的gnome桌面打开终端是一种非登录式shell（配置文件执行顺序：~/.bashrc--> /etc/bashrc--> /etc/profile.d/*.sh）。每次打开终端时，nodejs版本会使用默认的v12.8.1版本。

   修改~/.bashrc文件，增加切换nodejs版本内容：

   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
   [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
   # 增加此行
   nvm use v10.16.2
   ```

#### 0.4 配置npm

* 指定全局安装路径和缓存路径

  > 使用nvm安装方式时，不设置，默认安装路径为 `/home/jiuchou/.nvm/versions/node/v10.16.2/lib/node_modules`

  ```bash
  # 设置全局模块的安装路径到 `node_global` 文件夹 
  npm config set prefix /home/jiuchou/EnvironmentRely/nodejs/node_global
  # 设置缓存到 `node_cache` 文件夹
  npm config set cache /home/jiuchou/EnvironmentRely/nodejs/node_cache
  # 验证是否配置成功
  npm config get cache
  npm ls -g
  ```

* 使用淘宝镜像站`(建议跳过此步骤，不建议使用)`

* 安装 cnpm（根据个人需求）

  ```bash
  npm install cnpm -g --registry=https://registry.npm.taobao.org
  ```

### 1 Windows


## 第二部分 样式

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

### 2 鼠标放在文字上显示文字

```javascript
<a href="#" title="这里是显示的文字">hello</a>
```

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