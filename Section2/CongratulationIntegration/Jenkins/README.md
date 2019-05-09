# Jenkins

<!-- TOC -->

- [Jenkins](#jenkins)
    - [1 Installing Jenkins](#1-installing-jenkins)
        - [1.1 物理机/虚拟机](#11-物理机虚拟机)
        - [1.2 Docker](#12-docker)
            - [1.2.1 使用 jenkins/jenkins 镜像](#121-使用-jenkinsjenkins-镜像)
            - [1.2.2 使用 jenkinsci/blueocean 镜像](#122-使用-jenkinsciblueocean-镜像)
            - [1.2.3 问题记录](#123-问题记录)
        - [1.3 Windows](#13-windows)
            - [1.3.1 Windows安装Jenkins平台服务](#131-windows安装jenkins平台服务)
            - [1.3.2 详细安装步骤说明](#132-详细安装步骤说明)
    - [2 Jenkins Cli](#2-jenkins-cli)
    - [3 Jenkins Plugin](#3-jenkins-plugin)
        - [3.1 插件安装](#31-插件安装)
        - [3.2 插件说明（Comonly Used Plugins）](#32-插件说明comonly-used-plugins)
            - [3.2.1 用户认证鉴权](#321-用户认证鉴权)
                - [3.2.1.1 ldap](#3211-ldap)
                - [3.2.1.2 role-strategy](#3212-role-strategy)
            - [3.2.2 视图](#322-视图)
            - [3.2.3 节点](#323-节点)
            - [3.2.4 配置管理（SCM）](#324-配置管理scm)
            - [3.2.5 易用性工具插件](#325-易用性工具插件)
            - [3.2.6 其他主流插件](#326-其他主流插件)
            - [3.2.7 Docker插件](#327-docker插件)
            - [3.2.8 Coverity插件](#328-coverity插件)
    - [4 API调用](#4-api调用)
        - [4.1 使用 Linux curl 调用API](#41-使用-linux-curl-调用api)
            - [4.1.1 CSRF Protection](#411-csrf-protection)
                - [解决方案实例：](#解决方案实例)
                - [问题记录说明](#问题记录说明)
        - [4.2 Python使用Jenkins REST API](#42-python使用jenkins-rest-api)
    - [5 更新记录](#5-更新记录)

<!-- /TOC -->

> 本文内容Jenkins服务器基于 jenkinsci/blueocean 镜像搭建。
>
> Jenkins版本: 2.150.1

## 1 Installing Jenkins

* [Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/)

### 1.1 物理机/虚拟机 

* [Linux: Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/#docker)

### 1.2 Docker

> 步骤：
>
> ​	安装Docker
>
> ​	创建用户
>
> ​	运行容器
>
> 文档：
>
> ​	[Docker: Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/#linux)

*Run Jenkins in Docker*

#### 1.2.1 使用 jenkins/jenkins 镜像

```bash
docker run -p 8080:8080 -p 50000:50000 -v /home/jenkins/jenkins_home:/var/jenkins_home --user root -d --name JenkinsServer jenkins/jenkins:lts
```

#### 1.2.2 使用 jenkinsci/blueocean 镜像

```bash
# 1.install docker
# 2.user group
groupadd jenkins
useradd -d /home/jenkins -s /bin/bash -c "jenkins user" -g jenkins -G docker -m -p "jenkins" jenkins

# 3.run docker
mkdir /home/jenkins/jenkins_home
docker pull jenkinsci/blueocean
docker run -u jenkins -d -p 8080:8080 -p 50000:50000 -v /home/jenkins/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock  --name JenkinsServer jenkinsci/blueocean
```

#### 1.2.3 问题记录

启动失败, 报错 `Permission denied`

可能原因及解决方案

1.宿主机的 `jenkins` 用户及用户组问题

docker中jenkins的uid,gid默认都是1000,因此宿主机的路径必须也要设置成相同的权限

2.selinux开启问题(待整理, 未验证)

* 来源: https://blog.csdn.net/colorful_starhui/article/details/53518940

宿主机切换jenkins用户，id命令查看到:

```
bash-4.2$ id
uid=1000(jenkins) gid=1000(jenkins) groups=1000(jenkins) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```
而docker环境下id命令结果没有上面标红:

```
[root@localhost jenkins_home]# docker run -ti --rm --entrypoint="/bin/bash" jenkins -c "id"
uid=1000(jenkins) gid=1000(jenkins) groups=1000(jenkins)
```

宿主机下执行/usr/sbin/sestatus -v命令查看selinux状态：
```
[root@localhost jenkins_home]# /usr/sbin/sestatus -v
SELinux status:                 enabled
```

那么就可以判定selinux是打开的

那么处理方法有两种：
* 关闭selinux
```
# 临时
getenforce
setenforce 0

# 永久
vim /etc/sysconfig/selinux
SELINUX=enforcing 改为 SELINUX=disabled
```
* 不关闭selinux的情况下，修改宿主机jenkins挂载目录的权限：

在宿主机执行ls -Z可以查看selinux信息，
```
[root@localhost jenkins_home]# ls -Za
drwxr-xr-x. jenkins jenkins system_u:object_r:var_t:s0       .
drwxr-xr-x. root    root    system_u:object_r:var_t:s0       ..
```
那么同样在docker环境下查看selinux信息，
```
[root@localhost jenkins_home]# docker run -ti --rm --entrypoint="/bin/bash" jenkins -c "cd /var/jenkins_home;ls -Zal"
total 20
drwxr-xr-x.  2 jenkins jenkins system_u:object_r:svirt_sandbox_file_t:s0           4096 Dec  8 07:57 .
drwxr-xr-x. 12 root    root    system_u:object_r:svirt_sandbox_file_t:s0:c365,c598 4096 Nov  8 21:55 ..
```
比较第三列确有差异。

接下来手动修改/var/jenkins_home目录的selinux权限即可：
```
[root@localhost jenkins_home]# chcon -R -t svirt_sandbox_file_t .
[root@localhost jenkins_home]# ls -aZl
total 84
drwxr-xr-x. 13 system_u:object_r:svirt_sandbox_file_t:s0 jenkins jenkins 4096 Dec  8 15:21 .
drwxr-xr-x. 21 system_u:object_r:var_t:s0       root    root    4096 Dec  7 14:28 ..
```

### 1.3 Windows

> 参考： [安装Jenkins](https://jenkins.io/zh/doc/book/installing/)

#### 1.3.1 Windows安装Jenkins平台服务

从网站安装的话, 请使用安装程序：

- [Download the latest package](http://mirrors.jenkins.io/windows/latest)
- 打开包装并按照说明操作

#### 1.3.2 详细安装步骤说明

1. 下载 `jenkins-2.176.zip` 安装包，解压得到 `jenkins.exe`，双击按照如下步骤安装

![](image/install-jenkins-windows-1.png)

![](image/install-jenkins-windows-2.png)

![](image/install-jenkins-windows-3.png)

![](image/install-jenkins-windows-4.png)

![](image/install-jenkins-windows-5.png)

2. 安装完成后自动打开浏览器访问 `http://localhost:8080/login?from=%2F`
![](image/install-jenkins-windows-6.png)

3. 将 `D:\Develop\Jenkins\secrets\initialAdminPassword` 文件中内容输入到上图后，点击 `Continue` 按钮
4. 初始化插件安装方式，可选择 `Install suggested plugins` 和 `Select plugins to install` 两种模式，根据需求自行选择（本文基于 `Install suggested plugins` 演示）
![](image/install-jenkins-windows-7.png)

5. 进入默认推荐插件安装界面
![](image/install-jenkins-windows-8.png)

6. 安装完成，进入创建管理员用户界面，可选择 `Continue as admin` 和 `Save and Continue`（本文基于 `Save and Continue` 演示）
![](image/install-jenkins-windows-9.png)
![](image/install-jenkins-windows-10.png)

7. 配置服务器域名地址（本文基于默认配置 `http://localhost:8080/` 演示）
![](image/install-jenkins-windows-11.png)

8. 安装完成，点击 `Start using Jenkins`，进入Jenkins平台服务页面
![](image/install-jenkins-windows-12.png)

9. Jenkins平台服务初始页面
![](image/install-jenkins-windows-13.png)

## 2 Jenkins Cli

进入`系统设置 - 安全设置`开启命令行

*命令行格式*

```bash
java -jar jenkins-cli.jar -s JENKINS_URL command command options...
```

*命令行使用帮助*

```bash
java -jar jenkins-cli.jar --help
java -jar jenkins-cli.jar -s JENKINS_URL help
```

*命令行使用用例: Install Jenkins Plugin*
```bash
# 进入容器
docker exec -ti JenkinsServer /bin/bash

# 执行插件安装命令
java -jar /var/jenkins_home/war/WEB-INF/jenkins-cli.jar -remoting -s http://localhost:8080 install-plugin /var/jenkins_home/plugins/ssh-slaves.hpi -deploy
```

## 3 Jenkins Plugin

> 扩展
> https://blog.csdn.net/pansaky/article/details/80755739
> https://blog.csdn.net/chinabluexfw/article/details/7484311

### 3.1 插件安装

插件安装有两种安装方式：

1.在线安装

​	登录Jenkins，进入系统设置 - 插件管理 - 安装插件

2.离线安装

​	进入[Jenkins插件官网](https://plugins.jenkins.io/)，搜索指定插件下载安装。

​	方式一: 将下载到插件放入容器中的`/var/jenkins_home/plugins`目录中，重启容器

​	方式二: [命令行安装](## 2 Jenkins Cli)

### 3.2 插件说明（Comonly Used Plugins）

#### 3.2.1 用户认证鉴权

##### 3.2.1.1 ldap

```
官网地址: https://plugins.jenkins.io/ldap
功能: 连接LDAP，使用LDAP进行用户认证
```

**插件配置**

进入系统设置

##### 3.2.1.2 role-strategy

```
官网地址: https://plugins.jenkins.io/role-strategy
功能: 权限策略插件，自定义用户权限策略
```

#### 3.2.2 视图 

1.sectioned-view

```
官网地址: https://plugins.jenkins.io/sectioned-view
功能: 定义section视图，可用于Jenkins平台概述说明
```

#### 3.2.3 节点

> 1.创建节点
>
> ​	In 1.x version it was called "Dumb slave" and in modern versions "Permanent Agent" 
>
> 2.没有【Launch agent via Java Web Start】选项
>
> ​	进入`Manage Jenkins > Configure Global Security > TCP port for JNLP agents `，开启【TCP port for JNLP agents】，使用随机选取模式

1.ssh-slaves

```
官网地址: https://plugins.jenkins.io/ssh-slaves
仓库地址: https://github.com/jenkinsci/ssh-slaves-plugin
功能: 支持Unix及类Unix操作系统的节点机器(slave)使用ssh-slave连接
说明: 
	使用秘钥验证(https://support.cloudbees.com/hc/en-us/articles/115000073552-Host-Key-Verification-for-SSH-Agents)
依赖插件:
	JDKTool(https://plugins.jenkins.io/jdk-tool)
```

#### 3.2.4 配置管理（SCM）

> - Jenkins subversion Credentials

1.subversion

```
官网地址: https://plugins.jenkins.io/subversion
功能: 支持Unix及类Unix操作系统的节点机器(slave)使用ssh-slave连接
说明: 
依赖插件:
	mapdb-api(https://plugins.jenkins.io/mapdb-api)
	scm-api(https://plugins.jenkins.io/scm-api)
	command-launcher(https://plugins.jenkins.io/command-launcher)
```


#### 3.2.5 易用性工具插件

1.ansicolor

```
官网地址: https://plugins.jenkins.io/ansicolor
功能: 日志颜色支持
说明: 
```

2.timestamper

```
官网地址: https://plugins.jenkins.io/timestamper
功能: 支持显示Job执行时间
说明: 
```

3.build-timestamp

```
官网地址: https://plugins.jenkins.io/build-timestamp
功能: 
说明: 获取变量$BUILD_TIMESTAMP
```

4.description-setter

```
官网地址: https://plugins.jenkins.io/description-setter
功能: 修改构建(build)主页显示信息内容
说明: 主要用于标识永久保存的工程构建原因
```

5.Heavy Job

```
官网地址: https://plugins.jenkins.io/heavy-job
功能: 
说明: This plugin allows you to define "weight" on each job, and making each job consume that many executors (instead of just one.) Useful for a job that's parallelized by itself, so that Hudson can schedule jobs accordingly.
```

6.email-ext

```
官网地址: https://plugins.jenkins.io/email-ext
功能: 增加邮件通知功能(Editable Email Notification)
说明: 
```

7.groovy

```
官网地址: https://plugins.jenkins.io/groovy
功能: 增加使用groovy脚本功能
说明: 
```

8.jobConfigHistory

```
官网地址: https://plugins.jenkins.io/jobConfigHistory
功能: 增加查看Job历史配置功能
说明: 
```

9.rebuild

```
官网地址: https://plugins.jenkins.io/rebuild
功能: 增加rebuild功能
说明: 
```

10.schedule-build

```
官网地址: https://plugins.jenkins.io/schedule-build
功能: 增加定时触发构建功能
说明: 
```

11.ws-cleanup

```
官网地址: https://plugins.jenkins.io/ws-cleanup
功能: 增加构建完成后清理工作空间功能
说明:  
依赖插件:
	resource-disposer(https://plugins.jenkins.io/resource-disposer)
```

12.build-environment

```
官网地址: https://plugins.jenkins.io/build-environment
功能: 查看构建(build)的环境变量
说明: 
```

13.display-console-output(未使用)

```
官网地址: https://plugins.jenkins.io/display-console-output
功能: 在主页面显示最新构建日志
说明: 
```

14.downstream-buildview(未使用)

```
官网地址: https://plugins.jenkins.io/downstream-buildview
功能: 查看子项目构建情况
说明: 
```

#### 3.2.6 其他主流插件 

1.Global Post Script Plugin

```
官网地址: https://plugins.jenkins.io/global-post-script
功能: 增加全局脚本功能
说明: 
	官方使用指南: https://wiki.jenkins.io/display/JENKINS/Global+Post+Script+Plugin
```

2.SLOCCount Plugin

```
官网地址: https://plugins.jenkins.io/sloccount
功能: This plug-in generates trend report for SLOCCount and cloc open source tools, that count number of code lines written in many programming languages.
说明: 
	官方使用指南: https://wiki.jenkins.io/display/JENKINS/SLOCCount+Plugin
扩展:
	cloc: http://cloc.sourceforge.net/
	sloccount: https://dwheeler.com/sloccount/
```

#### 3.2.7 Docker插件

1.docker-slaves

```
官网地址: https://plugins.jenkins.io/docker-commons
功能: 
说明: 
```

2.docker-slaves(未使用)

```
官网地址: https://plugins.jenkins.io/docker-slaves
功能: 
说明: 
```

3.docker-custom-build-environment(未使用)

```
官网地址: https://plugins.jenkins.io/docker-custom-build-environment
功能: 
说明: 
```

#### 3.2.8 Coverity插件

> Coverity 2018.12之后版本，使用`synopsys-coverity`插件

coverity插件

```
官网地址: https://plugins.jenkins.io/synopsys-coverity
仓库地址: 
功能: 
说明: 
```

## 4 API调用

* 参考：
  * [Python-Jenkins API使用 —— 在后端代码中操控Jenkins](https://www.cnblogs.com/znicy/p/5498609.html)

### 4.1 使用 Linux curl 调用API

> 详细内容查看官网介绍: [Remote access API](https://wiki.jenkins.io/display/JENKINS/Remote+access+API)

该方式是通过命令行直接调curl去发POST请求的方式来触发job的构建。

对于用openid管理的Jenkins，需要带上参数--user USERNAME:PASSWORD，其中的USERNAME和PASSWORD不是你的openID登录的账号密码，而是登录后显示在Jenkins中的User Id和API Token。

API Token的查看方式为

**Jenkins1.x**

使用openID登录jenkins -> 点击右上角用户名，进入用户个人页面 -> 点击左边的设置，打开设置页面 -> API Token，Show Api Token... 

**Jenkins2.x**

使用openID登录jenkins -> 点击右上角用户名，进入用户个人页面 -> 点击左边的设置，打开设置页面 -> API Token（创建时显示后保存，之后无法查看，如果忘记需要重新设置）


#### 4.1.1 CSRF Protection

> 如果CSRF开启，需使用crumb，否则会出现报错：`Error 403 No valid crumb was included in the request`

官网说明

If your Jenkins uses the "Prevent Cross Site Request Forgery exploits" security option (which it should), when you make a `POST` request, you have to send a CSRF protection token as an HTTP request header.
For curl/wget you can obtain the header needed in the request from the URL `JENKINS_URL/crumbIssuer/api/xml` (or `.../api/json`). Something like this:

```
wget -q --auth-no-challenge --user USERNAME --password PASSWORD --output-document - \
'JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'
```

This will print something like ".crumb:1234abcd", which you should add to the subsequent request.

##### 解决方案实例：

* 参考：
  * https://stackoverflow.com/questions/23497819/trigger-parameterized-build-with-curl-and-crumb
  * https://stackoverflow.com/questions/38137760/jenkins-rest-api-create-job

实例1：

**obtain crumb** $ `wget -q --auth-no-challenge --user USERNAME --password PASSWORD --output-document - 'JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'`

**Now Run Jenkins Job** $ `curl -I -X POST http://USERNAME:PASSWORD@JENKINS_URL/job/JOBName/build -H "Jenkins-Crumb:44e7038af70da95a47403c3bed5q10f8"`

实例2：

```bash
CRUMB=$(curl -s --user USERNAME:PASSWORD 'JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')
curl --user USERNAME:PASSWORD -H "$CRUMB" -d "script=$GROOVYSCRIPT" JENKINS_URL/script
```

实例3：

```bash
CRUMB=$(curl -s 'http://USERNAME:APITOKEN@JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')
curl -X POST -H "$CRUMB" "http://USERNAME:APITOKEN@JENKINS_URL/createItem?name=NewJob"
```

##### 问题记录说明

1.获取 `Jenkins-Crumb` 失败

**现象** 无返回值或返回错误信息

**原因** 网络受限制，日常使用过程中机器添加了代理导致

**解决方案** 使用 `unset http_proxy https_proxy` 取消代理

2.获取 `Jenkins-Crumb` 失败

**现象**  wget: unrecognized option: auth-no-challenge
BusyBox v1.2.8.4 (2018-07-17 15:21:40 UTC)

**原因** 在使用`jenkinsci/blueocean:latest` 镜像启动平台时, 如果执行节点使用 `master`, 则在使用 `wget` 时属于 `BusyBox wget` 而不是 `GNU wget`, `BusyBox wget` 未实现 `--auth-no-challenge` 参数

**解决方案** 使用 `curl` 命令实现功能

### 4.2 Python使用Jenkins REST API  

1.Python 使用Jenkins Rest API 之 [python-jenkins](python-jenkins.md)

2.Python 使用Jenkins Rest API 之 [jenkinsapi](jenkinsapi.md)

## 5 更新记录

```
2019.02.13: 完成初稿，包含Jenkins服务器安装概述、主流插件概述、Jenkins API等内容
2019.02.17: 完善API接口调用内容
2019.03.14: 完善实际使用中可能存在的问题记录
2019.05.09: 增加windows平台安装Jenkins服务的详细说明
```

