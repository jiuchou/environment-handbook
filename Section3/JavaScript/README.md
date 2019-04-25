# JavaScript
<!-- TOC -->

- [JavaScript](#javascript)
    - [第一部分 Vue](#第一部分-vue)
        - [1 网页标题栏添加favicon.ico图标](#1-网页标题栏添加faviconico图标)
            - [1.1 favicon.ico图标文件制作](#11-faviconico图标文件制作)
            - [1.2 favicon.ico图标不显示](#12-faviconico图标不显示)
                - [1.2.1 部署问题](#121-部署问题)
                - [1.2.2 缓存问题](#122-缓存问题)
                - [1.2.3 路径错误](#123-路径错误)

<!-- /TOC -->
## 第一部分 Vue

### 1 网页标题栏添加favicon.ico图标

#### 1.1 favicon.ico图标文件制作

> 建议图标大小为 `16*16` 或 `32*32`
>
> 根据实际测试，超过 32x32 的 favicon.ico 图标，不但效果没有明显改变，而且还会导致某些浏览器无法展示。而且之前的谷歌网站图标缓存服务器，超过 16kb 就不会缓存，而是直接展示默认的图标。而 **16x16** **和 32x32** **的网站图标，实际展示在浏览器标签栏的效果也没有很明显的区别**。
>
> 所以，对于网站 favicon.ico 图标的大小，建议大家选择 16x16 或者 32x32，再大也是完全没有必要的。效果不见涨，还可能会影响网站速度。
>
> （以上说明内容转载自 [关于网站图标favicon.ico那点事儿](https://zhang.ge/4344.html)）

1.准备好合适的图标图片文件

2.使用 `在线ico图标转换工具` 制作图标文件

可用 `在线ico图标转换工具` 推荐：

* http://www.faviconico.org/
* http://www.bitbug.net/
* https://www.favicon.cc/

#### 1.2 favicon.ico图标不显示

##### 1.2.1 部署问题

**背景**

​	django+vue前后端分离项目，内部项目，无域名。

​	favicon.ico配置如下：

​		1.favicon.ico放置在public目录下

​		2.在入口文件 `public/index.html` 中使用如下方式调用 `<link rel="icon" href="/favicon.ico">`

**现象**

​	使用 `npm run dev` 进行前端测试时显示正常，使用 `npm run build` 打包后，将生成文件部署至Django项目中，无法显示。

**原因**

​	没有配置域名，当以绝对路径访问项目时，不能正常引入favicon.ico

**解决方案**

​	**方案一** 配置域名（如果暂时无配置域名计划，可使用方案一）

​	**方案二** 将favicon.ico放在static目录下，然后在入口文件 `public/index.html` 中使用如下方式调用

```html
<link rel="icon" href="/static/favicon.ico">
```

##### 1.2.2 缓存问题

> 暂无案例
>
> **原因**
>
> ​	可能是浏览器缓存的问题，只要清除浏览器缓存就好

##### 1.2.3 路径错误

> 暂无案例
>
> **原因**
>
> ​	图标文件 `favicon.ico` 路径出错，找到 `favicon.ico` 绝对路径如能正常显示，则为引入图标时路径出错

