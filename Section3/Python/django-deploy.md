# Docker 部署 Django + Vue 前后端分离项目

>  本方案基于uwsgi + nginx方案实现

## 1 部署后端 Django

### 1.1 制作项目镜像

1. 拉取python:3.6镜像

   * 配置docker国内镜像加速 `vim /etc/docker/daemon.json`

     ```
     {
       "registry-mirrors": [
         "https://3laho3y3.mirror.aliyuncs.com"
       ]
     }
     ```

   * 拉取镜像

     ```bash
     docker pull python:3.7
     ```

2. 配置docker镜像

   编辑 `requirements.txt`

   ```
   django>=2.1.0,<2.2
   django-cors-headers>=2.4.0
   djangorestframework==3.9.4
   django-rest-swagger==2.2.0
   mysqlclient>=1.3.14
   pymssql==2.1.4
   Pillow==6.2.1
   docutils>=0.3
   python-ldap>=3.1.0
   pyjwt>=1.7.1
   suds-jurko>=0.6
   psycopg2-binary>=2.8.3
   django-crontab==0.7.1
   wget==3.2
   # svn==0.3.46
   # svn 依赖 python-dateutil 和 nose
   python-dateutil>=2.8.0
   nose>=1.3.7
   python-jenkins==1.5.0
   uwsgi==2.0.18
   # https://pypi.org/project/django-pyodbc-azure/
   # Supports Microsoft SQL Server 2008/2008R2, 2012, 2014, 2016, 2017 and Azure SQL Database
   django-pyodbc-azure==2.1.0.0
   xlrd==1.2.0
   sqlalchemy==1.3.13
   django-cluster-redis>=1.0.5
   ```


   编辑Dockerfile文件

   ```dockerfile
   FROM python:3.7
   
   LABEL 45128 <yang_kaige@dahuatech.com>
   
   # unixodbc/unixodbc-dev 用来解决 fatal error: sql.h: No such file or directory
   # 参考: https://stackoverflow.com/questions/55929732/error-with-linux-pyodbc-connection-cant-open-lib-sql-server-native-client11-0
   RUN export http_proxy=http://10.1.82.22:3128 \
       && export https_proxy=http://10.1.82.22:3128 \
       && apt-get update \
       && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
       && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
       && apt-get update \
       && apt-get install -y --no-install-recommends \
           libldap2-dev libsasl2-dev \
           jq vim cron rsyslog logrotate \
           unixodbc unixodbc-dev \
       && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
           msodbcsql17 mssql-tools \
       # && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
       && sed -i "s|^#cron|cron|g" /etc/rsyslog.conf \
       && rm -rf /var/lib/apt/lists/*
   
   COPY requirements.txt ./
   RUN export http_proxy=http://1.1.1.1:8080 \
       && export https_proxy=http://1.1.1.1:8080 \
       && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip \
       && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
   
   RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
       && echo 'Asia/Shanghai' > /etc/timezone
   COPY build/apiserver/resolve.conf /etc/resolve.conf
   COPY build/apiserver/logrotate/devops /etc/logrotate.d/
   
   # 修改第三方库
   COPY build/apiserver/rest_framework_swagger/index.html /usr/local/lib/python3.7/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html
   # COPY vendor/svn/common.py /usr/local/lib/python3.6/site-packages/svn/common.py
   COPY vendor/svn/ /usr/local/lib/python3.7/site-packages/svn/
   COPY vendor/svn-0.3.46.dist-info/ /usr/local/lib/python3.7/site-packages/svn-0.3.46.dist-info/
   
   # 使用 devops 用户部署环境
   RUN groupadd -g 1011 devops \
       && useradd -m -d /home/devops -s /bin/bash -u 1011 -g devops devops
       # "$6$eryoFf6M$3fM4TvESBHkkudaxCYU9GhysQnS1MmKg.4cNkf2kWnKJSeriQo1Dk5WvkNRMfngXtbezhbZhj5dMaX4XULNfQ0" \
   
   WORKDIR /home/devops
   COPY opslab/ /home/devops
   COPY build/apiserver/uwsgi.ini /home/devops
   COPY build/apiserver/2b4d9a15bd3b53673a9ee3255f90d443 /root/.subversion/auth/svn.simple/2b4d9a15bd3b53673a9ee3255f90d443
   COPY build/apiserver/a98cc98ec220a5818ff12f5bf4c24311 /root/.subversion/auth/svn.simple/a98cc98ec220a5818ff12f5bf4c24311
   COPY build/apiserver/vimrc /home/devops/.vimrc
   COPY build/apiserver/bashrc /home/devops/.bashrc
   RUN mkdir -p /home/devops/static
   #RUN sed -i "s|^# from .development|from .development|g" /home/devops/opslab/settings/__init__.py
   RUN sed -i "s|^# from .production|from .production|g" /home/devops/opslab/settings/__init__.py
   RUN python manage.py collectstatic
   # RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
   # RUN echo 'export LC_CTYPE="C.UTF-8"' >> ~/.bashrc
   
   RUN chown devops:devops -R /home/devops
   RUN find /home/devops -type d | xargs -i chmod 750 -R {}
   RUN find /home/devops -type f | xargs -i chmod 640 {}
   
   # USER devops
   
   # EXPOSE 8000
   EXPOSE 8000 8080
   CMD uwsgi --ini /home/devops/uwsgi.ini
   # ENTRYPOINT /usr/local/bin/uwsgi --ini /home/devops/uwsgi.ini && /bin/bash
   ```


   编辑uwsgi.ini文件

   ```
   [uwsgi]
   # 配置参考
   # https://www.iteye.com/blog/heipark-1847421
   
   # 项目目录，目录为项目运行时的绝对路径
   # 部署新的项目后需要修改该路径为项目的绝对路径
   chdir   = /home/devops
   # 项目的app下的wsgi
   module  = opslab.wsgi:application
   # sock的文件路径
   # socket=/usr/src/opslab/uwsgi.sock
   # socket后面接uwsgi启动地址和端口号，到时候nginx就会通过socket连接这个地址和端口号
   socket  = :8000
   http = :8080
   # 指定静态文件
   static-map=/backend_static=/static
   
   # 启用主进程
   master      = true
   # 运行进程数
   processes   = 4
   # 线程数
   threads = 8
   # 启用线程
   enable-threads  = true
   
   workers     = 5
   
   thunder-lock    = true
   
   pidfile     = uwsgi.pid
   # 仅将日志记录到文件
   logto           = /home/devops/log/uwsgi.log
   # 设置日志目录
   # daemonize       = /home/devops/log/uwsgi.log
   # 缓存大小
   buffer-size     = 21573
   # 自动移除unix Socket和pid文件当服务停止的时候
   vacuum          = true
   # uid = devops
   # gid = devops
   ```

