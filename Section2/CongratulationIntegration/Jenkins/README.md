# Jenkins

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

1.ldap

```
官网地址: https://plugins.jenkins.io/ldap
功能: 连接LDAP，使用LDAP进行用户认证
```

2.role-strategy

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

### 4.1 使用 Linux curl 调用API

详细内容查看官网介绍: [Remote access API](https://wiki.jenkins.io/display/JENKINS/Remote+access+API)

### 4.2 Python使用Jenkins Rest API  

#### 4.2.1 Python 使用Jenkins Rest API 之 python-jenkins 

#### 4.2.2 Python 使用Jenkins Rest API 之 jenkinsapi

## 5 更新记录

```
2019.02.23: 完成初稿，包含Jenkins服务器安装概述、主流插件概述、Jenkins API等内容。
```

