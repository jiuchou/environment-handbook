# bat批处理文件

### 1 Windows代理

#### 1.1 Windows系统命令行操作代理

**查看proxy**

```bat
netsh winhttp show proxy
```

**设置proxy** 

* `Setting a proxy for Windows using the command-line`，`bypass-list` 的参数是不走代理地址

```
netsh winhttp set proxy proxy-server="socks=localhost:9090" bypass-list="localhost"
```

**删除proxy**

```bat
netsh winhttp reset proxy
```

### 1.2 浏览器配置代理

**Google** 进入`设置 - 更多 - 系统 - 打开代理设置 - 局域网设置`，然后配置代理

## 2 bat批处理文件

### 2.1 bat/cmd常用命令

**1. 获取当前文件的绝对路径**

- 命令行 `dir /b /s /a-d filename`
- 脚本 `echo %~f0`

**2. 获取当前文件所在目录的绝对路径**

- 命令行

  `for /f "delims=" %i in ('dir /b /s /a-d filename') do (set current_path=%i)
  set current_path=%current_path:~0,-11%
  echo %current_path%`

- 脚本 `echo %~dp0`

### 2.2 bat/cmd将命令执行的结果赋值给变量

> * 参考
>   * [windows下如何实现类似awk获取文件字段值功能](https://jingyan.baidu.com/article/0320e2c10ca7c31b87507bce.html)
>
> 
>
> ​	skip=1 丢弃1行
>
> ​	tokens=2 第2列
>
> ​	“delims”分隔符的值，使用默认分隔符——“空格和TAB键”

**1. 直接赋值**

* 命令行

```
for /f "tokens=2 delims= " %i in ('svn info svn_path^|findstr Revision') do (set REVISION=%i)
echo %REVISION%

if %REV% == HEAD (for /f "tokens=2 delims= " %i in ('svn info svn_path^|findstr Revision') do (set REVISION=%i))  else (set SVN_REVISION=%REV%)
```

* bat/cmd脚本

```
for /f "tokens=2 delims= " %%i in ('svn info svn_path^|findstr Revision') do (set REVISION=%%i)
echo %REVISION%
```

**2. 写入到文件后处理**

* 命令行

```
svn info svn_path | findstr Revision > revision.txt
for /f "tokens=2 delims= " %i in (revision.txt) do (set REVISION=%i)
echo %REVISION%
```

* bat/cmd脚本

```
svn info svn_path | findstr Revision > revision.txt
for /f "tokens=2 delims= " %%i in (revision.txt) do (set REVISION=%%i)
echo %REVISION%
```

