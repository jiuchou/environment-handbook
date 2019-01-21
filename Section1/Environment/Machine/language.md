# 1.1.2.语言显示


## Windows平台中文乱码
### 1.临时解决方案

打开cmd命令行，执行如下命令

```bash
CHCP 65001
```
说明: CHCP是一个计算机指令，能够显示或设置活动代码页编号。

| 代码页 | 描述              |
| ------ | ----------------- |
| 65001  | UTF-8代码页       |
| 950    | 繁体中文          |
| 936    | 简体中文默认的GBK |
| 437    | MS-DOS 美国英语   |

### 2.永久解决方案
#### 2.1 方法一
在运行中通过regedit进入注册表
找到HKEY_CURRENT_USER\Console\%SystemRoot%_system32_cmd.exe

新建一个 DWORD（32位值）,命名为CodePage，值设为65001 
已有CodePage的话，修改它，改为十进制，65001

#### 2.2 方法二
新建一个cmd.reg，内容如下。保存之后，双击运行cmd.reg即可。

```bash
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Console\%SystemRoot%_system32_cmd.exe]
"CodePage"=dword:0000fde9
"FontFamily"=dword:00000036
"FontWeight"=dword:00000190
"FaceName"="Consolas"
"ScreenBufferSize"=dword:232900d2
"WindowSize"=dword:002b00d2
```