3. 构建镜像

   ```bash
   docker build -t backend  .
   ```

### 1.2 启动容器

```bash
# 开放http端口
docker run -ti -d -p 8001:8000 -p 8081:8080 --name apiserver1 backend bash
# 不开放http端口
docker run -ti -d -p 8002:8000 --name apiserver2 backend bash
```

## 2 部署前端 Vue

### 2.1 制作前端镜像

1. 拉取nginx镜像

   ```bash
   docker pull nginx
   ```

2. 配置docker镜像

   编辑Dockerfile文件

   ```dockerfile
   FROM nginx
   
   LABEL 45128 <yang_kaige@dahuatech.com>
   
   COPY dist/ /usr/share/nginx/html/
   COPY build/nginx.conf /etc/nginx/nginx.conf
   COPY build/default.conf /etc/nginx/conf.d/default.conf
RUN chmod 755 -R /usr/share/nginx/html/
   ```

   编辑 `nginx.conf`
   
   ```
   user  nginx;
   # worker_processes  1;
   worker_processes  16;
   
   error_log  /var/log/nginx/error.log warn;
   pid        /var/run/nginx.pid;
   
   
   events {
       # worker_connections  1024;
       worker_connections  4096;
   }
   
   
   http {
       include       /etc/nginx/mime.types;
       default_type  application/octet-stream;
   
       log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                         '$status $body_bytes_sent "$http_referer" '
                         '"$http_user_agent" "$http_x_forwarded_for"';
   
       access_log  /var/log/nginx/access.log  main;
   
       sendfile        on;
       #tcp_nopush     on;
   
       keepalive_timeout  65;
   
       #gzip  on;
       # https://blog.csdn.net/huangbaokang/article/details/79931429
       #开启gzip
       gzip  on;
       # 低于1kb的资源不压缩
       gzip_min_length 1k;
       # 压缩级别【1-9】，越大压缩率越高，同时消耗cpu资源也越多，建议设置在4左右。
       gzip_comp_level 3;
       # 需要压缩哪些响应类型的资源，多个空格隔开。
       # 不建议压缩图片，会消耗大量的cpu资源，且不一定有明显的效果。
       gzip_types text/plain application/javascript application/x-javascript text/javascript text/xml text/css;
       #配置禁用gzip条件，支持正则。此处表示ie6及以下不启用gzip（因为ie低版本不支持）
       gzip_disable "MSIE [1-6]\.";
       # 是否添加“Vary: Accept-Encoding”响应头
       gzip_vary on;
   
       include /etc/nginx/conf.d/*.conf;
   }
   ```

   编辑default.conf文件
   
   ```
    upstream apiserver {
        server devops.com:8001;
        server devops.com:8002;
        server devops.com:8003;
    }

    server {
        listen      80;
        server_name localhost;

        location / {
            root        /usr/share/nginx/html;
            index       index.html index.htm;
            try_files   $uri $uri/ /index.html;
        }

        location /api {
            rewrite /(.*)   /$1 break;
            add_header              Access-Control-Allow-Origin *;
            add_header              Access-Control-Allow-Headers "Origin, X-Requested-With, Content-Type, Acept";
            add_header              Access-Control-Allow-Methods "GET, POST, OPTIONS";
            uwsgi_connect_timeout   3000;
            uwsgi_send_timeout      3000;
            uwsgi_read_timeout      3000;
            uwsgi_pass  apiserver;
            include     /etc/nginx/uwsgi_params;
        }
   
       location /swagger {
           rewrite /(.*)   /$1 break;
           add_header              Access-Control-Allow-Origin *;
           add_header              Access-Control-Allow-Headers "Origin, X-Requested-With, Content-Type, Acept";
           add_header              Access-Control-Allow-Methods "GET, POST, OPTIONS";
           uwsgi_connect_timeout   30000;
           uwsgi_send_timeout      30000;
           uwsgi_read_timeout      30000;
           uwsgi_param Host        $Host;
           uwsgi_param X-Real-IP   $remote_addr;
           uwsgi_param X-Forwarded-For $proxy_add_x_forwarded_for;
           uwsgi_param X-Forwarded-Proto   $http_x_forwarded_proto;
           uwsgi_pass  apiserver;
           include     /etc/nginx/uwsgi_params;
       }
   
       location /backend_static {
           rewrite /(.*)   /$1 break;
           uwsgi_connect_timeout   30000;
           uwsgi_send_timeout      30000;
           uwsgi_read_timeout      30000;
           uwsgi_pass  apiserver;
           include     /etc/nginx/uwsgi_params;
       }
   
   
       error_page  500 502 503 504 /50x.html;
       location = /50x.html {
           root    /usr/share/nginx/html;
       }
   }
   ```
   
   拷贝vue的产物目录dist到Dockerfile文件同级目录下
   
   构建镜像
   
   ```bash
   docker build -t console .
   ```
### 2.1 启动容器

```bash
docker run -ti -d -p 3000:80 --name console console
```

