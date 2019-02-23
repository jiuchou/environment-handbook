# Linux 字符串

## 1 字符串替换

### 1.1 利用 shell 中变量的字符串替换

```bash
# 用 text 来替换 string 变量中第一个匹配到的 pattern
string=${string/pattern/text}
# 用 string 来替换 text 变量中所有匹配到的 pattern
string=${string//pattern/text}
```

### 1.2 设置分隔符，通过 IFS 变量

* 来自： [Shell中的IFS解惑](https://blog.csdn.net/whuslei/article/details/7187639)

#### 1.2.1 IFS 介绍

Shell 脚本中有个变量叫 IFS(Internal Field Seprator) ，内部域分隔符。官方介绍：

`The shell uses the value stored in IFS, which is the space, tab, and newline characters by default, to delimit words for the read and set commands, when parsing output from command substitution, and when performing variable substitution.`

IFS 是一种 set 变量（参考 [Linux 环境变量](../linux-environment-variable.md)），当 shell 处理"命令替换"和"参数替换"时，shell 根据 IFS 的值，默认是 space, tab, newline 来拆解读入的变量，然后对特殊字符进行处理，最后重新组合赋值给该变量。

#### 1.2.2 IFS 使用

```bash
#!/bin/bash
IFS_old=$IFS      #将原IFS值保存，以便用完后恢复
IFS=$’\n’        #更改IFS值为$’\n’ ，注意，以回车做为分隔符，IFS必须为：$’\n’
for i in $((cat pwd.txt)) #pwd.txt 来自这个命令：cat /etc/passwd >pwd.txt
do
    echo $i
done
IFS=$IFS_old      #恢复原IFS值
```

### 1.3 使用 Linux 命令

常用的可实现字符串操作的命令，如 `sed`、 `tr` 等。

命令用法（待补充）：

1. [sed]()
2. [tr]()

## 2 字符串截取

* 来自：[Shell脚本8种字符串截取方法总结](https://www.jb51.net/article/56563.htm)

**1. # 号截取，删除左边字符，保留右边字符。**

复制代码代码如下:

echo ${var#*//}

其中 var 是变量名，# 号是运算符，*// 表示从左边开始删除第一个 // 号及左边的所有字符
即删除 http://
结果是 ：www.aaa.com/123.htm

**2. ## 号截取，删除左边字符，保留右边字符。**

复制代码代码如下:

echo ${var##*/}

\##*/ 表示从左边开始删除最后（最右边）一个 / 号及左边的所有字符
即删除 http://www.aaa.com/

结果是 123.htm

**3. %号截取，删除右边字符，保留左边字符**

复制代码代码如下:

echo ${var%/*}

%/* 表示从右边开始，删除第一个 / 号及右边的字符

结果是：http://www.aaa.com

**4. %% 号截取，删除右边字符，保留左边字符**

复制代码代码如下:

echo ${var%%/*}

%%/* 表示从右边开始，删除最后（最左边）一个 / 号及右边的字符
结果是：http:

**5. 从左边第几个字符开始，及字符的个数**

复制代码代码如下:

echo ${var:0:5}

其中的 0 表示左边第一个字符开始，5 表示字符的总个数。
结果是：http:

**6. 从左边第几个字符开始，一直到结束。**

复制代码代码如下:

echo ${var:7}

其中的 7 表示左边第8个字符开始，一直到结束。
结果是 ：www.aaa.com/123.htm

**7. 从右边第几个字符开始，及字符的个数**

复制代码代码如下:

echo ${var:0-7:3}

其中的 0-7 表示右边算起第七个字符开始，3 表示字符的个数。
结果是：123

**8. 从右边第几个字符开始，一直到结束。**

复制代码代码如下:

echo ${var:0-7}

表示从右边第七个字符开始，一直到结束。
结果是：123.htm

注：（左边的第一个字符是用 0 表示，右边的第一个字符用 0-1 表示）

## 3 其他字符串操作

### 3.1 获取字符串指定位置的内容

**1 使用变量方式**

```shell
# 获取字符串 string 的长度
length=${#string}

# 获取 string 中 position 位置之后的字符
# 例： string1=${string:3}
string1=${string:position}

# 获取 string 中 position 位置之后的 length 个字符
# 例： string1=${string:3:4}
string1=${string:position:length} 
```

**2 使用 Linux 命令**

> 注意：
>
> 在 Makefile 中 awk 无法使用，cut 可以使用

**2.1 awk**

命令格式： `awk -F '' '{print $1}'`

**2.2 cut**

* [linux每日一命令--cut](https://www.cnblogs.com/Hobbies/articles/4527447.html)

命令格式： `cut -d '' -f2`



## 更新说明

```
2019.02.23: 完成基本内容，包含Linux字符串替换、截取、读取等
```

