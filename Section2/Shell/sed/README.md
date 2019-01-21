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

