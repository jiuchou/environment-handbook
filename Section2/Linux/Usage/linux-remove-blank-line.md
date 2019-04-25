# Linux 去除空行的几种方法

<!-- TOC -->

- [Linux 去除空行的几种方法](#linux-去除空行的几种方法)
    - [1 正文](#1-正文)
    - [更新说明](#更新说明)

<!-- /TOC -->

## 1 正文

删除文件或字符串中的空行（空格、制表符出现次数不确定），可以使用 `awk`、 `grep`、 `perl`、 `sed`、 `tr`

> LINUX下换行符是 `$`， windows 下换行符是 `^M$`。
>
> 以下内容主要针对linux场景，脚本中提前使用 `doc2unix` 命令将文件转换为 `unix` 格式

1.使用 `awk`

```bash
# NF代表当前行的字段数，空行的话字段数为0，被awk解释为假，因此不进行输出。
cat filename | awk NF
awk NF filename
# 推荐
cat filename | awk '!/^[[:blank:]]*$/{print $0}'
awk '!/^[[:blank:]]*$/{print $0}' filename

# 删除不含有空格和tab的空行
cat filename | awk '{if($0!="")print}'
cat filename | awk '{if(length!=0) print $0}'
```

2.使用 `grep`

```bash
# 不输出由空格或制表符出现次数不确定的行
grep -vE "^[[:blank:]]*$" filename
```

> 说明：[参考](https://www.jianshu.com/p/fc1f2c08f516?from=timeline&isappinstalled=0)
>
> 1.`grep` 是一个强大的文本搜索工具，其中选项 `-v` 代表反向匹配( 代表输出的是不匹配的行 )，选项 `-E` 代表使用扩展正则表达式。
>
> 2.`[:blank:]` 是 `POSIX` 字符集，匹配的是空格和制表符
>
> 3.`^`和 `$` 分别代表匹配文本的开头和结尾
>
> 4.`[ ]` 代表匹配中括号中的任意一个字符
>
> 5.`*` 代表其前面的字符出现0次或多次
>
> 如果文本中的空行不是由空白或者制表符造成的，而只是在编写文本时由于输入换行符造成的，那这条命令同样适用。虽然 `grep` 无法直接匹配换行符，但是可以通过 `grep -E "^$"` 实现匹配换行符，所以上面的命令可以过滤掉任意情况造成的空行。
>

3.使用 `perl`

```bash
# 将去除空行后的内容打印到屏幕
perl -n -e "print if /\S/" filename

# 直接去除文件中的空行
perl -i -n -e "print if /\S/" filename

# output file: filename.backup
# filename为去除空格的文件内容
# filename.backup为源文件内容
perl -i .backup -n -e "print if /\S/" filename
perl -n -e "print if /\S/" filename > filename.backup
```

4.使用`sed`

```bash
cat filename | sed '/^[[:blank:]]*$/d'
sed '/^[[:blank:]]*$/d' filename

# 错误写法, 无法匹配到纯空格字符的行
cat filename | sed '/^$/d'

# 错误写法, 无法匹配到纯table字符的行
cat filename | sed '/^ *$/d'
```

5.使用`tr`

```bash
# 删除无空格、制表符的空行
cat filename | tr -s '\n'
```

## 更新说明

```
2019.02.23: 整理初稿，功能验证通过。
```



