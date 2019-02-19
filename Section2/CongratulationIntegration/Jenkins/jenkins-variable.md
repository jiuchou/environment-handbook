# Jenkins 获取字符串变量

> 场景说明：
>
> Jenkins工程中配置的**构建前参数**在使用时含有特殊字符（如"$"），使用Execute Shell插件获取时会进行转义，导致结果不符合预期。

在工程配置中配置`Execute system Groovy script`，内容如下：

> 说明：
>
> ​	此groovy脚本将**构建前参数**`cmd`写入cmdFile文件中，后续如果在Shell中使用可通过读取cmdFile文件获取期望内容。
>
> 注意：
>
> ​	必须使用系统groovy脚本，否则无法调用Jenkins API。

```groovy
import hudson.model.*

String workspace = "/var/jenkins_home/workspace/projectName"
String cmdFile = workspace + "/cmdFile"

def resolver = build.buildVariableResolver
String buildCmd = resolver.resolve("cmd")

new File(cmdFile).withPrintWriter { printWriter ->
	printWriter.println(cmd)
}
```

