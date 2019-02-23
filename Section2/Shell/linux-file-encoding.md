# Linux 文件编码

**查看文件编码**

1. 命令行使用 `file -i filename` 查看文件编码
2. 命令行使用 `vim` 打开文件，使用 `:set fileencoding` 查看

**转换文件编码**

`iconv`

**特殊场景说明**

查看文件编码为 `ISO-8859-1` 并且含有中文字符的文件

1. `vim -c "e ++enc=GBK" filename`

   或者配置 `~/.vimrc`（未验证）

   ```
   set encoding=utf-8
   set fileencoding=utf-8
   ```

2. 转换为 `GBK` 格式后使用 `vim` 正常打开查看

   `iconv -f GBK oldFilename -o newFilename`


## 更新说明

```
2019.02.24: 开始整理，增加编码ISO-8859-1的文件中中文字符显示异常的说明
```

