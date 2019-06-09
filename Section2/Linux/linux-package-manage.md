# Linux 包管理

## Ubuntu

### apt

```bash
apt install package

apt-get install package

apt policy package

apt-cache policy package

dpkg -l

apt search package
```



### apt-file

```bash
apt install apt-file

apt-file update

apt-file search *.so.1
```



* Ubuntu使用apt-file解决库或者文件缺失依赖
  * https://www.jianshu.com/p/9fd19418cf83
  * https://blog.csdn.net/quincuntial/article/details/79047050



## CentOS

* yum whatprovides 通过模块找包



