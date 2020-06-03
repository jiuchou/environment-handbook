# Linux wget

wget 失败

linux 下载 命令 wget 和 curl
https://blog.csdn.net/freeking101/article/details/53691481

wget失败问题

1.禁用
https://www.cnblogs.com/daocaoren/archive/2011/06/07/2074492.html

解决wget被某些网站禁用
现在比较喜欢阅读HTML的电子书，PDF中往回跳转不是很方便，并且PDF阅读器都很臃肿，对于不需要添加脚注等特殊需求的电子书，HTML应该是首选了，只需要浏览器就能浏览，而且速度很快。

  Linux下的wget可谓是网站镜像的利器，在~/.bashrc中做了一个别名，alias getsite='wget -r -k -p -np'，这样见到网上好的电子书时，只需要:
  getsite http://url/to/html/book

即可。

　但是今天碰到一个网站，用浏览器可以打开，但是wget就立刻返回403。一开始还以为是robots.txt文件限制了wget，但是增加robotx=off让wget忽略robots之后仍然是这个错误。经过一番搜索明白了，原来某些站点禁止了wget这个User Agent，估计就是为了防止整站下载，带来过多的流量和盗版吧。（呃，那我下载这个网站有点太邪恶了……） 

  问题找到了就可以解决了，给wget加上参数：-U NoSuchBrowser/1.0 这样对方看到的UA就不是wget了，顺利下载……

　问题是解决了，不过最后提醒一下读者，如果有的网站禁止了wget，肯定有其原因，最好还是不要用wget去下载了，更不要盗版…… 

2.host问题
http://ju.outofmemory.cn/entry/251802
url加引号

wget -U NoSuchBrowser/1.0 "http://10.1.248.186:22222/finish-product/0ecf1472-2c02-4f59-9123-cdd6ee744a06?AWSAccessKeyId=FA0X9MVACQHVXPWDQAJE&Expires=1566371063&Signature=M4DLj7QV7cyZDxKgbIVXAOxGVmg%3D" -O "aa"

import wget
wget.download("http://10.1.248.186:22222/finish-product/0ecf1472-2c02-4f59-9123-cdd6ee744a06?AWSAccessKeyId=FA0X9MVACQHVXPWDQAJE&Expires=1566371063&Signature=M4DLj7QV7cyZDxKgbIVXAOxGVmg%3D", out="z.zip")
