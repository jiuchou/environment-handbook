# set -o errexit, set -o pipefail与set -o nounset

[TOC]

## 1. 基本介绍

默认情况下，Bash脚本会忽略许多执行错误的内容。在脚本中添加以下几种设置，可以增强代码的可靠性和健壮性。

以下内容默认关闭，如果设置后需要手动关闭，将“-”替换成“+”即可。

### 1.1 set -o errexit(等价于 set -e)

* 建议使用

linux 介绍:

 `"Exit immediately if a simple command exits with a non-zero status."`

也就是说，在"set -e"之后出现的代码，一旦出现了返回值非零，整个脚本就会立即退出。

使用本设置，可以将我们从检查错误中解放出来。不过带来方便的同时，也无法再使用`$?`来获取命令执行状态了，因为bash无法获得任何非0的返回值。

以下方式无法继续使用：

```bash
command    
if [ $? -ne 0]; then
	echo "command failed"
	exit 1
fi
```

替代方案如下：

```bash
command || { echo "command failed"; exit 1; }    
```

或者使用：

```bash
if ! command; then 
	echo "command failed"
	exit 1
fi  
```

如果必须使用返回非0值的命令，或者对返回值并不感兴趣的话，可以使用`command || true`，或者有一段很长的代码，可以暂时关闭错误检查功能，建议谨慎使用。

### 1.2 set -o pipefail

* 建议使用(易出错，慎重)

linux 介绍:

 `"If set, the return value of a pipeline is the value of the last (rightmost) command to exit with a  non-zero  status,or zero if all commands in the pipeline exit successfully.  This option is disabled by default."`

也就是说设置了这个选项以后，包含管道命令的语句的返回值，会变成最后一个返回非零的管道命令的返回值。

### 1.3 set -o nounset(等价于 set -u)

* 建议使用(易出错，慎重)

linux介绍:

`暂时缺少`

执行脚本的时候，如果遇到不存在的变量，Bash 默认忽略它。

如果想改变这种行为，设置`set -o nounset`，遇到不存在的变量就会报错，并停止执行。

## 2. 区别

`set -o errexit`: 主要针对程序返回值是否为零

`set -o pipefail`：主要针对每个管道返回值是否为零

`set -o nounset`：主要针对变量是否提前已定义。

如果在文件中同时定义以上三个设置，检查较为严格，一般使用`set -o pipefail`或`set -o nounset`的同时，也会使用`set -o errexit`配置。

## 3. 测试程序

1.测试`set -o errexit`

```bash
#!/bin/bash
set -o errexit

# 错误的内容
test_exit
echo "Test End"
```

2.测试`set -o pipefail`

```bash
#!/bin/bash
set -o pipefail

echo "test" > testFile1
echo "" > testFile2
testNumber2=$(grep -r "test" testFile2 | wc -l)
testNumber1=$(grep -r "test" testFile1 | wc -l)
echo ${testNumber1}
echo ${testNumber2}
```

3.测试`set -o nounset`

```bash
#!/bin/bash
set -o nounset

echo $a
echo "Test End"
```



## 参考

* [写出健壮的Bash脚本](https://www.csdn.net/article/2012-03-19/313229)

