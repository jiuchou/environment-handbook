## Shell去除空行的几种方法

https://www.jianshu.com/p/fc1f2c08f516?from=timeline&isappinstalled=0

> LINUX下换行符是 $
>
> windows 下换行符是^M$
>
> 将文件转换为unix格式`doc2unix`
>
> 以下内容主要针对linux场景

* 用tr命令

```bash
# 若空行均由'\n'造成
cat filename | tr -s '\n'
```

* 用sed命令

```bash
sed '/^[[:blank:]]*$/d' filename

# 错误写法, 无法匹配到纯空格字符的行
cat filename | sed '/^$/d'

# 错误写法, 无法匹配到纯table字符的行
cat filename | sed '/^ *$/d'
```

* 用awk命令

```bash
cat filename | awk '{if($0!="")print}'
cat filename | awk '{if(length!=0) print $0}'

# 删除含有空格和tab的空行
# NF代表当前行的字段数，空行的话字段数为0,被awk解释为假，因此不进行输出。
awk NF filename
cat filename | awk NF

# 推荐
awk '!/^[[:blank:]]*$/{print $0}' filename
```

* 用grep命令

```bash
# [:blank:] 是POSIX字符集，匹配的是空格和制表符
grep -vE "^[[:blank:]]*$" filename
```

> 首先grep是一个强大的文本搜索工具，其中选项 -v 代表反向匹配( 代表输出的是不匹配的行 )，选项 -E 代表使用扩展正则表达式。匹配模式部分中 [:blank:] 是POSIX字符集，匹配的是空格和制表符，^和 $ 分别代表匹配文本的开头和结尾，[ ] 代表匹配中括号中的任意一个字符，* 代表其前面的字符出现0次或多次，所以将这条命令连起来看就是不输出那些由空格或制表符开头并且空格和制表符出现次数不确定的行，需要注意的是如果文本中的空行不是由空白或者制表符造成的，而只是在编写文本时由于输入换行符造成的，那这条命令同样适用。grep虽然无法直接匹配换行符，但是可以通过grep -E "^$"实现匹配换行符，所以现在回过头来看上面的那条命令是不是发现了它可以过滤掉文本中不管是由什么原因造成的空行。

* 用perl命令
```bash
# output file: filename.backup
# filename为去除空格的文件内容
# filename.backup为源文件内容
perl -i.backup -n -e "print if /\S/" filename

# 直接去除文件中的空行
perl -i -n -e "print if /\S/" filename

# 将去除空行后的内容打印到屏幕
perl -n -e "print if /\S/" filename
```

## Linux Shell 中实现字符串切割的几种方法

https://blog.csdn.net/u010003835/article/details/80750003

awk 在makefile中无法使用，可使用cut
awk '{print $2}'
cut -d " " -f2

## Shell脚本8种字符串截取方法总结

https://www.jb51.net/article/56563.htm

```bash
# 只替换一个
text=${text/ /-}
# 全部替换
text=${text// /-}
```

cut
https://www.cnblogs.com/Hobbies/articles/4527447.html
