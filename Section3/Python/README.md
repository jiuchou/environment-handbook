# Python

**python 字符串比较忽略大小写的方法**

1. 正则表达式，使用IGNORECASE标志

```python
>>> import re
>>> m = re.search('multi', 'A mUltiCased string', re.IGNORECASE)
>>> bool(m)
True
```

2. 在比较前把2个字符串转换成同样大写，用upper()方法，或小写,lower()

```python
>>> s = 'A mUltiCased string'.lower()
>>> s
'a multicased string'
>>> s.find('multi')
2
```

**去除字符串 `strings` 中的重复字段**

```python
>>> ','.join(set(strings.replace(' ', '').split(',')))
```



**Python**

* [Python 发送邮件](https://blog.csdn.net/ywjun0919/article/details/53166976)
* [Python邮件发送之HTML表格快速建立](https://blog.csdn.net/u012111465/article/details/82713561)



**Jinja2**

* http://docs.jinkan.org/docs/jinja2/



## 1 Python 使用数据库

* https://www.jb51.net/article/135293.htm

### 1.1 错误记录

**python2.7 使用MySQL-python错误记录**

`fatal error: Python.h: No such file or directory` 

解决办法

```bash
apt-get install python-dev
```

**python 安装MySQLdb错误记录**

`mysql_config not fount`

解决方法

```bash
apt-get install libmysqlclient-dev
```



## 2 第三方库

### 2.1 codecs

* [python模块之codecs](https://www.cnblogs.com/misswangxing/p/8603529.html)

### 2.2 hashlib

### 2.3 ConfigParse

### 2.4 logger

## 3 待整理

### 项目发布

```bash
# 打包生成源码安装包
python setup.py dist
# 打包生成wheel包
python setup.py bdist_wheel
```

### 包操作

```bash
python -m pip install package
python -m pip uninstall package
python -m pip show package
python -m pip list
```





## 3 待整理

### 3.1 软件安装

#### 3.1.1 python2.7 安装 `mysqlclient` 

##### 3.1.1.1 报错： `EnvironmentError: mysql_config not found`

原因：机器未包含MySQL依赖

**Ubuntu**

```bash
# apt-get/dpkg: Ubuntu（未验证）
apt-get install libmysqld-dev
apt-get install libmysqlclient-dev
```

**CentOS**

```bash
# yum/rpm: CentOS
# 包名： mariadb-devel-5.5.60-1.el7_5.x86_64
yum install mysql-devel
```

##### 3.1.1.2 报错 `MySQLdb/_mysql.c:37:20: fatal error: Python.h: No such file or directory`

原因：机器未安装Python开发库

```bash
# apt-get/dpkg: Ubuntu
apt-get install python-dev
# yum/rpm: CentOS
yum install python-devel
```

### 3.1.2 Windows pip安装报错

**报错信息**

```bash
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
```

**解决方案**

下载安装 `build tools`

* 下载地址： https://go.microsoft.com/fwlink/?LinkId=691126

