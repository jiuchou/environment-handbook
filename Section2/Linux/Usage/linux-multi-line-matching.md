# Linux Shell多行匹配


假设文件 `filename` 内容如下：
```
START
    content
    static
    dynamic
END
```

## sed 多行模式匹配

* 参考
  * [sed中的多行匹配](https://www.cnblogs.com/2myroad/p/3912432.html)

    > 核心：sed中的多行匹配，可以用N，N的意思是把下一行写入保持空间。
    >
    > 解读：比较凌乱，其中单引号消失问题是因为 `sed -i` 后使用了单引号，将注释行的单引号转义即可。

  * [sed匹配多行并替换其中的内容](https://www.cnblogs.com/yangxiaochu/p/7602884.html)

    > `sed -i '/START/{:a; n; s/content/target/g; /END/!ba}' filename`
    >
    > ​	n 读取下一行
    >
    > ​	:a 设定跳转标签a
    >
    > ​		/END/!ba  若当前行匹配不上END，则跳转到标签a处继续执行，构成一个循环。若匹配到END，则退出循环，sed重新对读入的每行匹配START。

* 来源（待整理）

  * [SED多行模式空间](https://blog.csdn.net/imzoer/article/details/8740673)

普通情况下，使用sed都是单行模式，即 `sed` 每次处理一个行。

但是 `sed` 是允许一次处理多行的，这就是所谓的多行模式空间。

多行模式空间命令有（N、D、P），他们分别对应单行模式空间（n、d、p），分别是他们的多行形式。

比如，`d` 每次删除一行，而 `D` 每次删除多行模式空间中的“一行”，其实就是一个记录。

> 例如
>
> ​	使用N来创建多行模式空间，将loves\ncc直接替换成loves cc，然后在sed命令的末尾使用\来表示换行。则得到了上面的结果。
>
> ```
> ubuntu@ubuntu:~$ cat data 
> naughty loves
> cc,and cc loves naughty.
> they are very happy!
> 
> ubuntu@ubuntu:~$ cat d
> N
> s/loves\ncc/loves cc\
> /
> 
> ubuntu@ubuntu:~$ sed -f d data 
> naughty loves cc
> ,and cc loves naughty.
> they are very happy!
> ```
>
> sed命令中的loves c\，反斜杠是换行之意。如果没有它，那么两行将成为一行
>
> ```
> ubuntu@ubuntu:~$ cat d
> N
> s/loves\ncc/loves cc\ /
> 
> ubuntu@ubuntu:~$ sed -f d data 
> naughty loves cc ,and cc loves naughty.
> they are very happy!
> ```
>
> 



**替换多行内容（待替换的字符串占位超过1行）**

> 其中，
>
> ​	:a 设定跳转标签a
>
> ​	N 把下一行写入保持空间
>
> ​	n 读取下一行
>
> ​	!ba 如果未匹配上，跳转到标签a处

```bash
sed -i ':a; $!{N;ba}; s/static\n\ \ \ \ dynamic/target/g' filename
# 或(可以限定开始结束行)
sed -i '/START/{:a; n; s/content/target/g; /END/!ba}' filename
```

**相关1：替换所有具备相同字符串的行中的字符串**

```bash
# 一般方法
sed -i "s/content/target/g" filename
# 使用多行匹配的模式，参考 [参考 - sed匹配多行并替换其中的内容]
sed -i '/START/{:a; n; s/content/target/g; /END/!ba}' filename
```

**相关2：常用内容**

```bash
# 替换多行具备相同字符串的内容
sed -i "s/content/target/g" filename
# 删除多行
sed -i '2,3d' filename
```

**相关3：删除匹配行的上一行和下一行**

固定的字符串

```bash
sed -i -e '/string/{n;d}' -e '$!N;/\n.*string/!P;D' file
```

使用变量替代字符串

```bash
# 变量指定匹配字符串
AA=string
sed -i -e '/'"$AA"'$/{n;d}' -e '$!N;/\n.*'"$AA"'$/!P;D' file
```

## grep 多行匹配

* 来源（待整理）

  * [grep 多行 正则匹配](https://www.cnblogs.com/xuxm2007/p/9180604.html)

```bash
grep -Pzo "static\n\ \ \ \ dynamic" filename
```

grep查找关键字所在行以及其上下几行（`-r`和`-B`组合使用才可以）

```bash
# 打印匹配行的前后5行
grep -r -5 'parttern' filename
grep -r -C 5 'parttern' filename
# 打印匹配行的后5行
grep -r -A 5 'parttern' filename
# 打印匹配行的前5行
grep -r -B 5 'parttern' filename
```



## awk 多行匹配

http://hte.sourceforge.net/doxygenized-0.8.0pre1/files.html
https://blog.csdn.net/chief1985/article/details/1929170
http://ftp.gnu.org/gnu/glibc/



* 待整理

  * [awk处理案例九--输出取余某特定几行](https://www.cnblogs.com/lottu/p/3335891.html)