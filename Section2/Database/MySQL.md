# MySQL

## 1 基础操作

### 1.1 创建数据库

CREATE DATABASE db_name DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

### 1.2 重排auto_increment（清空表数据后让自增ID仍从1开始）

方法1

```bash
truncate table_name;
```

优点：
1）速度快
2）可以对自增ID进行重排，使自增ID仍从1开始计算

方法2

清空表数据后，使用alter修改表

```bash
alter table table_name auto_increment=1;
```

### 1.3 MySQL字段操作

#### 1.3.1 设置自增主键

```mysql
# 设置自增主键
alter table user_management_report change column `id` `id` int(11) not null primary key AUTO_INCREMENT;
```

#### 1.3.2 增加一列

- https://www.csdn.net/gather_28/MtTaMgxsNjU4OC1ibG9n.html

1.3.3 修改数据库的名字和表名

* https://www.cnblogs.com/Roc-Atlantis/p/9359216.html

1.3.4 修改表字段类型

- https://blog.csdn.net/liu16659/article/details/83115823
- https://www.cnblogs.com/mr-wuxiansheng/p/6891940.html
- https://blog.51cto.com/xiaocao13140/2124941?utm_source=oschina-app

## 2 数据操作

### 2.1 MySQL合并重复数据

> 下列命令中，查询时会获取当前最新的数据，合并后数据保留最老的内容
>
> 如果合并数据时想保留最新的数据，需要将下列命令中的`MIN`替换成`MAX`

```mysql
# 查询最新的重复数据
SELECT * FROM table_name WHERE name='name' AND date>='2019-01-01' AND date<='2020-01-01' AND id NOT IN (SELECT id FROM (SELECT MIN(id) AS id FROM table_name WHERE name='name' AND date>='2019-01-01' AND date<='2020-01-01' GROUP BY table_name.age, table_name.sex HAVING count(*)>=1) m);

# 删除最新的重复数据
DELETE FROM table_name WHERE name='name' AND date>='2019-01-01' AND date<='2020-01-01' AND id NOT IN (SELECT id FROM (SELECT MIN(id) AS id FROM table_name WHERE name='name' AND date>='2019-01-01' AND date<='2020-01-01' GROUP BY table_name.age, table_name.sex HAVING count(*)>=1) m);
```

MySQL表不能修改、删除等操作，卡死、锁死情况的处理办法
* https://blog.csdn.net/test_soy/article/details/79003958
```sql
show full processlist;
kill processid;
```

### 2.2 数据导出

- https://zhidao.baidu.com/question/1823681782192611148.html

```mysql
mysql> select * from tablename into outfile "/tmp/db.txt";
ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
```

一些版本的mysql对通过文件导入导出作了限制，默认不允许，

查看配置，执行mysql命令 `SHOW VARIABLES LIKE "secure_file_priv";`

如果value值为null，则为禁止，如果有文件夹目录，则只允许改目录下文件（测试子目录也不行），如果为空，则不限制目录。

修改配置可修改mysql配置文件，查看是否有 `secure_file_priv = ` 这样一行内容，如果没有，则手动添加。

`secure_file_priv = /home` 表示限制为/home文件夹

`secure_file_priv = ` 表示不限制目录

等号一定要有，否则mysql无法启动。修改完配置文件后，重启mysql生效。

```mysql
mysql> select * from tablename into outfile "/tmp/db.txt";
Query OK, 93 rows affected (0.00 sec)
```



## 3 待整理


```mysql
mysql> show variables;
ERROR 1146 (42S02): Table 'performance_schema.session_variables' doesn't exist
```

```bash
mysql_upgrade -u root -p --force
```

```bash
mysql> show variables;
ERROR 1682 (HY000): Native table 'performance_schema'.'session_variables' has the wrong structure
mysql> set @@global.show_compatibility_56=ON;
```
