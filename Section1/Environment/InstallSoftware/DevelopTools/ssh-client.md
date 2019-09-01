# 1.2.1.2 ssh 客户端软件

1. XShell
2. FinalShell



## 第一部分 Xshell使用

Xshell可以在Windows界面下用来访问远端不同系统下的服务器，从而比较好的达到远程控制终端的目的。除此之外，其还有丰富的外观配色方案以及样式选择。

### 1 版本说明

#### 1.1 Xshell5

Xshell5在2018年开始已经不提供使用，打开提示：“要继续使用此程序，您必须应用最新的更新或使用新版本”，点击确定后，软件会退出，导致无法使用。

Xshell6官方免费版本使用时有最大标签页（4个）限制，且暂不存在破解版本，使用起来很不舒服。而网络上百度到的Xshell5破解版本基本都是无法使用的，浪费大量时间。

此处有可用的Xshell5破解版，下载地址：

- https://www.portablesoft.org/down/1985/
- https://portablesoft.ctfile.com/fs/763521-329513248
  - 压缩包解压密码: [www.portablesoft.org](http://www.portablesoft.org/)

> **注意**
>
> Xshell5在2017年出现了一次影响较大的安全漏洞问题（具体记不太清了，可百度），如果对安全方面有较强的要求，需要特别注意。据我所知，华为全公司及合作方所有员工，全面禁用xshell软件。

#### 1.2 Xshell6

> Xshell6存在商业版和免费版，XShell在商业环境使用下是需要买许可的，此处只介绍免费版。

Xshell6免费版，即 Home & school 版本，标签页限制最大数为4个。

Xshell6免费版下载地址链接：

- http://www.netsarang.com/download/free_license.html

### 2 使用说明

#### 2.1 字体选择



#### 2.2 配色方案

几款Xshell绝佳配色方案

- https://blog.csdn.net/hxspace/article/details/79851144
- https://blog.csdn.net/seekkevin/article/details/49662391
- https://www.jzfblog.com/detail/100

黑客帝国 blue.xcs


### 3 使用问题

#### 3.1 纯黑背景下无法找到鼠标

**现象**

鼠标经过纯黑背景的 `xshell` 窗口时，看不到光标，这样容易给人一种鼠标光标丢失的感觉，对于使用鼠标操作的用户来说，会造成一定的困扰和不方便。

**分析定性**

非xshell软件配置问题，而是windows7系统中关于鼠标光标默认方案中使用的“文本选择”项光标为纯黑色图标导致的。

**解决方案**

- 方案一

  设置 `C:\windows\Cursors\` 目录下的鼠标光标文件 `beam_*.cur` 

  进入win7下的“鼠标属性”设置界面，在“指针”页签中当前使用的“方案”下，“自定义”栏目中查找到“文本选择”项，点击“浏览”在对话框中选中“beam_r.cur”文件，最后点击“确定”即可。

  流程说明：

  ​		控制面板--> 鼠标属性 --> 指针 --> 文本选择 --> 浏览 --> beam_r.cur --> 打开 --> 应用 --> 确定

- 方案二

  控制面板--> 鼠标 --> 指针 --> 方案 --> 应用 --> 确定

### 4 同类产品

- secureCRT（收费）
- putty（多窗口，不支持标签）
- MobaXterm
- FinalShell
