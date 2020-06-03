# Python网络相关库

## python操作curl

* pycurl

* libcurl 文档：https://curl.haxx.se/libcurl/c/curl_easy_getinfo.html

```python
import io
import pycurl

buf = io.BytesIO()
curl = pycurl.Curl()
curl.setopt(pycurl.WRITEFUNCTION, buf.write)
curl.setopt(pycurl.CONNECTTIMEOUT, 5)
curl.setopt(pycurl.TIMEOUT, 5400)
curl.setopt(pycurl.NOPROGRESS, 0)
curl.setopt(pycurl.MAXREDIRS, 1)
url = 'http://www.baidu.com/download'
curl.setopt(pycurl.URL, url)
curl.setopt(pycurl.USERPWD, 'username:password')

curl.perform()

the_page = buf.getvalue()
buf.close()
```

