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
            - [3.2.1 用户及权限管理](#321-用户及权限管理)
                - [3.2.1.1 认证管理](#3211-认证管理)
                    - [3.2.1.1.1 ldap](#32111-ldap)
                    - [3.2.1.1.2 Active Directory](#32112-active-directory)
                    - [3.2.1.1.3 GitHub Authentication](#32113-github-authentication)
                    - [3.2.1.1.2 GitLab Authentication](#32112-gitlab-authentication)
                    - [3.2.1.1.2 openid](#32112-openid)
                - [3.2.1.2 权限管理](#3212-权限管理)
                    - [3.2.1.2.1 role-strategy](#32121-role-strategy)
                    - [3.2.1.2.2  Matrix Authorization Strategy](#32122--matrix-authorization-strategy)
                - [3.2.1.3 其他](#3213-其他)
                    - [3.2.1.2.1 avatar](#32121-avatar)
            - [3.2.2 视图](#322-视图)
                - [3.2.2.1 List view Jenkins](#3221-list-view-jenkins)
                - [3.2.2.2 sectioned-view](#3222-sectioned-view)
                - [3.2.2.3 Build Pipeline](#3223-build-pipeline)
                - [3.2.2.4 Folder](#3224-folder)
                - [3.2.2.5 Nested View](#3225-nested-view)
            - [3.2.3 节点](#323-节点)
                - [3.2.3.1 Linux节点](#3231-linux节点)
                    - [3.2.3.1.1 ssh-slaves](#32311-ssh-slaves)
                - [3.2.3.2 Windows节点](#3232-windows节点)
                - [3.2.3.3 Docker节点](#3233-docker节点)
                    - [3.2.3.3.1 Docker](#32331-docker)
                    - [3.2.3.3.2 Kubernetes](#32332-kubernetes)
                - [3.2.3.4 Slave Monitor](#3234-slave-monitor)
                    - [3.2.3.4.1 Slave Monitor for system load average](#32341-slave-monitor-for-system-load-average)
            - [3.2.4 代码管理](#324-代码管理)
                - [3.2.4.1 git](#3241-git)
                - [3.2.4.2 subversion](#3242-subversion)
            - [3.2.5 构建](#325-构建)
                - [3.2.5.1 构建参数](#3251-构建参数)
                    - [3.2.5.1.1 Nodelabelparameter（未验证）](#32511-nodelabelparameter未验证)
                    - [3.2.5.1.2 待整理](#32512-待整理)
                - [3.2.5.2 构建触发](#3252-构建触发)
                    - [3.2.5.2.1 Build periodically](#32521-build-periodically)
                    - [3.2.5.2.2 Poll SCM](#32522-poll-scm)
                    - [3.2.5.2.3 GitHub Integration](#32523-github-integration)
                    - [3.2.5.2.4 GitLab](#32524-gitlab)
                    - [3.2.5.2.4 GitLab](#32524-gitlab-1)
                    - [3.2.5.2.5 Gerrit Trigger](#32525-gerrit-trigger)
                    - [3.2.5.2.6 JIRA Trigger](#32526-jira-trigger)
            - [3.2.6 易用性工具插件](#326-易用性工具插件)
            - [3.2.7 其他主流插件](#327-其他主流插件)
            - [3.2.8 Docker插件](#328-docker插件)
            - [3.2.9 其他](#329-其他)
            - [3.2.10 Admin相关插件](#3210-admin相关插件)
                - [3.2.10.1 Configuration Slicing](#32101-configuration-slicing)
                - [3.2.10.2 Mask Passwords](#32102-mask-passwords)
                - [3.2.10.3 Backup](#32103-backup)
    - [4 API调用](#4-api调用)
        - [4.1 使用 Linux curl 调用API](#41-使用-linux-curl-调用api)
            - [4.1.1 使用简介](#411-使用简介)
            - [4.1.2 参数说明](#412-参数说明)
                - [4.1.2.1 API Token](#4121-api-token)
                - [4.1.2.2 CSRF Protection](#4122-csrf-protection)
                    - [4.1.2.2.1 解决方案实例](#41221-解决方案实例)
                    - [4.1.2.2.2 问题记录说明](#41222-问题记录说明)
        - [4.2 Python使用Jenkins REST API](#42-python使用jenkins-rest-api)
        - [4.3 Groovy 调用 Jenkins API](#43-groovy-调用-jenkins-api)
    - [5 可借鉴整理](#5-可借鉴整理)
    - [6 更新记录](#6-更新记录)

<!-- /TOC -->

## 1 Installing Jenkins

* [Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/)

### 1.1 物理机/虚拟机 

* [Linux: Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/#docker)

### 1.2 Docker

> 本文内容Jenkins服务器基于 jenkinsci/blueocean 镜像搭建。
>
> Jenkins版本: 2.150.1
>
> 
>
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

### 2.1 命令行使用问题

#### 2.1.1 Jenkins1.x

##### `Failed to authenticate with you SSH keys`

> 版本
>
> * Jenkins1.609.1

- 参考: [来自Jenkins-CI的命令行登录告警问题](http://jenkins-ci.361315.n4.nabble.com/jenkins-command-line-Failed-to-authenticate-with-your-SSH-keys-td4642440.html)

**报错信息** `[WARN] Failed to authenticate with you SSH keys. Proceeding as anonymous`

**操作内容** 执行 `java -jar jenkins-cli.jar -s JENKINS_URL login --username USERNAME --password PASSWORD` 提示告警信息

**原因** CLI authenticates the user according to the public key stored in users Jenkins configuration.
So for this to work, we need the public key corresponding to the private key that you specify in the command line is specified in the configuration of the corresponding user.

**解决方案** 进入 `http://JENKINS_URL/user/USERNAME/configure`，添加公钥到 `SSH Public Keys` 中

#### 2.1.2 Jenkins2.x

##### `anonymous is missing the Job/Create permission`

> 版本
>
> - Jenkins2.150.1

**报错信息** `anonymous is missing the Job/Create permission`

**操作内容** 执行 `java -jar jenkins-cli.jar --remoting -s JENKINS_URL` 报错

**原因**

**解决方案** 不使用 `--remoting` 参数



## 3 Jenkins Plugin

> 扩展
> https://blog.csdn.net/pansaky/article/details/80755739
> https://blog.csdn.net/chinabluexfw/article/details/7484311

开源版本的Jenkins具有三大能力：
- Master-Slave的分布式构建调度能力
- Pipeline编排能力
- 强大的开源生态（插件）能力。
本节主要介绍一些常用的插件及简单的用法说明。

### 3.1 插件安装

插件安装有两种安装方式：

1.在线安装

​	登录Jenkins，进入 `系统设置 - 插件管理 - 可选插件`，选择完成后，点击 `直接安装`  或 `下载待重启后安装`。

2.离线安装

​	进入[Jenkins插件官网](https://plugins.jenkins.io/)，搜索指定插件并下载安装包。

​	方式一: 将下载到的插件安装包放入 `JENKINS_HOME/plugins` 目录中，重启Jenkins服务

​	方式二: 使用 [命令行安装](## 2 Jenkins Cli) 方式进行安装

### 3.2 插件说明（Comonly Used Plugins）

#### 3.2.1 用户及权限管理

> 根据业务需求，选择合适的用户和权限管理插件。
>
> 官方插件列表： https://plugins.jenkins.io/?labels=user
>
> * https://jenkins.io/doc/book/managing/security/#authorization

##### 3.2.1.1 认证管理

###### 3.2.1.1.1 ldap

- 插件地址: https://plugins.jenkins.io/ldap

连接 `LDAP`，使用 `LDAP` 进行用户认证， `LDAP` 服务器可以是 `Active Directory` 或者 `OpenLDAP`。

**插件配置**

进入 `系统管理（Manage Jenkins） - 全局安全配置（Configure Global Security） - 启用安全（Enable security）`

选择使用 `LDAP` 配置

![jenkins-ldap-1](image/jenkins-ldap-1.png)

详细配置类似下图所示，根据业务情况进行配置

![jenkins-ldap-2](image/jenkins-ldap-2.png)



###### 3.2.1.1.2 Active Directory

> **Notice**
>
> ​	基于Windows Active Directory进行域管理的企业，推荐使用Active Directory。

* 插件地址: https://plugins.jenkins.io/active-directory

这个插件允许使用 `Active Directory` 对用户进行认证，同时结合诸如 `Matrix Authorization Strategy` 等插件，可以识别用户所在的所有用户组，对用户授权进行灵活配置。

###### 3.2.1.1.3 GitHub Authentication

- 插件地址: https://plugins.jenkins.io/github-oauth

这个插件提供了使用 `GitHub` 进行用户认证和授权的方案。

###### 3.2.1.1.2 GitLab Authentication

* 插件地址: https://plugins.jenkins.io/gitlab-oauth

这个插件提供了使用 `GitLab` 进行用户认证和授权的方案。

###### 3.2.1.1.2 openid

- 插件地址: https://plugins.jenkins.io/openid

这个插件提供了使用 `openid` 进行用户认证和授权的方案

##### 3.2.1.2 权限管理

###### 3.2.1.2.1 role-strategy

- 插件地址: https://plugins.jenkins.io/openid

这个插件提供了一种基于角色（Role）的用户权限管理策略，支持创建 `global` 角色、`Project` 角色、 `Slave` 角色，以及给用户分配这些角色。这款插件是最常用的Jenkins权限策略和管理插件。

###### 3.2.1.2.2  Matrix Authorization Strategy

* 插件地址: https://plugins.jenkins.io/matrix-auth

这个插件提供了基于矩阵的授权策略，支持全局和项目级别的配置。

##### 3.2.1.3 其他

###### 3.2.1.2.1 avatar

* 插件地址: https://plugins.jenkins.io/avatar

A new section appears in the user configuration page. You can upload any image type that Java ImageIO understands (JPEG, PNG, BMP, GIF). Transparency (in image formats that support it) is preserved. Animated image formats (GIF, PNG) are respected (requires display support by browser).

Once an avatar has been attached to a user the avatar is displayed on the user page (e.g. `http``://[jenkins-root]/user/<username>`)`.`

The avatar is also available directly for use by other plugins and pages at:

```
 http://[jenkins-root]/user/<username>/avatar/image
```

To remove an avatar simply click upload with no file selected.

> **WARNING: Avatar images are held in heap memory. Keep image sizes to a minimum to avoid memory issues.**

#### 3.2.2 视图 

##### 3.2.2.1 List view Jenkins

默认支持List类型的视图，用户可以创建List视图来过滤所关心的项目。

##### 3.2.2.2 sectioned-view

- 插件地址: https://plugins.jenkins.io/sectioned-view

定义section视图，这个插件支持一种新的视图，视图可以分为多个部分，每部分可以单独配置显示所选择的项目信息。可用于Jenkins平台概述说明及工具分类展示等功能。

##### 3.2.2.3 Build Pipeline

> 不常用，根据业务情况选择使用。

- 插件地址: https://plugins.jenkins.io/build-pipeline-plugin

这个插件提供了一种Build Pipeline视图，用于显示上下游项目构建的关系。

##### 3.2.2.4 Folder

> 不常用，根据业务情况选择使用

- 插件地址: https://plugins.jenkins.io/cloudbees-folder

这个插件支持用户使用目录管理项目，目录支持嵌套，并且支持在目录中创建视图。

##### 3.2.2.5 Nested View

> 不常用，根据业务情况选择使用。与Folder插件功能类似，如果业务需要，建议使用`List view ` + `Folder插件`能力。

- 插件地址: https://plugins.jenkins.io/nested-view

这个插件支持一种新的视图，它不是直接显示项目，而是以目录图标显示所包含的子视图，每个子视图显示所选项目信息。

#### 3.2.3 节点

> 1.创建节点
>
> ​	In 1.x version it was called "Dumb slave" and in modern versions "Permanent Agent" 
>
> 2.没有【Launch agent via Java Web Start】选项
>
> ​	进入`Manage Jenkins > Configure Global Security > TCP port for JNLP agents `，开启【TCP port for JNLP agents】，使用随机选取模式
>
> 3.节点配置说明
>
> ![](image/jenkins-slave-1.png)
>
> * 【# of executors】根据CPU的个数来填写数量
>
> * 【远程工作目录】这个就是用来存放master到slave时，存放的临时目录，如slave的服务软件也会放在此，并且会以每个job名称来区分开
>
> * 【用法】只需要选择【只允许运行绑定到这台机器的Job】这种模式下，Jenkins只会构建哪些分配到这台机器的Job。这允许一个节点专门保留给某种类型的Job。例如，在Jenkins上连续的执行测试，你可以设置执行者数量为1，那么同一时间就只会有一个构建，一个实行者不会阻止其它构建，其它构建会在另外的节点运行。
>
> * 【启动方式】只需要选择【Launch agent via Java Web Start】，以服务的方式启动，应用最广且最好配置，其余的都太复杂，不建议使用。注意：2.x版本的默认没有这个选项，需要单独开启，参考：

##### 3.2.3.1 Linux节点

###### 3.2.3.1.1 ssh-slaves

- 插件地址: https://plugins.jenkins.io/ssh-slaves
- 依赖插件:
  - JDKTool(https://plugins.jenkins.io/jdk-tool)

这个插件支持Unix及类Unix操作系统的节点机器(slave)使用ssh-slave连接。

节点配置启动方式选择 `Launch agent agents via SSH`

使用秘钥验证，参考 [Host Key Verification for SSH Agents](https://support.cloudbees.com/hc/en-us/articles/115000073552-Host-Key-Verification-for-SSH-Agents)

##### 3.2.3.2 Windows节点

> 内置功能，进入 `系统管理（Manage Jenkins） - 全局安全配置（Configure Global Security） - 启用安全（Enable security）`
>
> 开启 `TCP port for inbound agents` 功能，选择指定 `5000` 端口。

Jenkins内置功能支持Windows操作系统的节点机器(slave)进行连接。

根据节点配置说明进行配置，启动方式选择 `Launch agent by connecting it to the master`，配置完成后点击下载agent.jar文件保存在本地并拷贝至slave所在的虚拟机。配置完成后点击保存，节点内容如下图所示。

![](image/jenkins-slave-2.png)

在slave所在的虚拟机命令行中运行如下命令连接节点。设置自动启动 [参考](https://blog.csdn.net/liuchunming033/article/details/48652097)

```bat
java -jar agent.jar -jnlpUrl http://localhost:8080/computer/jiuchou/slave-agent.jnlp -secret 2dd5c0b34273430f5c0ec1d03117005751eb48041b25e615cabd204e532c9463 -workDir "D:\jenkins"
```

**Notice**

启动方式也可选择 `Launch agent via Java Web Start`，配置完成后点击launch按钮，根据提示下载slave-agent.jnlp文件保存在本地并拷贝至slave所在的虚拟机。（新版本[Jenkins ver. 2.176](https://jenkins.io/)貌似已废除此方式，待确定。）

##### 3.2.3.3 Docker节点

Jenkins的Master-Slave架构实现了分布式构建，可以充分地横向扩展Slave来提升构建能力，将Slave容器化是目前主流的构建环境标准化、集群化和弹性化的方式。

###### 3.2.3.3.1 Docker

* 插件地址: https://plugins.jenkins.io/docker-plugin

这个插件可以配置docker host，从而动态地提供Jenkins Agent（Slave），运行构建后再销毁这个Slave。

###### 3.2.3.3.2 Kubernetes

- 插件地址: https://plugins.jenkins.io/kubernetes

这个插件支持利用Kubernetes cluster动态提供Jenkins Agent（Slave），利用Kubernetes调度机制来优化Jenkins负载等。

##### 3.2.3.4 Slave Monitor

###### 3.2.3.4.1 Slave Monitor for system load average

* 插件地址: https://plugins.jenkins.io/systemloadaverage-monitor

待补充

#### 3.2.4 代码管理

> - Jenkins subversion Credentials

在Jenkins项目中，通过配置Source Code Management去下载代码进行构建任务，是非常普遍的应用场景。Jenkins插件支持多种SCM系统，最常见的系统是Git和SVN。

##### 3.2.4.1 git

* 插件地址: https://plugins.jenkins.io/git

支持使用GitHub、GitLab、Girrit等系统管理代码仓库。

##### 3.2.4.2 subversion

- 插件地址: https://plugins.jenkins.io/subversion
- 依赖插件
  - mapdb-api(https://plugins.jenkins.io/mapdb-api)
  - scm-api(https://plugins.jenkins.io/scm-api)
  - command-launcher(https://plugins.jenkins.io/command-launcher)

支持使用Subversion系统管理代码仓库。

#### 3.2.5 构建

##### 3.2.5.1 构建参数

Jenkins除了支持普通的参数类型（Boolean、String、Multi-line String、Choice和File）外，还有一些插件能够支持更加丰富实用的参数类型，比如参数间动态关联、多层级参数、隐藏参数、文件参数等。

###### 3.2.5.1.1 Nodelabelparameter（未验证）

- 插件地址: https://plugins.jenkins.io/nodelabelparameter

这个插件增加了新的参数类型Node和Label，从而使用户可以通过参数选择项目构建运行的节点。

###### 3.2.5.1.2 待整理

* https://plugins.jenkins.io/hidden-parameter
* https://plugins.jenkins.io/extended-choice-parameter
* https://plugins.jenkins.io/validating-string-parameter
* https://plugins.jenkins.io/extensible-choice-parameter
* https://wiki.jenkins.io/display/JENKINS/Active+Choices+Plugin

##### 3.2.5.2 构建触发

Jenkins支持多种Build触发方式，其中的一些自动化触发方式非常有用。

###### 3.2.5.2.1 Build periodically

Jenkins内置策略，可以设置类似crontab时间，实现周期性地自动触发构建。

###### 3.2.5.2.2 Poll SCM

Jenkins内置功能，类似Build periodically，可以设置类似crontab时间，不同之处在于，不是直接进行构建，而是周期性地在后台检查所配置的SCM有没有更新，只有当有代码更新时才触发构建。

###### 3.2.5.2.3 GitHub Integration

- 插件地址: https://plugins.jenkins.io/github-pullrequest

这个插件将Jenkins集成到GitHub中，支持GitHub分支及Pull requests触发Jenkins构建。这个插件将Jenkins集成到GitHub中，支持GitHub分支及Pull requests触发Jenkins构建。

###### 3.2.5.2.4 GitLab

- 插件地址: https://plugins.jenkins.io/github-pullrequest

这个插件将Jenkins集成到GitLab web hook中，支持Gitlab分支及Merge Request等相关事件触发Jenkins构建。

###### 3.2.5.2.4 GitLab

- 插件地址: https://plugins.jenkins.io/gitlab-plugin

这个插件将Jenkins集成到GitHub中，支持GitHub分支及Pull requests触发Jenkins构建。这个插件将Jenkins集成到GitHub中，支持GitHub分支及Pull requests触发Jenkins构建。

###### 3.2.5.2.5 Gerrit Trigger

- 插件地址: https://plugins.jenkins.io/gerrit-trigger

这个插件将Jenkins集成到Gerrit code review中，支持Jenkins配置Gerrit服务器等信息，实现Gerrit event 触发Jenkins构建。

###### 3.2.5.2.6 JIRA Trigger

- 插件地址: https://plugins.jenkins.io/jira-trigger

这个插件将Jenkins集成到Jira WebHooks中，支持在Jira issue的状态等变化时触发Jenkins构建。

#### 3.2.6 易用性工具插件

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

#### 3.2.7 其他主流插件 

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

#### 3.2.8 Docker插件

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

#### 3.2.9 其他

**coverity插件**

> Coverity 2018.12之后版本，使用`synopsys-coverity`插件

```
官网地址: 
仓库地址: https://plugins.jenkins.io/synopsys-coverity
功能: 
说明: 
```

**log-parser-plugin**

> s 

```
官网地址: https://wiki.jenkins.io/display/JENKINS/Log+Parser+Plugin
仓库地址: 
功能: 
说明: 
```

#### 3.2.10 Admin相关插件

##### 3.2.10.1 Configuration Slicing

- 插件地址: https://plugins.jenkins.io/configurationslicing

这个插件支持批量修改项目配置。

##### 3.2.10.2 Mask Passwords

- 插件地址: https://plugins.jenkins.io/mask-passwords

这个插件支持遮挡构建log输出的password等敏感信息。

##### 3.2.10.3 Backup

- 插件地址: https://plugins.jenkins.io/backup

这个插件负责将备份功能添加到Jenkins management中。

## 4 API调用

* 参考：
  * [Python-Jenkins API使用 —— 在后端代码中操控Jenkins](https://www.cnblogs.com/znicy/p/5498609.html)

### 4.1 使用 Linux curl 调用API

> 详细内容查看官网介绍: [Remote access API](https://wiki.jenkins.io/display/JENKINS/Remote+access+API)

该方式是通过命令行直接调curl去发POST请求的方式来触发job的构建。

#### 4.1.1 使用简介

**sending "String Parameters"**

```bash
# CRUMB 需要通过 JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb) 获取
# 参考 `4.1.2 参数说明`
curl -X POST -H "${CRUMB}" JENKINS_URL/job/JOB_NAME/build \
  --user USER:TOKEN \
  --data-urlencode json='{"parameter": [{"name":"id", "value":"123"}, {"name":"verbosity", "value":"high"}]}'
```

**sending a "File Parameter"**

```bash
curl -X POST -H "${CRUMB}" JENKINS_URL/job/JOB_NAME/build \
  --user USER:PASSWORD \
  --form file0=@PATH_TO_FILE \
  --form json='{"parameter": [{"name":"FILE_LOCATION_AS_SET_IN_JENKINS", "file":"file0"}]}'
```

#### 4.1.2 参数说明

##### 4.1.2.1 API Token

对于用openid管理的Jenkins，需要带上参数--user USERNAME:PASSWORD，其中的USERNAME和PASSWORD不是你的openID登录的账号密码，而是登录后显示在Jenkins中的User Id和API Token。

API Token的查看方式为

**Jenkins1.x**

使用openID登录jenkins -> 点击右上角用户名，进入用户个人页面 -> 点击左边的设置，打开设置页面 -> API Token，Show Api Token... 

**Jenkins2.x**

使用openID登录jenkins -> 点击右上角用户名，进入用户个人页面 -> 点击左边的设置，打开设置页面 -> API Token（创建时显示后保存，之后无法查看，如果忘记需要重新设置）


##### 4.1.2.2 CSRF Protection

> 如果CSRF开启，需使用crumb，否则会出现报错：`Error 403 No valid crumb was included in the request`

官网说明

If your Jenkins uses the "Prevent Cross Site Request Forgery exploits" security option (which it should), when you make a `POST` request, you have to send a CSRF protection token as an HTTP request header.
For curl/wget you can obtain the header needed in the request from the URL `JENKINS_URL/crumbIssuer/api/xml` (or `.../api/json`). Something like this:

```
wget -q --auth-no-challenge --user USERNAME --password PASSWORD --output-document - \
'JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'
```

This will print something like ".crumb:1234abcd", which you should add to the subsequent request.

###### 4.1.2.2.1 解决方案实例

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

###### 4.1.2.2.2 问题记录说明

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

### 4.3 Groovy 调用 Jenkins API

- https://wiki.jenkins.io/display/JENKINS/Authenticating+scripted+clients

## 5 信息获取

### 5.1 Jenkins 获取操作者的信息

#### 5.1.1 远程获取

```bash
# 使用 xml 格式
curl -o api.xml -X POST "$JENKINS_URL/job/$JOB_NAME/$BUILD_NUMBER/api/xml"
operatingUser=$(cat api.xml | grep 'userId' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}')
buildUrl=$(cat api.xml | grep '<url>' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}')
# 获取构建状态
build_status=`grep 'result' temp.xml`
build_status=${build_status##*<result>}
build_status=${build_status%%</result>*}

# 使用 json 格式
curl -o api.json -X POST "$JENKINS_URL/job/$JOB_NAME/$BUILD_NUMBER/api/json"
operatingUser=$(cat api.json | jq .actions[0].causes[0].userId)
buildUrl=$(cat api.json | jq .url)
```

#### 5.1.2 本工程内获取

```bash
JOB_NAME
BUILD_URL
```



## 6 可借鉴整理

* [使用 Jenkins 执行持续集成的几个实用经验分享](https://blog.csdn.net/aixiaoyang168/article/details/80636544)

* Jenkins-cli 自动化构建工具（1）https://www.jianshu.com/p/45f010d63ff3

* [Jenkins实现前端项目自动化集成打包部署](https://segmentfault.com/a/1190000011121770)

* Why use Conditional step (single)?： https://wiki.jenkins.io/pages/viewpage.action?pageId=59507542

* Converting Conditional Build Steps to Jenkins Pipeline： https://jenkins.io/blog/2017/01/19/converting-conditional-to-pipeline/

  

## 7 更新记录

```
2019.02.13: 完成初稿，包含Jenkins服务器安装概述、主流插件概述、Jenkins API等内容
2019.02.17: 完善API接口调用内容
2019.03.14: 完善实际使用中可能存在的问题记录
2019.05.09: 增加windows平台安装Jenkins服务的详细说明
2019.05.12: 完善Jenkins插件内容
2019.06.09: 增加信息获取内容
```

