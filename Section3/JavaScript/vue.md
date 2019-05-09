### Axios

#### 扩展

> * 内容来自: https://blog.csdn.net/u012369271/article/details/72848102

`axios` 不支持 `vue.use()` 方式声明使用，建议在 `main.js` 中使用如下声明方式，这样在其他vue组件中就可以使用 `this.$axios` 调用

```js
import axios from 'axios';
Vue.prototype.$axios=axios;
```

