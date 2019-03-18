# Jenkins 命令行

## 命令行使用问题

### Jenkins2.x 

#### 1 `anonymous is missing the Job/Create permission`

**报错信息** `anonymous is missing the Job/Create permission`

**操作内容** 执行 `java -jar jenkins-cli.jar --remoting -s JENKINS_URL` 报错

**原因**

**解决方案** 不使用 `--remoting` 参数



