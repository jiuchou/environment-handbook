# 02 Linux crontab介绍

> 参考
>
> - [Linux crontab命令详解](https://www.cnblogs.com/ftl1012/p/crontab.html)
> - [crontab的语法规则格式（每分钟、每小时、每天、每周、每月、每年定时执行 规则）](https://blog.csdn.net/xinyflove/article/details/83178876)

## 1 安装及启动

### 1.1 CentOS

```bash
# 安装crontab
yum install crontabs

# 启动服务
/sbin/service crond start
# 关闭服务
/sbin/service crond stop
# 重启服务
/sbin/service crond restart
# 重新载入配置
/sbin/service crond reload

# 查看crontab服务状态
service crond status

# 查看crontab服务是否已设置为开机启动
# 方法1： 界面启动
ntsysv 
# 方法2： 加入开机自动启动
chkconfig –level 35 crond on
```

## 2 crontab介绍

crontab：定时任务的守护进程，精确到分，设计秒的我们一般写脚本  -->相当于闹钟

​	日志文件:  ll /var/log/cron*

​	编辑文件： vim /etc/crontab

​	进程：ps -ef | grep crond  ==> /etc/init.d/crond restart

​	作用：定时备份，实时备份

### 2.1 常见命令参数

```
`usage:  ``crontab` `[-u user] ``file``        ``crontab` `[-u user] [ -e | -l | -r ]``                ``(default operation is replace, per 1003.2)``        ``-e      (edit user's ``crontab``)``        ``-l      (list user's ``crontab``)``        ``-r      (delete user's ``crontab``)``        ``-i      (prompt before deleting user's ``crontab``)``        ``-s      (selinux context)`
```

### 2.2 定时任务分类

Linux下的任务调度分为两类，系统任务调度和用户任务调度。

- 系统任务调度：系统周期性所要执行的工作，比如写缓存数据到硬盘、日志清理等。

  ​	在/etc/crontab文件，这个就是系统任务调度的配置文件。

- 用户任务调度：用户定期要执行的工作，比如用户数据备份、定时邮件提醒等。

  ​        用户可以使用 crontab 工具来定制自己的计划任务。

  ​        在crontab 文件都被保存在/var/spool/cron目录中。其文件名与用户名一致

```bash
1.系统定时任务：例如清理系统日志，清理系统缓存   -->不过多的关注
    查询系统定时处理任务的路径：
        路径1：
            cd /etc/logrotate.d/        -->可以写定时任务
            less syslog 
        路径2：
            cat /etc/crontab   -->不推荐使用，但是可以看格式
        路径3：
             ls /etc/ | grep cron*
                 anacrontab
                 cron.d                 -->同路径2 ，可以写定时任务  
                 cron.daily
                 cron.deny              -->控制普通用户使用定时任务crontab
                 cron.hourly
                 cron.monthly
                 crontab
                 cron.weekly
2.用户的定时任务      -->关注重点
```

### 2.3 crontab文件内容分析

`cat /etc/crontab`

![](/home/jiuchou/Code/environment-handbook/Section2/Linux/book/Second/image/crontab-config-file-description.png)1

前四行是用来配置crond任务运行的环境变量

第一行SHELL变量指定了系统要使用哪个shell，这里是bash

第二行PATH变量指定了系统执行命令的路径

第三行MAILTO变量指定了crond的任务执行信息将通过电子邮件发送给root用户

如果MAILTO变量的值为空，则表示不发送任务执行信息给用户

第四行的HOME变量指定了在执行命令或者脚本时使用的主目录。

小 结：
    数字的表示最好用2为阿拉伯数字显示
    周和日最好不要同时用
    定时任务要加注解
    可以定向到日志文件或者空文件
    定时任务一定是绝对路径，且目录必须存在才能出结果
    crontab 服务一定要开启运行

### 2.4 crontab日志路径

```bash
# 【日志是按照天排列的】
# /var/log/cron只会记录是否执行了某些计划的脚本，但是具体执行是否正确以及脚本执行过程中的一些信息则linux会每次都发邮件到该用户下。
ll /var/log/cron*

less /var/spool/mail/root
```

### 2.5 crontab的注意事项

1. 注意环境变量问题

在crontab文件中定义多个调度任务时，需要特别注意的一个问题就是环境变量的设置

```bash
`# 脚本中涉及文件路径时写全局路径；``# 脚本执行要用到java或其他环境变量时，通过source命令引入环境变量，如：``cat` `start_cbp.sh``#!/bin/sh``source` `/etc/profile``export` `RUN_CONF=``/home/d139/conf/platform/cbp/cbp_jboss``.conf``/usr/local/jboss-4``.0.5``/bin/run``.sh -c mev &` `# 当手动执行脚本OK，但是crontab死活不执行时。可以尝试在crontab中直接引入环境变量解决问题。``0 * * * * . ``/etc/profile``;``/bin/sh` `/var/www/java/audit_no_count/bin/restart_audit``.sh`
```

2. 系统级任务调度与用户级任务调度

```
`root用户的任务调度操作可以通过“``crontab` `–uroot –e”来设置，也可以将调度任务直接写入``/etc/crontab``文件，需要注意的是，如果要定义一个定时重启系统的任务，就必须将任务放到``/etc/crontab``文件，即使在root用户下创建一个定时重启系统的任务也是无效的。`
```

3. 其他注意事项

```
`当``crontab``突然失效时，可以尝试``/etc/init``.d``/crond` `restart解决问题。或者查看日志看某个job有没有执行/报错``tail` `-f ``/var/log/cron``。``千万别乱运行``crontab` `-r。它从Crontab目录（``/var/spool/cron``）中删除用户的Crontab文件。删除了该用户的所有``crontab``都没了。``在``crontab``中%是有特殊含义的，表示换行的意思。如果要用的话必须进行转义\%，如经常用的``date` `‘+%Y%m%d’在``crontab``里是不会执行的，应该换成``date` `‘+\%Y\%m\%d’`
```

4. 生产调试定时任务

```
`1.增加执行任务的频率调试``2.调整系统时间调试任务，提前5分钟   -->不用于生产环境``3.通过脚本日志输出调试定时 任务``4.注意一些任务命令带来的问题        -->确保命令的正确性`
```

5.crontab箴言

```
`1.环境变量问题，例如``crontab``不能识别Java的环境变量``    ``crontab``执行shell时，只能识别为数不多的环境变量，普通的环境变量是无法识别的，所以在编写shell时，最好使用``export``重新声明变量，确保脚本执行。 ``2.命令的执行最好用脚本``3.脚本权限加``/bin/sh``，规范路径``/server/scripts``4.时间变量用反斜线转义，最好用脚本``5.定时任务添加注释``6.>``/dev/null` `2>&1   ==>&>``/dev/null``,别随意打印日志文件``7.定时任务里面的程序脚本尽量用全路径``8.避免不必要的程序以及命令输出``9.定时任务之前添加注释``10.打包到文件目录的上一级`
```

## 3 crontab的语法规则格式（每分钟、每小时、每天、每周、每月、每年定时执行 规则）

### 3.1 crontab的语法规则格式

> 周的数字为 0 或 7 时，都代表“星期天”的意思

| 代表意义 | 分钟 | 小时 | 日期 | 月份 | 周   | 命令           |
| -------- | ---- | ---- | ---- | ---- | ---- | -------------- |
| 数字范围 | 0~59 | 0~23 | 1~31 | 1~12 | 0~7  | 需要执行的命令 |

### 3.2 辅助字符

辅助的字符，大概有下面这些：

| **特殊字符** | **代表意义**                                                 |
| ------------ | ------------------------------------------------------------ |
| *(星号)      | 代表任何时刻都接受的意思。举例来说，`0 12 * * * command` 日、月、周都是*，就代表着不论何月、何日的礼拜几的12：00都执行后续命令的意思。 |
| ,(逗号)      | 代表分隔时段的意思。举例来说，如果要执行的工作是3：00与6：00时，就会是：`0 3,6 * * * command`时间还是有五列，不过第二列是 3,6 ，代表3与6都适用 |
| -(减号)      | 代表一段时间范围内，举例来说，8点到12点之间的每小时的20分都进行一项工作：`20 8-12 * * * command`仔细看到第二列变成8-12.代表 8,9,10,11,12 都适用的意思 |
| /n(斜线)     | 那个n代表数字，即是每隔n单位间隔的意思，例如每五分钟进行一次，则：`*/5 * * * * command`用*与/5来搭配，也可以写成0-59/5，意思相同 |

### 3.3 Crontab格式说明

![](/home/jiuchou/Code/environment-handbook/Section2/Linux/book/Second/image/crontab-format-description.png)



### 3.4 规则案例

1.每分钟定时执行一次规则
每1分钟执行： `*/1 * * * *`或者`* * * * *`
每5分钟执行： `*/5 * * * *`

2.每小时定时执行一次规则：
每小时执行： `0 * * * *`或者`0 */1 * * *`
每天上午7点执行：`0 7 * * *`
每天上午7点10分执行：`10 7 * * *`

3.每天定时执行一次规则：
每天执行 `0 0 * * *`

4.每周定时执行一次规则：
每周执行 `0 0 * * 0`

5.每月定时执行一次规则：
每月执行 `0 0 1 * *`

6.每年定时执行一次规则：
每年执行 `0 0 1 1 *`

7.其他例子

```bash
5 * * * * 指定每小时的第5分钟执行一次ls命令
30 5 * * * ls 指定每天的 5:30 执行ls命令
30 7 8 * * ls 指定每月8号的7：30分执行ls命令
30 5 8 6 * ls 指定每年的6月8日5：30执行ls命令
30 6 * * 0 ls 指定每星期日的6:30执行ls命令[注：0表示星期天，1表示星期1，以此类推，也可以用英文来表示，sun表示星期天，mon表示星期一等。]
30 3 10,20 * * ls 每月10号及20号的3：30执行ls命令[注：“，”用来连接多个不连续的时段]
25 8-11 * * * ls 每天8-11点的第25分钟执行ls命令[注：“-”用来连接连续的时段]
*/15 * * * * ls 每15分钟执行一次ls命令 [即每个小时的第0 15 30 45 60分钟执行ls命令 ]

30 6 */10 * * ls 每个月中，每隔10天6:30执行一次ls命令[即每月的1、11、21、31日是的6：30执行一次ls命令。 ]
```

