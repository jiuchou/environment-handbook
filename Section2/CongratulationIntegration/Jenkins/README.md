# Jenkins

## 1 Installing Jenkins

* [Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/)

### 1.1 物理机/虚拟机 

* [Linux: Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/#docker)

### 1.2 Docker

* [Docker: Jenkins服务器安装 官方文档](https://jenkins.io/doc/book/installing/#linux)

> 前提：
>
> ​	安装Docker()

*Run Jenkins in Docker*

```bash
docker run -p 8080:8080 -p 50000:50000 -v localPath:dockerPath --user root -d --name JenkinsServer jenkins/jenkins:lts
```


## 2 Install Jenkins Plugin

*Install Jenkins Plugin*

```bash
java -jar jenkins-cli.jar -s JENKINS_URL command command options...
```

For example:

```bash
java -jar /var/jenkins_home/war/WEB-INF/jenkins-cli.jar -remoting -s http://localhost:8080 install-plugin /var/jenkins_home/plugins/ssh-slaves.hpi -deploy
```

## 3 Comonly Used Plugins

 
 插件
 https://plugins.jenkins.io/

 * jenkins全局脚本

https://wiki.jenkins.io/display/JENKINS/Global+Post+Script+Plugin

 

* Install Plugins
https://plugins.jenkins.io/ldap
https://plugins.jenkins.io/role-strategy

视图
https://plugins.jenkins.io/sectioned-view

slave节点
https://plugins.jenkins.io/ssh-slaves
报错,安装JDKTool
https://plugins.jenkins.io/jdk-tool

Jenkins 2.x版本的节点配置选项更新
http://www.cnblogs.com/EasonJim/p/5997490.html

https://plugins.jenkins.io/heavy-job

scm svn
https://plugins.jenkins.io/subversion
https://plugins.jenkins.io/mapdb-api
https://plugins.jenkins.io/scm-api
https://plugins.jenkins.io/command-launcher

时间
https://plugins.jenkins.io/timestamper
获取变量$BUILD_TIMESTAMP
https://plugins.jenkins.io/build-timestamp

颜色
https://plugins.jenkins.io/ansicolor

SSH Slaves Plugin
https://support.cloudbees.com/hc/en-us/articles/115000073552-Host-Key-Verification-for-SSH-Agents
https://github.com/jenkinsci/ssh-slaves-plugin

docker
https://plugins.jenkins.io/docker-custom-build-environment
https://plugins.jenkins.io/docker-commons
https://plugins.jenkins.io/docker-slaves

set builder description
https://plugins.jenkins.io/description-setter

Editable Email Notification
https://plugins.jenkins.io/email-ext

https://plugins.jenkins.io/downstream-buildview

> * Jenkins subversion Credentials

> * Jenkins Restart Plugin
https://plugins.jenkins.io/rebuild

https://plugins.jenkins.io/groovy
https://plugins.jenkins.io/jobConfigHistory
https://plugins.jenkins.io/schedule-build

查看build的环境变量
https://plugins.jenkins.io/build-environment

全局脚本
Global Post Script Plugin
https://plugins.jenkins.io/global-post-script

coverity插件
https://plugins.jenkins.io/synopsys-coverity

在主页面显示最新构建的log
https://plugins.jenkins.io/display-console-output

https://plugins.jenkins.io/downstream-buildview

workspace clean
https://plugins.jenkins.io/ws-cleanup

1.install docker
2.user group
groupadd jenkins
useradd -d /home/jenkins -s /bin/bash -c "jenkins user" -g jenkins -G docker -m -p "jenkins" jenkins
3.run docker
mkdir /home/jenkins/jenkins_home
docker pull jenkinsci/blueocean
docker run -u jenkins -d --name JenkinsServer -p 8080:8080 -p 50000:50000 -v /home/jenkins/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean


