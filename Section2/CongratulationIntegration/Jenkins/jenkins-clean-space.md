# Jenkins 清理空间

> Jenkins常用脚本：
>
> ​	[Jenkins Script Console](https://wiki.jenkins.io/display/JENKINS/Jenkins+Script+Console)

## 1 历史记录

> script页面访问方式
>
> 1. 系统管理-脚本命令行
> 2. JenkinsUrl/script

删除build历史记录

**Jenkins 服务器后台**

1. Check your home jenkins directory: **"Manage Jenkins" ==> "Configure System"**

   ```bash
   # Command for delete all jenkins job builds
   cd /jenkins_home/jobs
   rm -rf */builds/*
   
   # 删除30天之前的构建记录
   find [1-9]* -type d -mtime +30 -exec rm -rf {} \;
   
   # 删除Build Number为1到7的构建记录
   find [1-7] -type d -exec rm -rf {} \;
   ```

2. After delete should reload config: **"Manage Jenkins" ==> "Reload Configuration from Disk"**

**脚本命令行**

> Groovy Scripts using Hudson API 

删除指定工程的build记录

```groovy
Jenkins.instance.getItemByFullName({YOUR_JOB_NAME}).builds.findAll { it.number >={START_SN} && it.number <= ${END_SN} }.each { it.delete() }
```

删除所有工程的build记录

```groovy
import hudson.model.*
// For each project
for(item in Hudson.instance.items) {
  // check that job is not building
  if(!item.isBuilding()) {
    System.out.println("Deleting all builds of job "+item.name)
    for(build in item.getBuilds()){
      build.delete()
    }  
  }
  else {
    System.out.println("Skipping job "+item.name+", currently building")
  }
}
```

Or for cleaning all workspaces :

```
import hudson.model.*
// For each project
for(item in Hudson.instance.items) {
  // check that job is not building
  if(!item.isBuilding()) {
    println("Wiping out workspace of job "+item.name)
    item.doDoWipeOutWorkspace()
  }
  else {
    println("Skipping job "+item.name+", currently building")
  }
}
```

There are a lot of examples on the [Jenkins wiki](https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+Script+Console) 

**Linux 命令行之 curl**

```bash
curl -u userName:apiToken -X POST http://jenkins-host.tld:8080/jenkins/job/myJob/[1-56]/doDeleteAll
```

**Linux 命令行之 jenkins-cli**

```bash
java -jar jenkins-cli.jar -s http://my.jenkins.host delete-builds myproject '1-7499' --username $user --password $password
```

重置Jenkins的build序号

```groovy
item = Jenkins.instance.getItemByFullName("your-job-name-here")
//THIS WILL REMOVE ALL BUILD HISTORY
item.builds.each() { build ->
  build.delete()
}
item.updateNextBuildNumber(1)
```

## 2 工作空间

### 2.1 清理工作空间

#### 2.1.1 界面操作

进入工程，清理工作空间。

#### 2.1.2 服务器后台

**使用master进行构建**

> 除了一些Jenkins相关的维护Jobs外，我们不推荐使用master运行常规编译等构建任务。 

如果使用了master运行构建，默认构建的工作区 `jenkins_home/jobs/myJob/workspace`，当然这个工作区会占用master 上的磁盘空间大小，一会影响 `jenkins_home` 的大小，数据备份的时候 workspace 可以不用备份。 

**使用slave进行构建**

使用slave进行构建，构建的工作区会创建在slave上，具体的默认路径是  `<Slave remote root directory>/workspace/myJob`， 当然这个工作区会占用slave的磁盘空间，slave磁盘空间满会造成构建失败。 

#### 2.1.3 配置-丢弃旧的构建(Discard old builds)

把以前构建过的过时历史数据自动清除掉，保留最近更新的天数和个数，实现控制工作空间大小的能力。

> 根据项目实际情况制定策略，如：
>
> * 保持构建的天数 10
> * 保持构建的最大个数 30
>
> 
>
> 批量配置Discard old builds选项
>
> 1. 如果已经配置了很多Jenkins job，逐个来修改Discard old builds，非常费时费力。可以使用 [Configuration Slicing plugin](https://wiki.jenkins.io/display/JENKINS/Configuration+Slicing+Plugin) 插件进行批量配置。
>
> 2. 批量配置步骤
>
>    Manage Jenkins -> Configuration Slicing
>
>    分别打开以下菜单，在左边的“Configured Value”中填入新的值 
>
>    * Discard Old Builds Slicer - Days to keep artifacts
>    * Discard Old Builds Slicer - Days to keep builds
>    * Discard Old Builds Slicer - Max # of builds to keep
>    * Discard Old Builds Slicer - Max # of builds to keep with artifacts


#### 2.1.4 插件清理

[Workspace+Cleanup+Plugin](https://wiki.jenkins.io/display/JENKINS/Workspace+Cleanup+Plugin)

**构建前清理**

Build Environment -> Delete workspace before build starts

**构建后清理**

Post-build Actions -> Delete workspace when build is done

#### 2.1.5 使用 Linux curl 调用 Rest API 清理

```bash
curl -u "username:password" JENKINS_URL/job/JOB_NAME/doWripOutWorkspace
```

#### 2.1.6 使用 Groovy 脚本清理

* 参考
  * Wipe out workspaces of all jobs
    https://wiki.jenkins.io/display/JENKINS/Wipe+out+workspaces+of+all+jobs
  * Wipe workspaces for a set of jobs on all nodes
    https://wiki.jenkins.io/display/JENKINS/Wipe+workspaces+for+a+set+of+jobs+on+all+nodes

* 扩展
  * https://wiki.jenkins.io/display/JENKINS/Jenkins+Script+Console#JenkinsScriptConsole-ExampleGroovyscripts

* Jenkins视屏
  * https://edu.csdn.net/course/play/8981/186399(待整理)

配置工程（工程名为 `doWripOutWorkspace`，参数为`projectName`），清理Jenkins中制定工程的工作空间

```groovy
import hudson.model.*
import jenkins.model.Jenkins

projectName = Jenkins.instance.getItem('doWripOutWorkspace').getLastBuild().getBuildVariables().get('projectName')
// For each project
for(item in Hudson.instance.items) {
	jobName = item.getFullDisplayName()
    if (jobName == projectName) {
        customWorkspace = item.getCustomWorkspace()
        for (node in Hudson.getInstance().getNodes()) {
            workspacePath = node.getWorkspaceFor(item)
            if (workspacePath == null) {
                println("Warning: Can't get workspace path!")
            } else {
                if (customWorkspace != null) {
                    workspacePath = node.getRootPath().child(customWorkspace)
                }

                if (workspacePath.exists()) {
                    workspacePath.deleteRecursive()
                    println("Node: " + node.getDisplayName())
                    println("Deleted from location " + workspacePath.getRemote())
                }
            }
        }
    }
}
```

#### 2.1.7 清理工程已经删除的工作空间 

直接删除Jenkins Job，并没有先**清理工作空间**，这样会导致有些被删除的Jenkins Job原来的工作空间一直存在，导致无用数据占用磁盘，需要清理。

**使用 jenkinsapi**

> 参考：[jenkinsapi](jenkinsapi.md)
>
> 来自：[删除Jenkins JOB后清理workspace](https://my.oschina.net/donhui/blog/677935)

```python
# -*- coding: utf-8 -*-
import os
import shutil
import logging

from jenkinsapi.jenkins import Jenkins

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


def get_jenkins_instance():
    jenkins_url = "http://jenkins.example.com"
    jenkins_username = "username"
    jenkins_password = "password"
    return Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)


def clean_workspace():
    jenkins_instance = get_jenkins_instance()

    jenkins_workspace_path = "/opt/JENKINS_HOME/workspace/"

    for dirpath, dirnames, filenames in os.walk(jenkins_workspace_path):
        if dirpath == jenkins_workspace_path:
            for dirname in dirnames:
                jenkins_job_name = dirname
                # 如果job被删除，则清理相应的workspace
                if not jenkins_instance.has_job(jenkins_job_name):
                    logger.info("removing workspace dir of job:%s" % dirname)
                    shutil.rmtree(os.path.join(dirpath, dirname))


if __name__ == "__main__":
    clean_workspace()
```

## 更新记录

```
2019.02.24: 初步整理，增加历史记录、工作空间相关内容。
```




