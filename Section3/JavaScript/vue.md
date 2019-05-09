# Vue

[官方教程](https://cn.vuejs.org/v2/guide/)



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