# SVN

* [勾子](https://www.jianshu.com/p/56b8a31bbcbb)

## SVN Server

1. 创建仓库
```bash
svnadmin create /root/svn/repos_jiuchou
```

2. `svn` 启动
```bash
svnserve -d -r /root/svn/repos_jiuchou
```
