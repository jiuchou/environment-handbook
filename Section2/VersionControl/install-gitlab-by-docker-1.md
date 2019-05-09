### 3 GitLab 数据迁移

#### 3.1 GitLab

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

#### 3.2 失败问题

##### 1. 启动失败

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
