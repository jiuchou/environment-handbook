# 07 Linux 软件管理

## 1  简介

与windows安装各种应用程序相似，在linux下也可以安装各种需要的应用程序，通常称为软件包。

大多数包系统都是围绕包文件的集合构建的。包文件通常是一个存档文件，它包含已编译的二进制文件和软件的其他资源，以及安装脚本。包文件同时也包含有价值的元数据，包括它们的依赖项，以及安装和运行它们所需的其他包的列表。

目前，在Linux系统下常见的软件包格式主要有：RPM包、TAR包、bz2包、gz包、deb包、sh结尾的文件、src源代码包、bin文件。

Linux安装软件包主要有以下几种方式：

* 软件源安装
* 软件包安装
* 源码安装
* 二进制安装

虽然这些包管理系统的功能和优点大致相同，但打包格式和工具却因平台而异，以下针对几种软件安装方式及主流的Linux发行版本进行进一步说明。

| 操作系统 | 格式          | 工具                                  |
| -------- | ------------- | ------------------------------------- |
| Debian   | `.deb`        | `apt`, `apt-cache`, `apt-get`, `dpkg` |
| Ubuntu   | `.deb`        | `apt`, `apt-cache`, `apt-get`, `dpkg` |
| CentOS   | `.rpm`        | `yum`                                 |
| Fedora   | `.rpm`        | `dnf`                                 |
| FreeBSD  | Ports, `.txz` | `make`, `pkg`                         |
| openSUSE | `.rpm`        | `zypper`                              |

另外对于比较复杂的和大型的软件集的安装，不同的发行版本也都有相应的解决方案：

* openSUSE：Yast 和 zypper 都提供了软件样式集(patterns 或叫元包 metapackages)来安装整套的软件， 软件样式集会自动安装复杂软件的各种依赖和分散的组件，相当于是一键安装复杂的软件集。 
* CentOS：yum

## 2 软件源安装

软件源安装方式，即通过软件包管理器（apt/yum等）安装，可以自动解决包依赖问题。

通过软件包管理器安装软件本质上是从软件源搜索并下载安装程序，因此所能安装的软件的以及下载的速度都取决于机器配置的软件源。

不同的Linux发行版本的包管理器也不相同，主要分为apt/apt-get/yum/zypper等。

### 2.0 Linux软件源



### 2.1 apt和apt-get

**代表产品**

* Ubuntu16.04
* Debian

Ubuntu16.04版本引入 `apt` 命令， `apt` 更加结构化，为用户提供了管理软件包所需的必要选项。简单来说就是：apt = apt-get、apt-cache 和 apt-config 中最常用命令选项的集合。

> 详细内容参考 [Linux中apt与apt-get命令的区别与解释](https://www.sysgeek.cn/apt-vs-apt-get/)

以下说明不限制必须使用apt/apt-get。

```bash
# 安装软件
apt install package
apt-get install package

# 查看包信息
apt policy package
apt-cache policy package

# 搜索包
apt search package
# 搜索包：使用apt-file
apt install apt-file
apt-file update
apt-file search *.so.1
```

#### 2.1.1 扩展

* Ubuntu使用apt-file解决库或者文件缺失依赖
  * https://www.jianshu.com/p/9fd19418cf83
  * https://blog.csdn.net/quincuntial/article/details/79047050

#### 2.1.2 Ubuntu配置软件源



### 2.2 yum

**代表产品**

* CentOS
* RedHat

```bash
# 安装包
yum install package
# 通过模块找包
yum whatprovides3
```

#### 2.2.1 CentOS配置软件源

centos的yum源默认是国外的服务器，切换成国内的阿里或网易的源。

```bash
# 进入配置目录
cd /etc/yum.repos.d

# 将默认的Base配置文件改名
mv CentOS-Base.repo  CentOS-Base.repo.backup

# 获取网易yum源并替换
# CentOS6
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS6-Base-163.repo

# 更新软件源
yum update
```

## 3 软件包安装

针对特定的软件安装包，使用软件管理工具（dpkg/rpm）进行安装。

### 3.1 dpkg

```bash
# 查看当前机器安装的包
dpkg -l
```

### 3.2 rpm

```bash
# 查找已安装软件中包含的某个安装包
rpm -qa | grep package
# 
rpm 
```



## 4 源码安装



## 5 二进制安装

