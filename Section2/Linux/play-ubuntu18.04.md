# 玩转Ubuntu18.04

## 1 Install Ubuntu System

## 2 Setting

### 2.1 笔记本设置合上盖子时不关机

`vim /etc/systemd/logind.conf`

```bash
# 设置
HandleLidSwitch=ignore
# 重启服务
service systemd-logind restart
```

### 2.2 设置桌面

Ubuntu18.04 默认

#### 2.2.1 设置桌面主题

- https://blog.csdn.net/caizi001/article/details/39494293
- https://www.jianshu.com/p/f83833b28d64

#### 2.2.2 设置桌面背景

setting - background - background



- https://blog.csdn.net/sinat_21533627/article/details/88322603
- 下雪特效：https://www.imooc.com/article/272574

#### 2.2.3 设置终端背景

- 透明度设置
- 颜色设置
- 设置终端配色和vim配色
  - https://baijiahao.baidu.com/s?id=1592697072023097071&wfr=spider&for=pc

#### 2.2.4 设置桌面top bar

```bash
apt install gnome-tweaks
```

#### 2.2.5 隐藏桌面回收站

### 2.3 默认功能设置

#### 2.3.1 设置默认语言

设置 - 区域和语言 - 语言（选择中文或英文）

#### 2.3.2 设置截图

设置 - 设备 - 键盘 - 截图

* 复制截图到剪贴板：Ctrl+Alt+A
* 将截图保存到目录：Ctrl+Shift+A

### 2.4 安装搜狗输入法

- https://blog.csdn.net/fenglllle/article/details/84932988

- https://www.cnblogs.com/wenchaoz/p/8981834.html

> 参考
>
> * https://blog.csdn.net/lupengCSDN/article/details/80279177

1. 卸载ibus

```bash
# 卸载ibus
apt-get remove ibus
# 清除ibus配置
apt-get purge ibus
# 卸载顶部面板任务栏上的键盘指示
apt-get remove indicator-keyboard
```

2. 安装fcitx框架

```bash
# 安装fcitx输入法框架
apt install fcitx
# 切换为 Fcitx输入法
im-config -n fcitx
# 配置完成最好重启系统,确保可以生效
shutdown -r now
```

3. 安装搜狗输入法

下载： https://pinyin.sogou.com/linux/?r=pinyin

```bash
dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
```

4. 配置输入法

* 设置 - 区域和语言 - 管理已安装语言 - 键盘输入法系统（选择fcitx，并应用到整个系统）

* 关机重启

* 点击右上角输入法按钮 - 配置当前输入法（添加搜狗输入法到输入法列表中）

## 3 Software

### 3.1 Typora

- 详细介绍：https://github.com/jiuchou/git-handbook/blob/master/gitbook-handbook/Chapter3/section3.1/Typora.md

Typora是一款由Abner Lee开发的轻量级Markdown编辑器，适用于OS X、Windows和Linux三种操作系统，是一款免费软件。

#### 3.1.1 Install

官网下载安装地址：https://typora.io/#linux

```bash
# or run:
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update
# install typora
sudo apt-get install typora
```

#### 3.1.2 Open With

- 方法1：通过应用图标打开
- 方法2：在终端输入typora命令打开

### 3.2 VSCode

editor.fontFamily 设置

### 3.3 百度云

- https://www.jianshu.com/p/00b95ba24010

## 4 娱乐

### 4.1 网易云音乐

#### 4.1.1 Install



#### 4.1.2 Open With

* 方法1：通过应用图标打开
* 方法2：终端输入netease-cloud-music命令打开

### 4.2 WeChat

#### 4.2.1 Install

下载地址：https://github.com/geeeeeeeeek/electronic-wechat/releases

```bash
wget 
```



## 5 桌面程序开发

## 6 可参考

https://jingyan.baidu.com/article/a501d80c380c86ec630f5e1d.html

https://www.imooc.com/learn/1148

必备的linux桌面应用：https://www.imooc.com/article/258709

矛盾文学奖：http://www.wenming.cn/specials/hot/wmkd/201908/t20190816_5223668.shtml



GTK

https://blog.csdn.net/abel__2008/article/details/2980496

https://python-gtk-3-tutorial.readthedocs.io/en/latest/basics.html

https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Dialog.html#Gtk.Dialog



## 7 扩展

https://www.linuxidc.com/Linux/2018-06/152993.htm

https://zhuanlan.zhihu.com/p/79300868

https://extensions.gnome.org/extension/1108/add-username-to-top-panel/

https://zhuanlan.zhihu.com/p/72336639

https://linuxhint.com/100_best_ubuntu_apps/	



https://www.zhihu.com/question/47514122



# Linux下发送微信消息

https://www.jianshu.com/p/c20320ff3764?utm_campaign=

