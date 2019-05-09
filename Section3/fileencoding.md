# 文件编码

<!-- TOC -->

- [文件编码](#文件编码)
    - [1 Linux 处理编码](#1-linux-处理编码)
        - [1.1 查看文件编码](#11-查看文件编码)
        - [1.2 转换文件编码：使用 `iconv`](#12-转换文件编码使用-iconv)
        - [1.3 特殊场景说明](#13-特殊场景说明)
            - [1.3.1 `vim` 显示中文乱码解决方法](#131-vim-显示中文乱码解决方法)
                - [1.3.1.1 `vim` 打开对应编码格式文件](#1311-vim-打开对应编码格式文件)
                - [1.3.1.2 `vim` 配置 `~/.vimrc` 或 `/etc/vim/vimrc`](#1312-vim-配置-vimrc-或-etcvimvimrc)
                - [1.3.1.3 使用 `iconv`](#1313-使用-iconv)
    - [2 Python 处理编码](#2-python-处理编码)
    - [3 更新说明](#3-更新说明)

<!-- /TOC -->

## 1 Linux 处理编码

- 扩展
  - [GBK 编码](https://www.qqxiuzi.cn/zh/hanzi-gbk-bianma.php)

### 1.1 查看文件编码

1. 命令行使用 `file -i filename` 查看文件编码
2. 命令行使用 `vim` 打开文件，使用 `:set fileencoding` 查看

### 1.2 转换文件编码：使用 `iconv`

```bash
# iconv -f GBK 待转码文件名 -o 输出文件名
iconv -f GBK -t UTF-8 待转码文件名 -o 输出文件名
```

### 1.3 特殊场景说明

#### 1.3.1 `vim` 显示中文乱码解决方法

文件编码为 `ISO-8859-1` 并且含有中文字符的文件，在 `vim` 及其他文件读取时存在中文乱码的问题。

##### 1.3.1.1 `vim` 打开对应编码格式文件

```bash
# 参考 http://www.cnblogs.com/sparkbj/p/6212427.html
vim -c "e ++enc=GBK" filename
```

##### 1.3.1.2 `vim` 配置 `~/.vimrc` 或 `/etc/vim/vimrc`

> 在使用 `vim` 打开文件类型为 `ISO-8859 text` 的文件时，里面的中文是乱码，这是因为 `vim` 不能自动识别文件的编码类型，需要修改vim的配置，可以修改 `/etc/vim/vimrc(全局模式)`，也可以修改 `~/.vimrc(当前用户)`。

```bash
# 参考 http://blog.chinaunix.net/uid-14753126-id-2981712.html
set fencs=utf-8,GB18030,ucs-bom,default,latin1
```

或

```bash
# 参考 https://blog.csdn.net/z1134145881/article/details/46832685
set fileencodings=utf-8,gb2312,gbk,gb18030
set termencoding=utf-8
set fileformats=unix
set encoding=prc
```

或`（未验证）

```
set encoding=utf-8
set fileencoding=utf-8
```

##### 1.3.1.3 使用 `iconv`

```bash
# iconv -f GBK oldFilename -o newFilename
iconv -f GBK -t UTF-8 oldFilename -o newFilename
```

## 2 Python 处理编码

> 扩展
> 使用chardet检查字符串编码
> https://chardet.readthedocs.io/en/latest/index.html

在Python2.7脚本中，读取编码为 `iso-8859-1` 且包含中文内容的文件时，通过chardet获取字符串编码内容如下

```python
import chardet
f = open(filename, 'r')
output = f.read()
print chardet(outpt)
# {'confidence': 0.6466081639234461, 'language': '', 'encoding': 'ISO-8859-1'}
```

可使用如下方式将字符串内容转为utf-8编码后正常显示

```python
output_1 = output.decode("gbk", 'ignore').encode('utf8')
print output_1
print chardet(output_1)
# {'confidence': 0.40148270516097284, 'language': 'Turkish', 'encoding': 'Windows-1254'}
```

在Python2.7命令行中，读取编码为 `iso-8859-1` 且包含中文内容的文件时，通过chardet获取字符串编码内容如下

```
{'confidence': 0.6159047963522948, 'encoding': 'ISO-8859-2'}
```

可使用如下方式将字符串内容转为utf-8编码后正常显示

```python
>>> o1 = output.decode("gbk", 'ignore').encode('utf8')
>>> print o1
```

## 3 更新说明

```
2019.02.24: 开始整理，增加编码ISO-8859-1的文件中中文字符显示异常的说明
2019.05.09: 增加Linux和Python场景中文件编码的处理方式
```

