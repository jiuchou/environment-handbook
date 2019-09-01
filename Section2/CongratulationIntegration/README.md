# 持续集成相关

* jenkins获取传参中包含的特殊字符，如"$"

* https://wiki.jenkins.io/display/JENKINS/Groovy+plugin
* groovy – 让Jenkins上游工作 https://cloud.tencent.com/developer/ask/175727
* https://stackoverflow.com/questions/21236268/access-to-build-environment-variables-from-a-groovy-script-in-a-jenkins-build-st/26428580#26428580
* https://wiki.jenkins.io/display/JENKINS/Parameterized+System+Groovy+script



* jenkins命令行 https://510888780.iteye.com/blog/2207693



* [W3School：Jenkins中文文档](https://www.w3cschool.cn/jenkins/)

## API

* https://javadoc.jenkins.io/
* 第三方库
  * https://pypi.org/project/jenkinsapi/
  * https://python-jenkins.readthedocs.io/en/latest/install.html#documentation
* 博客
  * https://blog.csdn.net/nklinsirui/article/details/80832005
  * https://www.cnblogs.com/znicy/p/5498609.html

## groovy

* 使用Groovy操作文件
  * https://blog.csdn.net/chenyulancn/article/details/65443468

* 使用 Groovy 語言自動操作 Jenkins

  * https://www.codercto.com/a/3207.html

* [How to use groovy script on jenkins](https://www.cnblogs.com/root-wang/p/4569095.html)

* [How to get classpath in Groovy?](https://stackoverflow.com/questions/5212442/how-to-get-classpath-in-groovy)

## Jenkins Plugin


* https://plugins.jenkins.io/monitoring
* 界面登录： https://plugins.jenkins.io/autoaction-step
* 触发人信息： https://plugins.jenkins.io/buildtriggerbadge



* 多工程配置 https://plugins.jenkins.io/jenkins-multijob-plugin
  * Jenkins Multijob plugin version 1.32
    * maven-plugin v2.6 is missing. To fix, install v2.6 or later.
      * https://updates.jenkins.io/2.121/latest/maven-plugin.hpi
        * https://plugins.jenkins.io/javadoc
    * conditional-buildstep v1.3.3 is missing. To fix, install v1.3.3 or later.
      * https://plugins.jenkins.io/conditional-buildstep
        * https://plugins.jenkins.io/run-condition
    * envinject v1.90 is missing. To fix, install v1.90 or later.
      * https://plugins.jenkins.io/envinject
        * https://plugins.jenkins.io/envinject-api
    * built-on-column v1.1 is missing. To fix, install v1.1 or later.
      * https://plugins.jenkins.io/built-on-column
    * parameterized-trigger v2.25 is missing. To fix, install v2.25 or later.
      * https://plugins.jenkins.io/parameterized-trigger


jenkins模板插件

```bash
<hudson.plugins.templateproject.ProxyBuilder plugin="template-project@1.5.2">
```