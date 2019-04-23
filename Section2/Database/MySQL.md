# MySQL

创建数据库

CREATE DATABASE db_name DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;



1.MySQL合并重复数据

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

Mysql修改表字段类型
* https://blog.csdn.net/liu16659/article/details/83115823
* https://www.cnblogs.com/mr-wuxiansheng/p/6891940.html
* https://blog.51cto.com/xiaocao13140/2124941?utm_source=oschina-app

