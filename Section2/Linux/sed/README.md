# sed

* [linux命令总结sed命令详解](https://www.cnblogs.com/ginvip/p/6376049.html)

1.删除

```bash
# 删除指定行到某字段的内容
line=$(grep -n "content" fileName | cut -d ":" -f1)
if [[ "${line}" != "" ]]; then
	sed -i $(( line - 1)),"/content/d" fileName
fi

# 获取文件中某一行开始到文件结束的内容
sed -n "$(expr ${line} + 1),/\$p/p" fileName

# 删除指定行之间的内容
line=5
sed -i "1, ${line} d" fileName
```

2.修改

在包含某字符串中添加指定字符串string

* 如果指定字符串string不包含 `/`
    * 添加字符串到行首 `sed -i "/test/ s/^/${string}" filename`
    * 添加字符串到行尾 `sed -i "/test/ s/$/${string}" filename`

* 如果指定字符串string包含 `/`
    * 添加字符串到行首 `sed -i "s#^.*test#${string}&#g" filename`
    * 添加字符串到行尾 `sed -i "s#^.*test.*#&${string}#g" filename`





在文件指定位置后插入另一个文件的内容

```bash
sed -i '/naughty_position/r filename' file
```

在文件指定行后插入另一个文件的内容

```bash
sed -i '2r filename' file
```

