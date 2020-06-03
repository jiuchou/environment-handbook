# Linux Shell

**社区教程**

* [ChinaUnix: Shell基础二十篇](http://bbs.chinaunix.net/thread-452942-1-1.html)



**shell、child shell、subshell**

* [SHLVL 和 BASH_SUBSHELL 两个变量的区别](https://www.cnblogs.com/ziyunfei/p/4803832.html)



查找文件中所有不以AB或者XY开头的行

```bash
cat filename | grep -v "^[AX][BY]"
```


获取 svn 版本号（兼容svn1.6/svn1.9）

```bash
# SVN 版本信息使用提交的 commit 信息
SVN_REVISION=$(svn log -l 1 ${URL} | awk "NR==2" | awk '\''{print $1}'\'' | sed "s/r//g")
```

* timewait: http://www.httpclient.cn/archives/98.html


# 基础知识

## 常用

### 脚本参数

```bash
$# ：传入脚本的参数个数
$0: 脚本自身的名称　
$1: 传入脚本的第一个参数
$2: 传入脚本的第二个参数
$@: 传入脚本的所有参数
$*：传入脚本的所有参数
$$: 脚本执行的进程id
$?: 上一条命令执行后的状态，结果为0表示执行正常，结果为1表示执行异常
```

其中 `$@` 与 `$*` 正常情况下一样，当在脚本中将 `$*` 加上双引号作为 `"$*"` 引用时，此时将输入的所有参数当做一个整体字符串对待。比如输入参数有 `a b c` 三个参数，则 `"$*"` 表示 `"a b c"` 一个字符串。

测试程序如下：

```bash
# 在使用循环时，建议使用${name[@]}方式
name=(jack tony kevin)
for name in "${names[*]}"; do echo $name; done
for name in "${names[@]}"; do echo $name; done
```

### 变量

#### 变量说明

- 特殊变量：linux系统自带变量

  ```bash
  HOME: 用户home目录
  SECONDS: shell被invoke的时间间隔
  BASH: 当前使用的bash的路径
  BASH_VERSION: shell的版本
  BASH_VERSINFO: 当前使用shell的主版本信息。例如我的版本是3
  PWD: 当前路径
  OLDPWD: 上次cd前的路径
  ```

- 常规变量：在本文件中有效，定义方式为 `name="jiuchou"`

- 全局变量：跨文件生效，定义方式为 `export name="jiuchou"`

  **main.sh**

  ```bash
  #!/bin/bash
  
  export name="jiuchou"
  age=20
  
  echo "[main.sh] name is $name"
  echo "[main.sh] age is $age"
  
  bash name.sh
  ```

  **name.sh**

  ```bash
  #!/bin/bash
  
  echo "[name.sh] name is $name"
  echo "[name.sh] age is $age"
  ```

  **测试结果**

  ```bash
  root@ubuntu:/home/jiuchou# bash main.sh 
  [main.sh] name is jiuchou
  [main.sh] age is 20
  [name.sh] name is jiuchou
  [name.sh] age is 
  ```

- 局部变量：在所属的代码块中有效，定义方式为 `local name="jiuchou"`

  **local.sh**

  ```bash
  #!/bin/bash
  
  test_local() {
      name="jiuchou"
      local age=20
  
      echo $name
      echo $age
      echo "function test_local ending..."
  }
  
  test_local
  echo $name
  echo $age
  echo "file ending..."
  ```

  **测试结果**

```bash
  root@ubuntu:/home/jiuchou# bash local.sh 
  jiuchou
  20
  function test_local ending...
  jiuchou
  
  file ending...
```

#### 脚本调用说明

> source 文件和 bash 文件的区别

- 使用 `source` 或者 `.`
- 使用可执行文件模式（待考证）

### 函数Functions

使用function的两个原因

- function存放在系统的内存，所以调用的使用效率更高
- 更好的组织大规模bash，使之模块化

定义function的方式

- 使用function关键字

  ```bash
  # 此种方式可省略函数名后的括号
  function function_name() { 
      shell commands 
  } 
  ```

- 省略function关键字

  ```bash
  function_name() {
  	shell commands
  }
  ```

删除函数定义

```bash
unset -f function_name
```

查看已定义的函数

```bash
# 查看函数详细信息
declare -f 

# 查看函数名
declare -F
```

### 重名命令

**重名命令的优先级**

1. Aliases
2. 关键字，例如function，if，for
3. Functions
4. Built-ins，例如cd，type
5. 在命令搜索路径PATH下的脚本和可执行文件

**type**

如果我们需要查看所使用命令属于哪种，用**type name**，例如aa是个alias（表示pwd），同样我们也定义了它作为一个function，根据优先级别，aa优先作为alias，type aa，我们可以得到aa is aliased to ‘pwd’，可以用**type –a(或者-all) name** ，来查看aa代表的所有含义。

- **type –t name** 查看类型，将返回alias | keyword | function | builtin | file
- **type –p name** 用于查看file的路径，如果类型不是file将没有返回
- **type –P name** 则强制查找file的路径。例如一个重名，它是一个alias，也是一个在PATH目录下的可执行文件。-p则没有返回，-P这返回文件的绝对路径。

## 冷门

### 子shell

- https://blog.csdn.net/sosodream/article/details/5683515
- 

### 退出程序

#### exit不退出程序

- 原理解释： https://blog.csdn.net/godbreak/article/details/47117617

bash对于带有管道的那一行命令和没有管道的情况是不同的，带有管道的命令将先fork后执行。此时在function中的exit事实上是结束了子进程。

```bash
function exit_test()
{
    echo "function exit_test"
    exit
}

echo $$
exit_test | tee
echo 'why get here'
```

### 非常见区别

#### $() 和 ``的区别

- $() 移植性不如 ``，不是所有的shell都能使用
- 在多层嵌套模式下，`` 需要转义进行额外的跳脱( \ )处理，而 $( ) 则比较直观

```bash
command1 `command2 \`command3\` `
command1 $(command2 $(command3))
```

#### 特殊符号

- https://blog.csdn.net/qq_38572383/article/details/80911601

## 教程

- http://c.biancheng.net/linux_tutorial/50/
- http://c.biancheng.net/shell/

## Geek

### 控制台显示

```bash
# 显示全局路径及颜色标识
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
# 显示全局路径
PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
```

### PS4

# SVN

## svn的客户端凭证缓存

- https://blog.csdn.net/wangjianno2/article/details/51749410