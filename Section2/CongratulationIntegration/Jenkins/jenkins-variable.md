# Jenkins 获取字符串变量

## 1 使用Shell

在工程配置中的**构建步骤**中配置 `Execute Shell`，直接在脚本中使用取值符号（`$`）获取变量的值。

## 2 使用System Groovy script

- 官方文档:
  - [Parameterized System Groovy script](https://wiki.jenkins.io/display/JENKINS/Parameterized+System+Groovy+script)

在工程配置中的**构建步骤**中配置 `Execute system Groovy script`，内容如下：

> 说明：
>
> ​	此groovy脚本将**构建前参数**`cmd`写入cmdFile文件中，后续如果在Shell中使用可通过读取cmdFile文件获取期望内容。
>
> 注意：
>
> ​	必须使用系统groovy脚本，否则无法调用Jenkins API。

```groovy
import hudson.model.*

String workspace = Jenkins.instance.getJob("jobName").lastBuild.workspace.toString()
String cmdFile = workspace + "/cmdFile"

def resolver = build.buildVariableResolver
String buildCmd = resolver.resolve("cmd")

new File(cmdFile).withPrintWriter { printWriter ->
	printWriter.println(cmd)
}
```

## 3 使用Python script

在工程配置中的**构建步骤**中配置 `Execute Python script`，内容如下：

```python
import os

# workspace = os.getenv('WORKSPACE')
workspace = os.environ['WORKSPACE']
cmdFile = workspace + "/cmdFile"
cmd = os.environ['cmd']
with open(cmdFile, 'w') as f:
    f.write(cmd)
```

## 4 场景说明

* 方法1： Jenkins工程中配置的**构建前参数**在使用时含有特殊字符（如"$"），使用 `Execute Shell` 获取时会进行转义，导致结果不符合预期。
* 方法2： 获取到的文件存放在 `jenkins master` 上，在构建节点与服务器分离的场景下不适用。
* 方法3： `Execute Python script` 需要安装 `Python Plugin`，默认安装Jenkins不包含此选项。
