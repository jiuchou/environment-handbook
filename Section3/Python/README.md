# Python



## 1 Python包操作

```bash
python -m pip install package
python -m pip uninstall package
python -m pip show package
python -m pip list
```

### 1.1 Windows pip安装报错

**报错信息**

```bash
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
```

**解决方案**

下载安装 `build tools`

- 下载地址： https://go.microsoft.com/fwlink/?LinkId=691126



## 2 内置方法

### 2.1 os.environ 和 os.getenv() 的区别

* os.environ(x [,x])

  raises an exception if the environmental variable does not exist.

* os.getenv(x)

  does not raise an exception ,but returns None.

### 2.2 python 字符串比较忽略大小写的方法

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

### 2.3 去除字符串 `strings` 中的重复字段

```python
>>> ','.join(set(strings.replace(' ', '').split(',')))
```

### 2.4 判断字符串是否全是字母或数字

* [Python判断字符串是否全是字母或数字](https://www.cnblogs.com/liuyihua1992/p/9649739.html)

```python
# True if 只包含数字，otherwise False（此函数只能用于unicode string）
str.isnumeric()
# True if 只包含数字，otherwise False
str.isdigit()
# True if 只包含字母，otherwise False
str.isalpha()
# True if 只包含数字或字母，otherwise False
str.isalnum()
```



### 2.5 发送邮件

- [Python 发送邮件](https://blog.csdn.net/ywjun0919/article/details/53166976)
- [Python邮件发送之HTML表格快速建立](https://blog.csdn.net/u012111465/article/details/82713561)

### 2.6 python文件处理

#### 2.6.1 替换文件中的指定字符串

* https://blog.csdn.net/alittleyatou/article/details/84318600

#### 2.6.2 使用wget下载网络文件

* https://blog.csdn.net/dcrmg/article/details/79580365

## 3 第三方库

### 3.1 codecs

- [python模块之codecs](https://www.cnblogs.com/misswangxing/p/8603529.html)

### 3.2 hashlib

### 3.3 ConfigParse

### 3.4 logger

### 3.5 Jinja2

* http://docs.jinkan.org/docs/jinja2/

### 3.6 Python连接MySQL数据库

#### 3.6.1 使用python-mysql

> 适用版本：
>
> ​	Python2.7

##### 3.6.1.1 使用方法

* https://www.jb51.net/article/135293.htm

##### 3.6.1.2 错误记录

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

#### 3.6.2 使用mysqlclient

##### 3.6.2.1 使用方法

##### 3.6.2.2 错误记录

###### 3.6.2.2.1 python2.7 安装 `mysqlclient` 报错

**1）报错： `EnvironmentError: mysql_config not found`**

**原因**：机器未包含MySQL依赖

**解决方案**

* Ubuntu

  ```bash
  # apt-get/dpkg: Ubuntu（未验证）
  apt-get install libmysqld-dev
  apt-get install libmysqlclient-dev
  ```

* CentOS

  ```bash
  # yum/rpm: CentOS
  # 包名： mariadb-devel-5.5.60-1.el7_5.x86_64
  yum install mysql-devel
  ```

**2）报错 `MySQLdb/_mysql.c:37:20: fatal error: Python.h: No such file or directory`**

**原因**：机器未安装Python开发库

**解决方案**

```bash
# apt-get/dpkg: Ubuntu
apt-get install python-dev
# yum/rpm: CentOS
yum install python-devel
```

### 3.7 操作xlsx

> * https://www.cnblogs.com/cmt110/p/7464944.html

```bash
pip install openpyxl
```

```python
>>> import openpyxl
>>> workbook = openpyxl.load_workbook('dept.xlsx')
>>> worksheet = workbook.get_sheet_by_name('Sheet1')
>>> for item in list(worksheet.columns)[0]:
...     print(item.value, item.row)
```

## 4 项目发布

```bash
# 打包生成源码安装包
python setup.py dist
# 打包生成wheel包
python setup.py bdist_wheel
```

