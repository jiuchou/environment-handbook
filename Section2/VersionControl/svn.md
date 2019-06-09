# SVN

* [勾子](https://www.jianshu.com/p/56b8a31bbcbb)

## 1 SVN使用

### 1.1 SVN Server

1. 创建仓库
```bash
svnadmin create /root/svn/repos_jiuchou
```

2. `svn` 启动
```bash
svnserve -d -r /root/svn/repos_jiuchou
```



### 1.2 SVN Client

**svn获取指定分支的指定文件或目录**

```bash
svn export -r xxx http://xx.xx.xx.xx/test/file
svn export -r xxx http://xx.xx.xx.xx/test/dir
```



* 关于SVN常用命令之export: https://blog.csdn.net/gengxiaoming7/article/details/50510330
* svn external
  * https://blog.csdn.net/echoisland/article/details/6584875
  * https://blog.csdn.net/gtuu0123/article/details/4532848



```bash
# 使用编辑器更改属性
svn propedit $prop_name $path
# 设置属性
svn propset $prop_name $prop_value $path
# 获取属性
svn propget $prop_name $path
# 删除属性
svn propdel $prop_name $path
# 打印文件或目录的属性信息
svn proplist -v $path
# 版本相关更改加入参数
-revprop -r $version
```





## 2 SVN服务器搭建

```bash
 # svn-server

 # 下载镜像
docker pull krisdavison/svn-server:v2.0 
 # 生成文件夹
mkdir -p svn/data
 # 启动容器
 # 8081 用来查看服务器（apache），3690 是svn通信端口
docker run -d -ti -p 8081:80  -p 3690:3690 \
-v /home/F_xvdf1/svn/data:/home/svn \
--name qy-test-svn \
-v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro \
krisdavison/svn-server:v2.0 /startup.sh 

 # 页面查看 : user/password。这个密码是固定的，只能查看
http://ip:8081/svn
 
 # 进入容器： add repository (注意一点是/home/svn/FILE)
docker exec -d -ti qy-test-svn /usr/bin/svnadmin create /home/svn/test1
    # QYRepository is my repository'name
 # configure svn repository 
cd svn/QYRepository/conf
 # do some configure

 # 启动svn服务， 启动一次就好了
docker exec -d -ti qy-test-svn /usr/bin/svnserve -d -r /home/svn/

 # checkout in other machine
test: svn checkout svn://100.109.192.106/QYRepository --username=paas

 # configure
 3个文件
    - svnserve.conf: 总配置文件
        anon-access  = read # 非鉴权用户只读
        auth-access = write # 认证用户有写权限
        password-db = passwd # 密码配置文件（配置这个：passwd文件才生效）
        authz-db = authz  # 权限认证文件 （配置这个：authz文件才生效）
        # realm = test 认证域（类似登录时的提示）
        以上配置都是缺省值
    - passwd： 密码(需要conf文件中设置才行) 是用时读
        admin=admin # 用户=密码 (明文)
        paas=Huawei@123 
        root=huawei123
        qy=Huawei@123 
    - authz： 组和权限 （同上）
        [groups]
        g_write=admin,paas,qy
        g_read=paas
        [QYRepository:/] # 范围： '', 'r', 'rw'
        @g_write=rw
        @g_read=r
        *=r # * 代表任何用户，设置这个可以不用用户密码直接下载
    - hooks-env.tmpl 文件没用到

```

- 使用
```bash
 # 需要svn
which svn || apt-get install subversion

 # 下载 paas/Huawei@123
 # url=svn://100.109.192.106/QYRepository 
 # path是本地地址 
 # 下载匿名库不需要用户密码
mkdir svn && cd svn
svn checkout url --username=username--password=password path 

 # 命令
svn status (st) # 查看状态
    ？ 不在svn控制
    M  内容被修改
    C  发生冲突
    A  加入缓存区
    K  被锁定
    svn st -v # 查看文件(夹)的最后一个修改人
svn update (up) # 从远程库同步
    svn update -r 100 test.m # 将test.m文件还原到版本100
    如果update test.m失败，需要解决冲突，清理svn resolvd,再commit
svn add file/path # 添加（缓存区）
svn commit -m "" (ci) # 提交
svn delete -m "" (del rm) # 删除文件
    相当于 svn delete test.m && svn commit -m ""
svn log [path] # 显示文件的所有修改记录
    svn info 显示文件的详细信息
svn diff -r m:n [path] (di) # 对版本m和版本n比较差异
svn merge -r m:n path # 将2个版本的差异河滨到当前文件
svn lock [path] # 对一个文件进行锁定
    svn unlock # 解除一个文件的锁定
    # 锁定：一个用户在一个工作副本中锁定了一个文件，
    那么只有这个用户在这个工作副本才能解除锁定。
    其他任何用户任何副本都不能（包括这个用户）
    如果副本丢失，可以强制获取锁

 # 不常用
svn list # 查看目录
svn switch  url [path]  # 将工作副本映射到新的URL
    svn switch --relocate FROM TO [PATH] # 
```

## 3 待整理

**SVN修改已提交日志信息**

* https://blog.csdn.net/iefreer/article/details/19755595



