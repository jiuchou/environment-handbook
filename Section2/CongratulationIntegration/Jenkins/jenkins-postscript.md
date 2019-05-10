### ldap

* https://plugins.jenkins.io/ldap
* https://github.com/jenkinsci/ldap-plugin

* https://wiki.jenkins.io/display/JENKINS/LDAP+Plugin

系统管理 - 全局安全配置 - Enable security -  LDAP

```
Server							ldap://ldap.example.com
root DN 						OU=ldap,DC=example,DC=com
User search filter				sAMAccountName={0}
Manager DN						jiuchou@example.com
Manager Password				123456
Display Name LDAP attribute		displayname
Email Address LDAP attribute	mail
```



* [Jenkins实现前端项目自动化集成打包部署](https://segmentfault.com/a/1190000011121770)



Jenkins API使用

**sending "String Parameters"**

```bash
# CRUMB 需要通过 JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb) 获取
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



Groovy 调用 Jenkins API

* https://wiki.jenkins.io/display/JENKINS/Authenticating+scripted+clients
