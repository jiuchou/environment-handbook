# Vue

* 官方教程： https://cn.vuejs.org/v2/guide/



### vue-cli

[vue-cli3.0官方指南](https://cli.vuejs.org/guide/)

* vue-cli2 介绍： https://blog.csdn.net/xiaoyangerbani/article/details/80735310

### Axios

#### 扩展

> * 内容来自: https://blog.csdn.net/u012369271/article/details/72848102

`axios` 不支持 `vue.use()` 方式声明使用，建议在 `main.js` 中使用如下声明方式，这样在其他vue组件中就可以使用 `this.$axios` 调用

```js
import axios from 'axios';
Vue.prototype.$axios=axios;
```

### Vuex

[官方指南](https://vuex.vuejs.org/)

#### 扩展

* [解决Vuex持久化插件-在F5刷新页面后数据不见的问题](https://www.cnblogs.com/lemoncool/p/9645587.html)
* Vue+Element实现表格的编辑、删除、以及新增行的最优方法： https://blog.csdn.net/wangjie919/article/details/82050411
* npm_config_： https://www.cnblogs.com/amiezhang/p/10665953.html
* 插件中的chalk的用法： https://blog.csdn.net/amanda_wmy/article/details/80611879
* Vue.js经典开源项目汇总： https://www.cnblogs.com/dragonir/p/7402902.html




### UI

#### ElementUI

* 关于Vue ElementUI表格后台排序详解
  * https://blog.csdn.net/fture_bird/article/details/80916227



## 待整理

vue-cli3 一直运行 /sockjs-node/info?t= 解决方案
https://www.cnblogs.com/sichaoyun/p/10178080.html

