# Django框架





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