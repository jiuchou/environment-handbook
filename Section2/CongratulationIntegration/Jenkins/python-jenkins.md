# Python 使用Jenkins Rest API 之 python-jenkins

* 说明
  * [Python-Jenkins 官网](https://pypi.python.org/pypi/python-jenkins/)
  * [Python-Jenkins 官方文档](https://python-jenkins.readthedocs.io/en/latest/api.html)

## 1 基础说明

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

## 2 错误说明

### 2.1 Possibly authentication failed [403]: Forbidden

版本信息

```
Jenkins: 2.150.1
python-jenkins: 1.4.0
说明：通过测试，python-jenkins==1.4.0同时兼容Jenkins1.6xx版本
```

错误信息：

```python
>>> server.get_whoami()
xxxxxxxxxx jenkins.JenkinsException: Error in request. Possibly authentication failed [403]: Forbidden
```

定位过程：

```
可能原因：
1.用户鉴权失败
用户名和api-token确认无误，权限设置正常
2.CSRF（防止跨站点请求伪造）机制开启
Jenkins2.x版本默认开启CSRF机制。通过安全设置页，关闭CSRF机制，使用，接口调用依然失败。非CSRF机制设置问题。
> 扩展：https://wiki.jenkins.io/display/JENKINS/CSRF+Protection
3.代理
通过curl命令调用API接口失败，关闭机器代理，测试通过。
```

原因及解决方案：

```python
机器设置了代理，执行调用api接口时，请求经由代理转发出现错误。
Jenkins2.x版本默认开启CSRF机制，python-jenkins==1.4.0版本能够自动
关闭代理，问题解决。
```

### 2.2 调用get_version()提示Error communicating with server

https://www.jianshu.com/p/68dd714e6c31

## 3 扩展

### 3.1 kerberos

https://pypi.org/project/kerberos/#description