# 1.1.3.用户管理

> 创建用户及用户组

- [linux下查看所有用户及所有用户组](https://www.cnblogs.com/jackyyou/p/5498083.html)

## 创建用户

### 命令行

groupadd jenkins

useradd -d /home/jenkins -s /bin/bash -c "jenkins user" -g jenkins -G docker -m -p "jenkins" jenkins

### 文件

如何解决普通用户无法su到root用户的问题？
https://blog.csdn.net/lianjoke0/article/details/82598149