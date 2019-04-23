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




