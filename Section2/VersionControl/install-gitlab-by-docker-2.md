##### 2. GitLab服务启动成功后，使用SSH协议连接仓库失败问题

**报错**

```bash
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
