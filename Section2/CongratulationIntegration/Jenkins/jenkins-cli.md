# Jenkins 命令行

## 命令行使用问题

### Jenkins1.609.1 

#### 1 `Failed to authenticate with you SSH keys`

* 参考: [来自Jenkins-CI的命令行登录告警问题](http://jenkins-ci.361315.n4.nabble.com/jenkins-command-line-Failed-to-authenticate-with-your-SSH-keys-td4642440.html)

**报错信息** `[WARN] Failed to authenticate with you SSH keys. Proceeding as anonymous`

**操作内容** 执行 `java -jar jenkins-cli.jar -s JENKINS_URL login --username USERNAME --password PASSWORD` 提示告警信息

**原因** CLI authenticates the user according to the public key stored in users Jenkins configuration.
So for this to work, we need the public key corresponding to the private key that you specify in the command line is specified in the configuration of the corresponding user.

**解决方案** 进入 `http://JENKINS_URL/user/USERNAME/configure`，添加公钥到 `SSH Public Keys` 中

### Jenkins2.150.1

#### 1 `anonymous is missing the Job/Create permission`

**报错信息** `anonymous is missing the Job/Create permission`

**操作内容** 执行 `java -jar jenkins-cli.jar --remoting -s JENKINS_URL` 报错

**原因**

**解决方案** 不使用 `--remoting` 参数

