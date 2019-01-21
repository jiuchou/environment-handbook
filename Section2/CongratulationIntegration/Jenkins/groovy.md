# groovy

http://www.groovy-lang.org/documentation.html


## 使用

> 安装groovy插件

### 配置

系统管理 - 全局工具配置 - Groovy

groovy2.5.5
/var/jenkins_home/jiuchou/groovy2.5.5



jenkins 调用外部groovy script的方法

当使用load(path)方法调用外部groovy script的时候，路径使用单引号是调用当前WORKSPACE下的相对路径，路径使用双引号是直接使用绝对路径。例如：

file=load '/folder1/script1' 实际上是加载${WORKSPACE}/folder1/script1

file=load "/folder1/script1" 实际上加载/folder1/script1



jenkins plugin
groovy-postbuild
https://blog.csdn.net/gzh8579/article/details/59522469

groovy + job-dsl触发构建
https://www.cnblogs.com/learnbydoing/p/6734525.html


Ubuntu搭建groovy
https://blog.csdn.net/gxgxyjy062/article/details/77891981


jenkins通过groovy获取build环境变量
https://stackoverflow.com/questions/21236268/access-to-build-environment-variables-from-a-groovy-script-in-a-jenkins-build-st/26428580#26428580
