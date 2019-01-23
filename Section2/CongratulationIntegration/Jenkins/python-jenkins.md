# Python 使用Jenkins Rest API 之 python-jenkins

* 参考

  * [Python-Jenkins API使用 —— 在后端代码中操控Jenkins](https://www.cnblogs.com/znicy/p/5498609.html)
* 说明
  * [Python-Jenkins 官网](https://pypi.python.org/pypi/python-jenkins/)
  * [Python-Jenkins 官方文档](https://pypi.python.org/pypi/python-jenkins/)

### 1.1 安装

```bash
pip install python-jenkins
```

### 1.2 基础使用

```python
import jenkins
#定义远程的jenkins master server的url，以及port
jenkins_server_url='xxxx:xxxx'
#定义用户的User Id 和 API Token，获取方式同上文
user_id='xxxx'
api_token='xxxx'
#实例化jenkins对象，连接远程的jenkins master server
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
#构建job名为job_name的job（不带构建参数）
server.build_job(job_name)

#String参数化构建job名为job_name的job, 参数param_dict为字典形式，如：param_dict= {"param1"：“value1”， “param2”：“value2”} 
server.build_job(job_name, parameters=param_dict)

#获取job名为job_name的job的相关信息
server.get_job_info(job_name)

#获取job名为job_name的job的最后次构建号
server.get_job_info(job_name)'lastBuild'

#获取job名为job_name的job的某次构建的执行结果状态
server.get_build_info(job_name,build_number)['result']　　   

#判断job名为job_name的job的某次构建是否还在构建中
server.get_build_info(job_name,build_number)['building']

```



待整理

https://stackoverflow.com/questions/23497819/trigger-parameterized-build-with-curl-and-crumb

https://stackoverflow.com/questions/38137760/jenkins-rest-api-create-job

https://blog.csdn.net/tiandaochouqin99/article/details/79893107

https://stackoverflow.com/questions/12322668/jenkins-python-api-authentication-403-forbidden

https://python-jenkins.readthedocs.io/en/latest/examples.html

https://pypi.org/project/kerberos/#history

https://stackoverflow.com/questions/16738441/how-to-request-for-the-crumb-issuer-for-jenkins

https://www.jianshu.com/p/68dd714e6c31

https://blog.csdn.net/tiandaochouqin99/article/details/79893107

https://www.cnblogs.com/znicy/p/5498609.html


jenkins-api
https://github.com/pycontribs/jenkinsapi
https://jenkinsapi.readthedocs.io/en/latest/using_jenkinsapi.html#example-1-get-version-of-jenkins
https://stackoverflow.com/questions/30896343/how-to-install-gssapi-python-module



## 错误说明

### Possibly authentication failed [403]: Forbidden

命令:

```python
server.get_whoami()
```

详细信息:

```python
jenkins.JenkinsException: Error in request. Possibly authentication failed [403]: Forbidden
```

