# Django框架



## 2 Django框架内置包


### 2.1 Django models.Model

#### 2.1.1 QuerySet

> * 有效使用Django的QuerySets https://www.oschina.net/translate/django-querysets

##### QuerySet的惰性机制

**解释**

Model.objects.all() 或者 .filter() 等都只是返回一个QuerySet（查询结果集对象），它并不会马上执行sql，而是当调用QuerySet的时候才执行。

##### QuerySet特点

* 可切片

```python
persons = Person.objects.all()[:10]
```

* 可迭代

```python
for person in persons:
    print(person.name)
# 如果数据量过大可能会撑爆缓存，可以使用迭代器优雅地解决这个问题
for person in persions.iterator():
    print(person.name)
```

* 惰性计算和缓存机制

```python
# 惰性机制：等于一个生成器，不应用persons不会执行任何SQL操作
persons = Person.objects.all()
# QuerySet缓存机制：1次数据库查询记过QuerySet都会对应一次缓存
# 再次使用该QuerySet时，不会发生新的SQL操作，这样减小了频繁操作数据库给数据库带来的压力
```

##### 合并QuerySet

* 使用 `|` 直接将两个QuerySet拼接起来

```python
# 空的QuerySet对象
person = Person.objects.none()
# 合并QuerySet对象，返回对象类型不变（<class 'django.db.models.query.QuerySet'>）
person_1 = Person.objects.filter(name="jiuchou")
persons = person | person_1
```

* 使用chain拼接

> 当合并的结果（例中的persons）用于分页的时候，就有问题，会报chain没有len属性，当试图给persons赋len属性的时候不成功

```python
from itertools import chain
# 合并QuerySet并生成迭代器，返回对象类型为 <class 'itertools.chain'>
persons = chain(person_1, person_2)
```

* 使用列表的extend方法

```python
persons = []
persons.extend(person_1)
persons.extend(person_2)
```
**效率**

遗留问题：分页效率和空间花费

##### 检查QuerySet是否包含数据

* 使用if判断

> 执行（evaluation）：当你遍历QuerySet时，所有匹配的记录会从数据库获取，然后转换成Django的model

```python
# if 会执行SQL操作，将数据放入QuerySet的cache
if persons:
    pass
```

* 使用exists()检查是否有数据

```python
# exists() 的检查可以避免数据放入QuerySet的cache
if persons.exists():
    pass
```

##### QuerySet cache过大的解决方案

处理成千上万个记录时，将它们一次性装入内存是很浪费的，这个时候cache会成为问题。更糟糕的是，巨大的QuerySet可能会锁住系统进程，让你的程序濒临崩溃。

要避免在遍历数据的同时产生QuerySet cache，可以使用iterator()方法获取数据，处理完数据就将其丢弃。

```python
for person in persons.iterator():
    pass
```
> 使用iterator()方法防止生成cache的同时，意味着遍历同一个QuerySet时会重复执行查询。所以在使用iterator()时，要确保在操作一个大的QuerySet的时候没有重复执行查询。

##### QuerySet过大的解决方案

如前所述，查询集缓存对于组合 if 语句和 for 语句是很强大的，它允许在一个查询集上进行有条件的循环。然而对于很大的查询集，则不适合使用查询集缓存。

最简单的解决方案是结合使用exists()和iterator()，通过使用两次数据库查询来避免使用查询集缓存。

* 简单的解决方案

```python
persons = Person.objects.all()
# One database query to test if any rows exist.
if persons.exists():
    # Another database query to start fetching the rows in batches.
    for person in persons.iterator():
        print(person.name)
```

* 复杂的解决方案：使用Python的“高级迭代方法”，在开始循环前先查看一下 iterator() 的第一个元素再决定是否进行循环

```python
from itertools import chain

persons = Person.objects.all()
# One database query to start fetching the rows in batches.
persons_iterator = persons.iterator()
# Peek at the first item in the iterator.
try:
    first_person = next(persons_iterator)
except StopIteration:
    # No rows were found, so do nothing.
    pass
else:
    # At least one row was found, so iterate over
    # all the rows, including the first one.
    for person in chain([first_person], persons_iterator):
        print(person.name)
```

##### 防止不当的优化

queryset的cache是用于减少程序对数据库的查询，在通常的使用下会保证只有在需要的时候才会查询数据库。

使用exists()和iterator()方法可以优化程序对内存的使用。不过，由于它们并不会生成queryset cache，可能会造成额外的数据库查询。

所以编码时需要注意一下，如果程序开始变慢，你需要看看代码的瓶颈在哪里，是否会有一些小的优化可以帮到你。

##### 如何在QuerySet时进行格式转换

* https://blog.csdn.net/enlangs/article/details/81701358


#### 2.1.2 其他

