# 基于 Docker 镜像搭建 GitLab 平台

<!-- TOC -->

- [基于 Docker 镜像搭建 GitLab 平台](#基于-docker-镜像搭建-gitlab-平台)
    - [0 扉页](#0-扉页)
    - [1 基于 Docker 镜像搭建 GitLab 平台](#1-基于-docker-镜像搭建-gitlab-平台)
        - [1.1 获取镜像](#11-获取镜像)
        - [1.2 启动 GitLab 容器](#12-启动-gitlab-容器)
        - [1.3 GitLab 对接 LDAP 用户认证](#13-gitlab-对接-ldap-用户认证)
    - [2 GitLab 相关](#2-gitlab-相关)
        - [2.1 查询 GitLab 版本](#21-查询-gitlab-版本)
    - [3 GitLab 数据迁移](#3-gitlab-数据迁移)
        - [3.1 GitLab 数据迁移方式](#31-gitlab-数据迁移方式)
        - [3.2 失败问题](#32-失败问题)
            - [3.2.1 启动失败](#321-启动失败)
            - [3.2.2 SSH协议连接仓库失败](#322-ssh协议连接仓库失败)
    - [4 更新记录](#4-更新记录)

<!-- /TOC -->

* 参考

  * [GitLab安装、使用教程（Docker版）](https://www.imooc.com/article/23168?block_id=tuijian_wz)

## 0 扉页

## 1 基于 Docker 镜像搭建 GitLab 平台

### 1.1 获取镜像

1. 官方网站
   ```bash
   docker pull gitlab/gitlab-ce:latest
   ```

2. 阿里云仓库

   ```bash
   docker pull registry.cn-hangzhou.aliyuncs.com/imooc/gitlab-ce:latest
   ```

### 1.2 启动 GitLab 容器

> Tip:
>
> ​	1.根据实际情况修改 `HOST_NAME`，`GITLAB_PATH` 的值。如果 `HOST_NAME` 配置为域名，则需要配置域名解析服务。
>
> ​	2.宿主机 `80` 端口未被占用的情况下，建议使用宿主机 `80` 端口映射容器 `80` 端口。否则在进行访问和地址显示时需另外配置。

```bash
HOST_NAME="www.gitlab.com"
GITLAB_PATH="/home/gitlab"
docker run -d --hostname ${HOST_NAME} \
	-p 80:80 -p 10443:443 -p 10022:22 \
	--name gitlab \
	-v ${GITLAB_PATH}/config:/etc/gitlab \
	-v ${GITLAB_PATH}/logs:/var/log/gitlab \
	-v ${GITLAB_PATH}/data:/var/opt/gitlab \
	registry.cn-hangzhou.aliyuncs.com/imooc/gitlab-ce:latest
```

### 1.3 GitLab 对接 LDAP 用户认证

> 官方文档: https://docs.gitlab.com/ee/administration/auth/ldap.html

**修改配置文件 gitlab.rb**

`vim /etc/gitlab/gitlab.rb`

```bash
# 开启ldap
gitlab_rails['ldap_enabled'] = true
gitlab_rails['ldap_servers'] = YAML.load <<-'EOS' ###! **remember to close this block with 'EOS' below**
main: # 'main' is the GitLab 'provider ID' of this LDAP server
    label: 'LDAP'
    host: '192.168.1.1'
    port: 389
    uid: 'sAMAccountName'
    #bind_dn: 'cn=Manager,dc=abc,dc=cn'
    bind_dn: 'manager_dn@email.com'
    password: '123456'
    encryption: 'plain'
    verify_certificates: false
    active_directory: true
    allow_username_or_email_login: false
    block_auto_created_users: false
    # base: 'OU=部门，DC=公司，DC=com'
    base: 'OU=Develop，DC=gitlab，DC=com'
    user_filter: ''
    group_base: ''
    admin_group: ''
    sync_ssh_keys: false
EOS
```

**重新加载新配置**

`gitlab-ctl reconfigure`

**查看是否能正常获取用户列表**

`gitlab-rake gitlab:ldap:check`

## 2 GitLab 相关

### 2.1 查询 GitLab 版本

```bash
cat /opt/gitlab/embedded/service/gitlab-rails/VERSION
```

## 3 GitLab 数据迁移

### 3.1 GitLab 数据迁移方式

1.打包 `${GITLAB_PATH}` 目录到新机器的 `${GITLAB_PATH}（默认为：/home/gitlab）` 目录下

2.启动新的容器服务

```
HOST_NAME="www.gitlab-1.com"
GITLAB_PATH="/home/gitlab"
docker run -d --hostname ${HOST_NAME} \
	-p 80:80 -p 10443:443 -p 10022:22 \
	--name gitlab \
	-v ${GITLAB_PATH}/config:/etc/gitlab \
	-v ${GITLAB_PATH}/logs:/var/log/gitlab \
	-v ${GITLAB_PATH}/data:/var/opt/gitlab \
	registry.cn-hangzhou.aliyuncs.com/imooc/gitlab-ce:latest
```

### 3.2 失败问题

#### 3.2.1 启动失败

**背景**

由于公司资源问题，以非最佳实践方式（服务器、执行机一体）使用服务器主机，导致服务异常卡死，原有容器无法操作。强制删除原有容器服务，启动新容器服务并将原有数据挂载进新容器，新容器启动失败。

详细报错参考 [使用docker部署gitlab之后，数据迁移的问题](https://www.oschina.net/question/2607587_2274426)

**原因**

由于之前误操作宿主机，将挂载目录/home/gitlab权限和权限组修改为root，导致此问题。

（容器场景下）使用 `docker logs -f container_id` 查看日志

```
If this container fails to start due to permission problems try to fix it by executing:

  docker exec -it gitlab update-permissions
  docker restart gitlab
```

**解决方案**

```
docker exec -it gitlab update-permissions
docker restart gitlab
```

#### 3.2.2 SSH协议连接仓库失败

**背景**

进行 `GitLab` 数据迁移重新启动 `GitLab` 服务后，使用SSH协议连接仓库失败

```
root@ubuntu:~# git clone ssh://git@127.0.0.1:10022/USERNAME/repositry.git
Cloning into 'repositry'...
Read from socket failed: Connection reset by peer
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

**原因**

由于之前误操作宿主机，将挂载目录/home/gitlab权限和权限组修改为root，导致此问题。

（容器场景下）使用 `docker logs -f container_id` 查看日志

```
==> /var/log/gitlab/sshd/current <==
2019-05-09_02:10:47.90937 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
2019-05-09_02:10:47.90941 @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
2019-05-09_02:10:47.90941 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
2019-05-09_02:10:47.90941 Permissions 0775 for '/etc/gitlab/ssh_host_rsa_key' are too open.
2019-05-09_02:10:47.90941 It is required that your private key files are NOT accessible by others.
2019-05-09_02:10:47.90942 This private key will be ignored.
2019-05-09_02:10:47.90942 key_load_private: bad permissions
2019-05-09_02:10:47.90942 Could not load host key: /etc/gitlab/ssh_host_rsa_key
```

**解决方案**

登录容器，修改 `ssh_host_rsa_key` 和 `ssh_host_rsa_key.pub` 文件权限修改为之前的权限。

```bash
chown -R 998:998 ssh_host_rsa_key.*
```


## 4 更新记录

```
2019.03.18: 初步整理，增加基于 Docker 镜像搭建 GitLab 服务器文档，同时增加 LDAP 配置
2019.05.09: 增加 GitLab 数据迁移内容
```

