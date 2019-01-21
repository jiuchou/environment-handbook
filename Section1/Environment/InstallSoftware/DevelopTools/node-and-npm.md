# 1.2.1.1 node和npm

## 1 安装

下载地址: https://nodejs.org/en/

### 1.1 Windows

1.安装

下载nodejs安装包，按照windows系统安装软件方式安装软件即可。

最新版本的nodejs包含npm，无需额外安装。

2.环境变量

### 1.2 Linux

#### 1.2.1 Ubuntu14.04

## 2 记录

### 2.1 npm问题

#### 2.1.1 npm install失败

1.npm install

- 参考内容

  - [npm install问题](https://segmentfault.com/a/1190000008474798)

  1)报错信息

  ```
  npm ERR! phantomjs-prebuilt@2.1.14 install: `node install.js`
  
  npm ERR! Exit status 1
  
  npm ERR!
  
  npm ERR! Failed at the phantomjs-prebuilt@2.1.14 install script 'node install.js
  ```

  2)解决方案

  `在命令后加参数 --ignore-scripts`

  ```
  npm install --ignore-scripts
  ```

2.npm install node-sass error

- 参考内容

  - [node-sass软件地址](https://github.com/sass/node-sass/releases)
  - []()

  (1)报错信息

  (2)解决方案

  ```
  wget https://github.com/sass/node-sass/releases/download/v4.10.0/linux-x64-64_binding.node
  export SASS_BINARY_PATH=linux-x64-64_binding.node
  npm install node-sass --save-dev
  ```