# 基于 Docker 镜像搭建 GitLab 平台

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



## 更新记录

```
2019.03.18: 初步整理，增加基于 Docker 镜像搭建 GitLab 服务器文档，同时增加 LDAP 配置。
```