##### 2.1.2.1 Django的auto_now=True没有自动更新

- 参考：https://www.cnblogs.com/aguncn/p/10319255.html

auto_now=True自动更新，有一个条件，就是要通过django的model层。如create或是save方法。

如果是filter之后update方法，则直接调用的是sql，不会通过model层，所以不会自动更新此时间。

官方解释：

```
What you consider a bug, others may consider a feature, e.g. usingupdate_fieldsto bypass updating fields withauto_now. In fact, I wouldn't expectauto_nowfields to be updated if not present inupdate_fields.
```

解决办法：

强制改成save()或是update时，带上时间。如下：

```python
status_item = DeployStatus.objects.get(name=status_name)
DeployImage.objects.filter(name=order_name).update(
	deploy_status=status_item,
	change_date=datetime.now())

# 上面的操作，才会更新DeployImage表里的change_date(add_now=True)的时间，
# 或是如下调用save()方法
# deploy_item = DeployImage.objects.get(name=order_name)
# deploy_item.deploy_status = status_item
# deploy_item.save()
```

## 3 三方库

### 3.1 Django定时任务

#### 3.1.1 Django使用django-crontab设置定时任务

参考

* django-crontab： https://blog.csdn.net/weixin_35757704/article/details/89227896

##### 3.1.1.1 下载安装 `django-crontab`

* https://pypi.org/project/django-crontab/



**django重构**

* https://blog.csdn.net/weixin_42149982/article/details/81914428

* https://www.cnblogs.com/yangmv/p/5327477.html

* Nginx+Uwsgi+Vue+Django服务器配置 https://blog.csdn.net/apple9005/article/details/80336086
* Django-RESTful-framework 的中文文档 https://www.zhihu.com/question/29427828



**认证**

* django jwt authentication
  * https://blog.csdn.net/weixin_42578481/article/details/86599681



* jwt token: http://www.cnblogs.com/wayneiscoming/p/7513487.html

  ​	

  

  问题1.用户登出
  	问题2.token自动延期





# Django Event Error

### Django JSON:: 'dict' object has no attribute '_meta'
#### 问题
```
def display_home(request):
    from datetime import *
    now=datetime.today()
    print 'Month is %s'%now.month

events=Event.objects.filter(e_date__year=datetime.today().year).filter(e_date__month=datetime.today().month,e_status=1).values('e_name','e_date')
return render_to_response("SecureVirtualElection/home.html",{'events': serializers.serialize("json",events, fields=('e_name','e_date'))},context_instance=RequestContext(request))
```
error :: 'dict' object has no attribute '_meta'

#### 原因

Serializer waits for normal queryset, not ValuesQuerySet (which is returned by values). If you want to query only certain fileds, use only.

#### 解决方案
* 方法一: 使用only
```
events=Event.objects.filter(e_date__year=datetime.today().year).filter(e_date__month=datetime.today().month,e_status=1).only('e_name','e_date')
```
* 方法一: 使用all
```
events=Event.objects.filter(e_date__year=datetime.today().year).filter(e_date__month=datetime.today().month,e_status=1).all()
```

## 待整理

细说 Django — web 前后端分离

https://www.cnblogs.com/reboot51/p/8951521.html

django-rest-framework(概念篇)——apiview&viewset

https://www.jianshu.com/p/2700ff413250

django(六)：view和cbv

https://www.cnblogs.com/kuaizifeng/p/9532520.html

django(五)：cookie和session

https://www.cnblogs.com/kuaizifeng/p/9530446.html

Django---类视图详解

https://blog.csdn.net/qq_42684307/article/details/81042845

Django类方式写view

http://www.cnblogs.com/2bjiujiu/p/7453054.html

Python大神 - Django（基础知识）--构建项目的思路

https://www.cnblogs.com/langzibin/p/7693457.html

Django实际站点项目开发经验谈

http://www.cnblogs.com/Lands-ljk/p/5711392.html

https://www.ibm.com/developerworks/cn/opensource/os-cn-django/

Python进阶(三十六)-Web框架Django项目搭建全过程

https://blog.csdn.net/sunhuaqiang1/article/details/70182416

Django - 美多商场项目 - 思路总结

https://blog.csdn.net/apollo_miracle/article/details/83960922

Django()-----对美多商城项目的总结

https://blog.csdn.net/qq_43475097/article/details/83822954

https://www.jikexueyuan.com/course/962.html



Django写数据库

```bash

       #---------表中插入数据方式一
            # info={"username":u,"sex":e,"email":e}
            # models.UserInfor.objects.create(**info)
 
       #---------表中插入数据方式二
        models.UserInfor.objects.create(
            username=u,
            sex=s,
            email=e
        )
```



python 时间模块小结（time and datetime）

https://www.cnblogs.com/sunshineyang/p/6818834.html